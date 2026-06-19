# Треугольники скоростей 1 ступени R=const

> Оцифровано из: `Mathcad треугольники скоростей` (9 страниц)

<!-- page 1 -->

## Исходные данные

$$i := 0 .. 14$$

$$R_{\text{cp.p}} := 0.5$$

## Расчет окружных скоростей

### Угловая скорость вращения

$$\omega_{1_i} := \frac{2 u_{k1_i}}{D_{k1\_\text{вывод}_i}}$$

$$\omega_{1_0} = 900.59$$

### Окружная скорость на входе

$$u_{\text{cp1}_i} := \omega_{1_i} \cdot \frac{D_{\text{cp1}_i}}{2}$$

$$u_{\text{вт1}_i} := \omega_{1_i} \cdot \frac{D_{\text{вт1}_i}}{2}$$

<!-- page 2 -->

### Окружная скорость на выходе

$$u_{k2_i} := u_{k1_i} \cdot \frac{D_{k2_i}}{D_{k1\_\text{вывод}_i}}$$

$$u_{\text{cp2}_i} := \omega_{1_i} \cdot \frac{D_{\text{cp2}_i}}{2}$$

$$u_{\text{вт2}_i} := \omega_{1_i} \cdot \frac{D_{\text{вт2}_i}}{2}$$

### На выходе из НА

$$u_{k3_i} := u_{k1_i} \cdot \frac{D_{k3_i}}{D_{k1\_\text{вывод}_i}}$$

$$u_{\text{cp3}_i} := \omega_{1_i} \cdot \frac{D_{\text{cp3}_i}}{2}$$

$$u_{\text{вт3}_i} := \omega_{1_i} \cdot \frac{D_{\text{вт3}_i}}{2}$$

## Втулочное сечение

### На входе в РК

