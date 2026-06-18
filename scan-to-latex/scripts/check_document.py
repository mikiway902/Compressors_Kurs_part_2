#!/usr/bin/env python3
"""
Проверяет итоговый Markdown-файл с оцифрованным текстом на типичные проблемы:
  - несбалансированные $ / $$ / { }  (признак незакрытой формулы)
  - пропущенные или повторяющиеся страницы (по маркерам <!-- page N -->)
  - подозрительно короткие страницы (возможно, пропущена транскрипция)
  - места, явно помеченные как неразборчивые/неуверенные

Это проверка на ОЧЕВИДНЫЕ структурные проблемы, а не гарантия того, что
содержимое формул верно — смысловую сверку с оригиналом она не заменяет.

Использование:
    python check_document.py итог.md [--expected-pages 48]

--expected-pages удобно брать из pages/manifest.json (поле total_pages),
который создаёт pdf_to_pages.py.
"""

import argparse
import re
import sys
from pathlib import Path

PAGE_MARKER_RE = re.compile(r"<!--\s*page\s+(\d+)\s*-->", re.IGNORECASE)
UNCERTAIN_MARKERS = ["[?]", "[нечитаемо]", "[неразборчиво]", "(?)", "???"]


def check_dollar_balance(text):
    issues = []
    double_count = text.count("$$")
    if double_count % 2 != 0:
        issues.append(f"Нечётное число '$$' ({double_count}) — есть незакрытый блок формулы")

    # убираем $$...$$ блоки перед проверкой одиночных $, чтобы не путать их друг с другом
    stripped = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
    single_count = stripped.count("$")
    if single_count % 2 != 0:
        issues.append(f"Нечётное число одиночных '$' вне блоков $$ ({single_count}) — есть незакрытая формула")
    return issues


def check_brace_balance(text):
    issues = []
    open_n = text.count("{")
    close_n = text.count("}")
    if open_n != close_n:
        issues.append(f"Не совпадает число '{{' ({open_n}) и '}}' ({close_n}) — возможна сломанная LaTeX-конструкция")
    return issues


def check_pages(text, expected_pages):
    matches = list(PAGE_MARKER_RE.finditer(text))
    issues = []
    if not matches:
        issues.append(
            "Не найдено ни одного маркера страницы (<!-- page N -->) — "
            "добавляй их при транскрипции, иначе невозможно проверить полноту"
        )
        return issues

    numbers = [int(m.group(1)) for m in matches]
    found = set(numbers)

    dupes = sorted({n for n in numbers if numbers.count(n) > 1})
    if dupes:
        issues.append(f"Повторяющиеся маркеры страниц: {dupes}")

    total = expected_pages or max(found)
    missing = sorted(set(range(1, total + 1)) - found)
    if missing:
        issues.append(f"Отсутствуют страницы: {missing}")

    # длины разделов между соседними маркерами — для поиска подозрительно коротких страниц
    lengths = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        lengths.append((int(m.group(1)), end - m.start()))

    sizes = sorted(l for _, l in lengths)
    if sizes:
        median = sizes[len(sizes) // 2]
        threshold = max(80, median * 0.15)
        short_pages = [num for num, l in lengths if l < threshold]
        if short_pages:
            issues.append(f"Подозрительно короткие страницы (возможно, пропущена транскрипция): {short_pages}")

    return issues


def check_uncertain(text):
    lines = text.splitlines()
    hits = []
    for i, line in enumerate(lines, start=1):
        for marker in UNCERTAIN_MARKERS:
            if marker in line:
                hits.append((i, marker, line.strip()[:100]))
    return hits


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("markdown_file")
    parser.add_argument("--expected-pages", type=int, default=None)
    args = parser.parse_args()

    path = Path(args.markdown_file)
    text = path.read_text(encoding="utf-8")

    print(f"Проверка файла: {path}\n")

    all_issues = []
    all_issues += check_dollar_balance(text)
    all_issues += check_brace_balance(text)
    all_issues += check_pages(text, args.expected_pages)

    if all_issues:
        print("⚠ Найдены проблемы:")
        for issue in all_issues:
            print(f"  - {issue}")
    else:
        print("✓ Базовые проверки (баланс $, {}, страницы) пройдены")

    uncertain = check_uncertain(text)
    if uncertain:
        print(f"\nℹ Помечено как неуверенное/неразборчивое ({len(uncertain)} мест) — стоит перепроверить вручную:")
        for line_no, marker, snippet in uncertain[:30]:
            print(f"  строка {line_no} [{marker}]: {snippet}")
        if len(uncertain) > 30:
            print(f"  ... и ещё {len(uncertain) - 30}")

    sys.exit(1 if all_issues else 0)


if __name__ == "__main__":
    main()
