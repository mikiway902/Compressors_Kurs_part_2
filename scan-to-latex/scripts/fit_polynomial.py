#!/usr/bin/env python3
"""
Подбирает многочлен (полином) по набору точек (x, y), снятых ГЛАЗОМ
непосредственно с графика — для случаев, когда методичка задаёт зависимость
не формулой, а кривой на чертеже (характеристики, номограммы, экспериментальные
кривые типа "коэффициент потерь от угла атаки" и т.п.).

Координаты задаются в ЕДИНИЦАХ ОСЕЙ графика (а не в пикселях изображения) —
координатная сетка на самом чертеже уже является линейкой, поэтому отдельная
калибровка "пиксели -> единицы" не нужна: смотришь на график, по сетке
прикидываешь, через какие (x, y) проходит кривая, и подаёшь эти точки сюда.

Использование:
    python fit_polynomial.py --points "20,5.0;30,6.2;40,7.9;55,9.5;70,9.9;80,9.6" --auto
    python fit_polynomial.py --points-file points.csv --degree 3 --var "beta_1,i_0"

--points        точки через ";", в каждой паре x,y через запятую
--points-file   CSV-файл с двумя колонками x,y (без заголовка), по одной точке на строку
--degree        степень полинома (если не задана, по умолчанию включается --auto)
--auto          перебрать степени 1..min(5, N-1) и выбрать наименьшую, дающую
                R^2 не хуже --r2-threshold; если порог не достигнут — берётся
                степень с максимальным R^2 среди перебранных
--r2-threshold  порог R^2 для --auto (по умолчанию 0.99)
--var           имена переменных через запятую для подписи в LaTeX,
                например --var "\\beta_1,i_0" (по умолчанию "x,y")

Вывод: коэффициенты, R^2, диапазон применимости (по введённым x — экстраполяция
полинома за этот диапазон не гарантирована и почти всегда ошибочна для
дуг номограмм) и готовая строка LaTeX.
"""

import argparse
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("Нужен numpy: pip install numpy")


def parse_points(s):
    pts = []
    for chunk in s.strip().split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        x_str, y_str = chunk.split(",")
        pts.append((float(x_str), float(y_str)))
    return pts


def read_points_file(path):
    pts = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            x_str, y_str = line.split(",")
            pts.append((float(x_str), float(y_str)))
    return pts


def r_squared(y, y_fit):
    y = np.asarray(y, dtype=float)
    y_fit = np.asarray(y_fit, dtype=float)
    ss_res = np.sum((y - y_fit) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    if ss_tot == 0:
        return 1.0 if ss_res < 1e-12 else 0.0
    return 1 - ss_res / ss_tot


def fit_degree(xs, ys, degree):
    coeffs = np.polyfit(xs, ys, degree)
    y_fit = np.polyval(coeffs, xs)
    return coeffs, r_squared(ys, y_fit)


def format_number(value, sig=4):
    """Человеко- и LaTeX-читаемое представление числа, с переходом на
    научную нотацию для очень маленьких/больших коэффициентов (типично
    для старших степеней полинома)."""
    if value == 0:
        return "0"
    abs_v = abs(value)
    if abs_v < 1e-3 or abs_v >= 1e5:
        exponent = int(np.floor(np.log10(abs_v)))
        mantissa = value / (10 ** exponent)
        return f"{mantissa:.{max(sig - 1, 1)}g} \\times 10^{{{exponent}}}"
    return f"{value:.{sig}g}"


def to_latex(coeffs, var_x="x", var_y="y", sig=4):
    degree = len(coeffs) - 1
    max_abs = max((abs(c) for c in coeffs), default=1.0) or 1.0
    noise_floor = max_abs * 1e-9  # отсекаем числовой шум полифита, а не реальные малые члены
    pieces = []
    for i, c in enumerate(coeffs):
        power = degree - i
        if abs(c) < noise_floor:
            continue
        c_rounded = float(f"{c:.{sig}g}")
        if c_rounded == 0:
            continue
        abs_str = format_number(abs(c_rounded), sig=sig)
        if power == 0:
            term = abs_str
        elif power == 1:
            term = var_x if abs_str == "1" else f"{abs_str} {var_x}"
        else:
            term = f"{var_x}^{{{power}}}" if abs_str == "1" else f"{abs_str} {var_x}^{{{power}}}"
        sign = "-" if c_rounded < 0 else "+"
        pieces.append((sign, term))

    if not pieces:
        return f"{var_y} = 0"

    first_sign, first_term = pieces[0]
    body = ("-" if first_sign == "-" else "") + first_term
    for sign, term in pieces[1:]:
        body += f" {sign} {term}"
    return f"{var_y} = {body}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--points", default=None)
    parser.add_argument("--points-file", default=None)
    parser.add_argument("--degree", type=int, default=None)
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--r2-threshold", type=float, default=0.99)
    parser.add_argument("--var", default="x,y")
    args = parser.parse_args()

    if not args.points and not args.points_file:
        parser.error("Нужно указать --points или --points-file")

    pts = read_points_file(args.points_file) if args.points_file else parse_points(args.points)

    if len(pts) < 2:
        sys.exit("Нужно хотя бы 2 точки (а для разумной степени полинома — лучше 5-8)")

    pts = sorted(set(pts))
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    var_parts = (args.var.split(",") + ["x", "y"])[:2]
    var_x, var_y = var_parts[0].strip(), var_parts[1].strip()

    max_possible_degree = max(1, len(pts) - 1)

    if args.degree is not None:
        if args.degree > max_possible_degree:
            sys.exit(f"Степень {args.degree} слишком велика для {len(pts)} точек (максимум {max_possible_degree})")
        chosen, coeffs, r2 = args.degree, *fit_degree(xs, ys, args.degree)
    else:
        upper = min(5, max_possible_degree)
        best = None
        chosen = coeffs = r2 = None
        for d in range(1, upper + 1):
            c, r2_d = fit_degree(xs, ys, d)
            if best is None or r2_d > best[2]:
                best = (d, c, r2_d)
            if r2_d >= args.r2_threshold:
                chosen, coeffs, r2 = d, c, r2_d
                break
        if chosen is None:
            chosen, coeffs, r2 = best

    print(f"Точек: {len(pts)}, диапазон {var_x}: [{min(xs):.4g}, {max(xs):.4g}]")
    print(f"Степень полинома: {chosen}")
    print(f"R^2 = {r2:.5f}")
    print()
    print("Коэффициенты (от старшей степени к свободному члену):")
    print("  " + ", ".join(f"{c:.6g}" for c in coeffs))
    print()
    latex = to_latex(coeffs, var_x=var_x, var_y=var_y)
    print("LaTeX:")
    print(f"  $${latex}$$")
    print(f"  (справедливо для ${var_x} \\in [{min(xs):.4g},\\ {max(xs):.4g}]$; за пределами диапазона не использовать)")

    if r2 < 0.98:
        print(
            "\n⚠ R^2 заметно меньше 1 — проверь снятые точки: возможно, степень полинома "
            "не подходит к форме кривой, точки сняты неточно, или на графике несколько "
            "кривых перепутаны в одну выборку."
        )


if __name__ == "__main__":
    main()
