#!/usr/bin/env python3
"""
Вырезает фрагмент страницы (рисунок, график, труднодочитываемую формулу)
и сохраняет его как отдельное изображение — для вставки в итоговый документ
или просто чтобы рассмотреть формулу крупнее перед транскрипцией.

Координаты задаются ЛИБО в долях от размера изображения (0.0-1.0, удобно
прикидывать на глаз, глядя на страницу), ЛИБО в пикселях.

Использование:
    python crop_region.py страница.png вырезка.png --frac 0.05,0.10,0.55,0.40
    python crop_region.py страница.png вырезка.png --px 40,80,620,310 --zoom 2
"""

import argparse
from pathlib import Path

from PIL import Image


def parse_box(s):
    parts = [float(x) for x in s.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("Нужно ровно 4 числа: left,top,right,bottom")
    return tuple(parts)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("input_image")
    parser.add_argument("output_image")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--frac", type=parse_box, help="left,top,right,bottom в долях 0..1")
    group.add_argument("--px", type=parse_box, help="left,top,right,bottom в пикселях")
    parser.add_argument(
        "--zoom", type=float, default=1.0,
        help="Увеличить вырезку в N раз (полезно для мелких индексов и значков)",
    )
    args = parser.parse_args()

    img = Image.open(args.input_image)
    w, h = img.size

    if args.frac:
        l, t, r, b = args.frac
        box = (round(l * w), round(t * h), round(r * w), round(b * h))
    else:
        box = tuple(round(v) for v in args.px)

    if box[0] >= box[2] or box[1] >= box[3]:
        raise SystemExit(f"Некорректная область выреза {box}: left/top должны быть меньше right/bottom")

    crop = img.crop(box)
    if args.zoom != 1.0:
        new_size = (round(crop.width * args.zoom), round(crop.height * args.zoom))
        crop = crop.resize(new_size, Image.LANCZOS)

    out_path = Path(args.output_image)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    crop.save(out_path)
    print(f"Сохранено: {out_path} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