$$c_{1\text{абт}_i} := \sqrt{\left(c_{1a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{вт1}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{1\text{ибт}_i} := u_{\text{вт1}_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{\text{вт1}_i}}$$

$$\alpha_{1\text{бт}_i} := \text{atan}\left(\frac{c_{1\text{абт}_i}}{c_{1\text{ибт}_i}}\right)$$

<!-- page 3 -->

$$c_{1\text{бт}_i} := \frac{c_{1\text{абт}_i}}{\sin\left(\alpha_{1\text{бт}_i}\right)}$$

$$w_{1\text{абт}_i} := c_{1\text{абт}_i}$$

$$\beta_{1\text{бт}_i} := \text{atan}\left(\frac{w_{1\text{абт}_i}}{u_{\text{вт1}_i} - c_{1\text{ибт}_i}}\right)$$

$$w_{1\text{бт}_i} := \frac{c_{1\text{абт}_i}}{\sin\left(\beta_{1\text{бт}_i}\right)}$$

$$w_{1\text{ибт}_i} := w_{1\text{бт}_i} \cdot \cos\left(\beta_{1\text{бт}_i}\right)$$

### На входе в РК (продолжение)

$$c_{2\text{абт}_i} := \sqrt{\left(c_{2a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{вт2}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{2\text{ибт}_i} := u_{\text{вт2}_i} \cdot \left(1 - R_{\text{cp.p}}\right) + \frac{H_{T_i}}{2 u_{\text{вт2}_i}}$$

$$\alpha_{2\text{бт}_i} := \text{atan}\left(\frac{c_{2\text{абт}_i}}{c_{2\text{ибт}_i}}\right)$$

$$c_{2\text{бт}_i} := \frac{c_{2\text{абт}_i}}{\sin\left(\alpha_{2\text{бт}_i}\right)}$$

$$w_{2\text{абт}_i} := c_{2\text{абт}_i}$$

$$\beta_{2\text{бт}_i} := \text{atan}\left(\frac{w_{2\text{абт}_i}}{u_{\text{вт2}_i} - c_{2\text{ибт}_i}}\right)$$

$$w_{2\text{бт}_i} := \frac{c_{2\text{абт}_i}}{\sin\left(\beta_{2\text{бт}_i}\right)}$$

<!-- page 4 -->

$$w_{2\text{ибт}_i} := w_{2\text{бт}_i} \cdot \cos\left(\beta_{2\text{бт}_i}\right)$$

### На выходе из НА

$$c_{3\text{абт}_i} := \sqrt{\left(c_{3a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{вт3}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{3\text{ибт}_i} := u_{\text{вт3}_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{\text{вт3}_i}}$$

$$\alpha_{3\text{бт}_i} := \text{atan}\left(\frac{c_{3\text{абт}_i}}{c_{3\text{ибт}_i}}\right)$$

$$c_{3\text{бт}_i} := \frac{c_{3\text{абт}_i}}{\sin\left(\alpha_{3\text{бт}_i}\right)}$$

## Периферийное сечение

### На входе в РК

$$c_{1\text{ак}_i} := \sqrt{\left(c_{1a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{k3_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{1\text{ук}_i} := u_{k3_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{k3_i}}$$

$$\alpha_{1\text{к}_i} := \text{atan}\left(\frac{c_{1\text{ак}_i}}{c_{1\text{ук}_i}}\right)$$

$$c_{1\text{к}_i} := \frac{c_{1\text{ак}_i}}{\sin\left(\alpha_{1\text{к}_i}\right)}$$

$$w_{1\text{ак}_i} := c_{1\text{ак}_i}$$

$$\beta_{1\text{к}_i} := \text{atan}\left(\frac{w_{1\text{ак}_i}}{u_{k3_i} - c_{1\text{ук}_i}}\right)$$

<!-- page 5 -->

$$w_{1\text{к}_i} := \frac{c_{1\text{ак}_i}}{\sin\left(\beta_{1\text{к}_i}\right)}$$

$$w_{1\text{ук}_i} := w_{1\text{к}_i} \cdot \cos\left(\beta_{1\text{к}_i}\right)$$

### На выходе из РК

$$c_{2\text{ак}_i} := \sqrt{\left(c_{2a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{k3_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{2\text{ук}_i} := u_{k3_i} \cdot \left(1 - R_{\text{cp.p}}\right) + \frac{H_{T_i}}{2 u_{k3_i}}$$

$$\alpha_{2\text{к}_i} := \text{atan}\left(\frac{c_{2\text{ак}_i}}{c_{2\text{ук}_i}}\right)$$

$$c_{2\text{к}_i} := \frac{c_{2\text{ак}_i}}{\sin\left(\alpha_{2\text{к}_i}\right)}$$

$$w_{2\text{ак}_i} := c_{2\text{ак}_i}$$

$$\beta_{2\text{к}_i} := \text{atan}\left(\frac{w_{2\text{ак}_i}}{u_{k3_i} - c_{2\text{ук}_i}}\right)$$

$$w_{2\text{к}_i} := \frac{c_{2\text{ак}_i}}{\sin\left(\beta_{2\text{к}_i}\right)}$$

$$w_{2\text{ук}_i} := w_{2\text{к}_i} \cdot \cos\left(\beta_{2\text{к}_i}\right)$$

### На выходе из НА

$$c_{3\text{ак}_i} := \sqrt{\left(c_{3a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{k3_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{3\text{ук}_i} := u_{k3_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{k3_i}}$$

<!-- page 6 -->

$$\alpha_{3\text{к}_i} := \text{atan}\left(\frac{c_{3\text{ак}_i}}{c_{3\text{ук}_i}}\right)$$

$$c_{3\text{к}_i} := \frac{c_{3\text{ак}_i}}{\sin\left(\alpha_{3\text{к}_i}\right)}$$

## Среднее сечение

### На входе в РК

$$c_{1a_i} := \sqrt{\left(c_{1a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{cp3}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{1u_i} := u_{\text{cp3}_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{\text{cp3}_i}}$$

$$\alpha_{1_i} := \text{atan}\left(\frac{c_{1a_i}}{c_{1u_i}}\right)$$

$$c_{1_i} := \frac{c_{1a_i}}{\sin\left(\alpha_{1_i}\right)}$$

$$w_{1a_i} := c_{1a_i}$$

$$\beta_{1_i} := \text{atan}\left(\frac{w_{1a_i}}{u_{\text{cp3}_i} - c_{1u_i}}\right)$$

$$w_{1_i} := \frac{c_{1a_i}}{\sin\left(\beta_{1_i}\right)}$$

$$w_{1u_i} := w_{1_i} \cdot \cos\left(\beta_{1_i}\right)$$

<!-- page 7 -->

### На входе в РК (продолжение)

$$c_{2a_i} := \sqrt{\left(c_{2a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{cp3}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{2u_i} := u_{\text{cp3}_i} \cdot \left(1 - R_{\text{cp.p}}\right) + \frac{H_{T_i}}{2 u_{\text{cp3}_i}}$$

$$\alpha_{2_i} := \text{atan}\left(\frac{c_{2a_i}}{c_{2u_i}}\right)$$

$$c_{2_i} := \frac{c_{2a_i}}{\sin\left(\alpha_{2_i}\right)}$$

$$w_{2a_i} := c_{2a_i}$$

$$\beta_{2_i} := \text{atan}\left(\frac{w_{2a_i}}{u_{\text{cp3}_i} - c_{2u_i}}\right)$$

$$w_{2_i} := \frac{c_{2a_i}}{\sin\left(\beta_{2_i}\right)}$$

$$w_{2u_i} := w_{2_i} \cdot \cos\left(\beta_{2_i}\right)$$

### На выходе из НА

$$c_{3a_i} := \sqrt{\left(c_{3a_i}\right)^2 - 2 \cdot \left(1 - R_{\text{cp.p}}\right)^2 \cdot \left[\left(u_{\text{cp3}_i}\right)^2 - \left(u_{\text{cp3}_i}\right)^2\right]}$$

$$c_{3u_i} := u_{\text{cp3}_i} \cdot \left(1 - R_{\text{cp.p}}\right) - \frac{H_{T_i}}{2 u_{\text{cp3}_i}}$$

$$\alpha_{3_i} := \text{atan}\left(\frac{c_{3a_i}}{c_{3u_i}}\right)$$

$$c_{3_i} := \frac{c_{3a_i}}{\sin\left(\alpha_{3_i}\right)}$$

<!-- page 8 -->

## Результаты для i=0

### Вход в РК

| Параметр | Периферия | Среднее | Втулка |
|----------|-----------|---------|--------|
| $c_{1\text{ак}}$ | 124.084 | 182.097 | 228.159 |
| $c_{1\text{ук}}$ | 134.384 | 98.61 | 43.457 |
| $\alpha_1$ / deg | 42.718 | 61.563 | 79.216 |
| $\beta_1$ / deg | 31.3 | 44.933 | 55.023 |
| $c_1$ | 182.91 | 207.082 | 232.261 |
| $w_{1\text{ак}}$ | 124.084 | 182.097 | 228.159 |
| $w_{1\text{ук}}$ | 204.086 | 182.526 | 159.625 |
| $w_1$ | 238.847 | 257.827 | 278.454 |
| $u_{k3}$ | 338.47 | — | — |
| $u_{\text{cp3}}$ | — | 281.135 | — |
| $u_{\text{вт3}}$ | — | — | 203.082 |

### Выход из РК

| Параметр | Периферия | Среднее | Втулка |
|----------|-----------|---------|--------|
| $c_{2\text{ак}}$ | 123.338 | 181.589 | 227.754 |
| $c_{2\text{ук}}$ | 204.086 | 182.526 | 159.625 |
| $\alpha_2$ / deg | 31.146 | 44.853 | 54.975 |
| $\beta_2$ / deg | 42.546 | 61.496 | 79.198 |
| $c_2$ | 238.46 | 257.469 | 278.123 |
| $w_{2\text{ак}}$ | 123.338 | 181.589 | 227.754 |
| $w_{2\text{ук}}$ | 134.384 | 98.61 | 43.457 |
| $w_2$ | 182.404 | 206.636 | 231.863 |
| $u_{k3}$ | 338.47 | — | — |
| $u_{\text{cp3}}$ | — | 281.135 | — |
| $u_{\text{вт3}}$ | — | — | 203.082 |

<!-- page 9 -->

### Выход из НА

| Параметр | Периферия | Среднее | Втулка |
|----------|-----------|---------|--------|
| $c_{3\text{ак}}$ | 122.589 | 181.081 | 227.35 |
| $c_{3\text{ук}}$ | 134.384 | 97.383 | 43.457 |
| $\alpha_3$ / deg | 42.372 | 61.429 | 79.179 |
| $c_3$ | 181.899 | 205.606 | 223.644 |
