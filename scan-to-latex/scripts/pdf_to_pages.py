#!/usr/bin/env python3
"""
Нормализует входные данные (PDF или набор изображений) в последовательность
страниц page_001.png, page_002.png, ... в указанной выходной папке.

Использование:
    python pdf_to_pages.py <входной_путь> <папка_вывода> [--dpi 300] [--start N] [--end N]

<входной_путь> может быть:
  - PDF-файлом — будет растеризован постранично;
  - папкой с изображениями (png/jpg/jpeg/tif/tiff/bmp/webp) — файлы будут
    скопированы и переименованы в порядке сортировки имён (проверь порядок
    сам, если это фотографии с произвольными именами вроде IMG_2031.jpg).

Для PDF используется (в порядке предпочтения):
  1. PyMuPDF (pip install pymupdf) — не требует системных утилит.
  2. pdftoppm из poppler-utils, если он есть в PATH.

Результат: в папке вывода появятся page_NNN.png и manifest.json с числом
страниц и путями к файлам — manifest.json используется check_document.py
для проверки, что ни одна страница не потеряна при транскрипции.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}


def render_with_pymupdf(pdf_path, out_dir, dpi, start, end):
    import fitz  # PyMuPDF

    doc = fitz.open(str(pdf_path))
    total = doc.page_count
    start = start or 1
    end = end or total
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    pad = max(3, len(str(total)))
    written = []
    for i in range(start - 1, end):
        page = doc[i]
        pix = page.get_pixmap(matrix=matrix)
        out_path = out_dir / f"page_{i + 1:0{pad}d}.png"
        pix.save(str(out_path))
        written.append(str(out_path))
    return total, written


def render_with_pdftoppm(pdf_path, out_dir, dpi, start, end):
    info = subprocess.run(["pdfinfo", str(pdf_path)], capture_output=True, text=True)
    total = None
    for line in info.stdout.splitlines():
        if line.lower().startswith("pages:"):
            total = int(line.split(":")[1].strip())
    if total is None:
        raise RuntimeError("Не удалось определить количество страниц через pdfinfo")

    start = start or 1
    end = end or total
    prefix = out_dir / "raw"
    cmd = [
        "pdftoppm", "-png", "-r", str(dpi),
        "-f", str(start), "-l", str(end),
        str(pdf_path), str(prefix),
    ]
    subprocess.run(cmd, check=True)

    pad = max(3, len(str(total)))
    written = []
    raw_files = sorted(out_dir.glob("raw-*.png"))
    for idx, raw_file in enumerate(raw_files, start=start):
        target = out_dir / f"page_{idx:0{pad}d}.png"
        raw_file.rename(target)
        written.append(str(target))
    return total, written


def normalize_images(input_dir, out_dir):
    files = sorted(
        p for p in Path(input_dir).iterdir()
        if p.suffix.lower() in IMAGE_EXTS
    )
    if not files:
        raise RuntimeError(f"В папке {input_dir} не найдено изображений ({sorted(IMAGE_EXTS)})")
    pad = max(3, len(str(len(files))))
    written = []
    for idx, f in enumerate(files, start=1):
        target = out_dir / f"page_{idx:0{pad}d}{f.suffix.lower()}"
        shutil.copyfile(f, target)
        written.append(str(target))
    return len(files), written


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("input_path")
    parser.add_argument("output_dir")
    parser.add_argument(
        "--dpi", type=int, default=300,
        help="Разрешение растеризации PDF (по умолчанию 300; для мелких индексов/формул — 400-600)",
    )
    parser.add_argument("--start", type=int, default=None, help="Первая страница PDF (1-based)")
    parser.add_argument("--end", type=int, default=None, help="Последняя страница PDF (включительно)")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"Не найден входной путь: {input_path}", file=sys.stderr)
        sys.exit(1)

    if input_path.is_dir():
        total, written = normalize_images(input_path, out_dir)
        manifest = {"source": str(input_path), "type": "images", "total_pages": total, "pages": written}

    elif input_path.suffix.lower() == ".pdf":
        backend = None
        try:
            total, written = render_with_pymupdf(input_path, out_dir, args.dpi, args.start, args.end)
            backend = "pymupdf"
        except ImportError:
            if shutil.which("pdftoppm") is None:
                print(
                    "Не найден ни PyMuPDF, ни pdftoppm. Установите одно из:\n"
                    "  pip install pymupdf\n"
                    "  (или системно) apt-get install poppler-utils   /   brew install poppler",
                    file=sys.stderr,
                )
                sys.exit(1)
            total, written = render_with_pdftoppm(input_path, out_dir, args.dpi, args.start, args.end)
            backend = "pdftoppm"
        manifest = {
            "source": str(input_path), "type": "pdf", "backend": backend,
            "dpi": args.dpi, "total_pages": total, "pages": written,
        }

    else:
        print(
            f"Не понимаю, что делать с {input_path}: ожидается PDF-файл или папка с изображениями.",
            file=sys.stderr,
        )
        sys.exit(1)

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Готово: {len(written)} страниц в {out_dir}")
    print(f"Манифест: {manifest_path}")


if __name__ == "__main__":
    main()
