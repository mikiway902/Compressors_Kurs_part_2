# Метод лопатки — Расчёт профилирования

> Оцифровано из: `Mathcad_лопатки расчет` (37 страниц, Mathcad-документ)

---

<!-- page 1 -->

# Профилирование

## Периферийное сечение

$$\beta_{1\text{к}}^{\text{T}} = \begin{bmatrix} 18.329 & 21.449 & 22.839 & 23.889 & 24.566 & 24.98 & 25.204 & \ldots \end{bmatrix} \text{ deg}$$

$$\beta_{2\text{к}}^{\text{T}} = \begin{bmatrix} 26.367 & 33.842 & 37.645 & 39.618 & 40.963 & 41.881 & 42.494 & \ldots \end{bmatrix} \text{ deg}$$

$$\alpha_{2\text{к}}^{\text{T}} = \begin{bmatrix} 16.334 & 20.472 & 22.111 & 23.285 & 24.043 & 24.512 & 24.769 & \ldots \end{bmatrix} \text{ deg}$$

$$\alpha_{3\text{к}}^{\text{T}} = \begin{bmatrix} 22.92 & 32.373 & 36.591 & 38.772 & 40.247 & 41.249 & 41.913 & \ldots \end{bmatrix} \text{ deg}$$

$$\varepsilon_{\text{РКк}}^{\text{T}} = \begin{bmatrix} 8.039 & 12.393 & 14.806 & 15.729 & 16.397 & 16.901 & 17.291 & \ldots \end{bmatrix} \text{ deg}$$

$$\varepsilon_{\text{НАк}}^{\text{T}} = \begin{bmatrix} 6.586 & 11.901 & 14.479 & 15.488 & 16.204 & 16.737 & 17.143 & \ldots \end{bmatrix} \text{ deg}$$

---

<!-- page 2 -->

## Шаги и густоты

### Шаг лопаток

$$t_{\text{РК.к}_i} := \frac{\pi \cdot D_{\text{k1\_вывод}_i}}{Z_{\text{РК}_i}}$$

$$t_{\text{НА.к}_i} := \frac{\pi \cdot D_{\text{k2\_вывод}_i}}{Z_{\text{НА}_i}}$$

$$t_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 0.1289 & 0.1153 & 0.0755 & 0.0562 & 0.0466 & 0.0487 & 0.0398 & \ldots \end{bmatrix}$$

$$t_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 0.0782 & 0.0913 & 0.0644 & 0.0498 & 0.0421 & 0.0365 & 0.0304 & \ldots \end{bmatrix}$$

### Густота лопаток

$$b\_t_{\text{РК.к}_i} := \frac{1 \cdot b_{\text{РК}_i}}{t_{\text{РК.к}_i}}$$

$$b\_t_{\text{НА.к}_i} := \frac{1 \cdot b_{\text{НА}_i}}{t_{\text{НА.к}_i}}$$

$$b\_t_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 0.9467 & 0.8688 & 0.9681 & 1.0548 & 1.117 & 0.9597 & 1.0122 & \ldots \end{bmatrix}$$

$$b\_t_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 1.0727 & 0.9402 & 1.0248 & 1.0904 & 1.1424 & 1.1913 & 1.2409 & \ldots \end{bmatrix}$$

---

<!-- page 3 -->

## Углы атаки

$$i_{\text{РК.к}_i} := 2.5 \left(b\_t_{\text{РК.к}_i} - 1\right)$$

$$i_{\text{НА.к}_i} := 2.5 \left(b\_t_{\text{НА.к}_i} - 2\right)$$

$$i_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} -0.1332 & -0.328 & -0.0799 & 0.137 & 0.2926 & -0.1008 & \ldots \end{bmatrix}$$

$$i_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} -2.3181 & -2.6495 & -2.4381 & -2.2741 & -2.1441 & -2.0218 & \ldots \end{bmatrix}$$

---

<!-- page 4 -->

## Угол изгиба средней линии

Форма средней линии — дуга окружности.

$$\bar{x}_f := 0.5$$

Коэффициент, учитывающий форму средней линии профиля:

$$m_{\text{РК.к}_i} := 0.23 \cdot \left(2 \cdot \bar{x}_f\right)^2 + 0.18 - 0.002 \cdot \frac{\beta_{2\text{к}_i}}{\text{deg}}$$

$$m_{\text{НА.к}_i} := 0.23 \cdot \left(2 \cdot \bar{x}_f\right)^2 + 0.18 - 0.002 \cdot \frac{\alpha_{3\text{к}_i}}{\text{deg}}$$

$$m_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 0.3573 & 0.3423 & 0.3347 & 0.3308 & 0.3281 & 0.3262 & 0.325 & \ldots \end{bmatrix}$$

$$m_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 0.3642 & 0.3453 & 0.3368 & 0.3325 & 0.3295 & 0.3275 & 0.3262 & \ldots \end{bmatrix}$$

### Угол изгиба средней линии

$$\theta_{\text{РК.к}_i} := \frac{\dfrac{\varepsilon_{\text{РКк}_i}}{\text{deg}} - i_{\text{РК.к}_i}}{1 - m_{\text{РК.к}_i} \cdot \sqrt{\dfrac{1}{b\_t_{\text{РК.к}_i}}}} \text{ градус}$$

$$\theta_{\text{НА.к}_i} := \frac{\dfrac{\varepsilon_{\text{НАк}_i}}{\text{deg}} - i_{\text{НА.к}_i}}{1 - m_{\text{НА.к}_i} \cdot \sqrt{\dfrac{1}{b\_t_{\text{НА.к}_i}}}} \text{ градус}$$

$$\theta_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 12.913 & 20.104 & 22.561 & 23 & 23.354 & 25.491 & 25.497 & \ldots \end{bmatrix}$$

$$\theta_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 13.732 & 22.596 & 25.353 & 26.058 & 26.526 & 26.801 & 26.925 & \ldots \end{bmatrix}$$

---

<!-- page 5 -->

## Углы отставания

$$\delta_{\text{РК.к}_i} := m_{\text{РК.к}_i} \cdot \theta_{\text{РК.к}_i} \cdot \sqrt{\frac{1}{b\_t_{\text{РК.к}_i}}} \text{ градус}$$

$$\delta_{\text{НА.к}_i} := m_{\text{НА.к}_i} \cdot \theta_{\text{НА.к}_i} \cdot \sqrt{\frac{1}{b\_t_{\text{НА.к}_i}}} \text{ градус}$$

$$\delta_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 4.741 & 7.383 & 7.675 & 7.407 & 7.249 & 8.489 & 8.237 & 7.912 & \ldots \end{bmatrix}$$

$$\delta_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 4.828 & 8.045 & 8.436 & 8.296 & 8.178 & 8.042 & 7.884 & 7.673 & \ldots \end{bmatrix}$$

## Углы установки

$$\upsilon_{\text{РК.к}_i} := 0.5 \cdot \theta_{\text{РК.к}_i} + \frac{\beta_{1\text{к}_i}}{\text{deg}} + i_{\text{РК.к}_i} \text{ градус}$$

$$\upsilon_{\text{НА.к}_i} := 0.5 \cdot \theta_{\text{НА.к}_i} + \frac{\alpha_{2\text{к}_i}}{\text{deg}} + i_{\text{НА.к}_i} \text{ градус}$$

$$\upsilon_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 24.652 & 31.173 & 34.04 & 35.526 & 36.535 & 37.625 & 37.983 & \ldots \end{bmatrix}$$

$$\upsilon_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 20.882 & 29.12 & 32.35 & 34.04 & 35.162 & 35.89 & 36.334 & \ldots \end{bmatrix}$$

## Радиусы дуг средних линий

$$R_{\text{сл.РК.к}_i} := \frac{1.2 \cdot b_{\text{РК}_i}}{2 \cdot \sin\!\left(\dfrac{\theta_{\text{РК.к}_i} \cdot \text{deg}}{2}\right)} = \ldots \text{ м}$$

$$R_{\text{сл.НА.к}_i} := \frac{0.9 \cdot b_{\text{НА}_i}}{2 \cdot \sin\!\left(\dfrac{\theta_{\text{НА.к}_i} \cdot \text{deg}}{2}\right)} = \ldots \text{ м}$$

$$R_{\text{сл.РК.к}}^{\text{T}} = \begin{bmatrix} 0.651 & 0.3443 & 0.2243 & 0.1783 & 0.1544 & 0.1271 & 0.1096 & \ldots \end{bmatrix}$$

$$R_{\text{сл.НА.к}}^{\text{T}} = \begin{bmatrix} 0.3159 & 0.1971 & 0.1354 & 0.1084 & 0.0944 & 0.0845 & 0.073 & \ldots \end{bmatrix}$$

---

<!-- page 6 -->

## Втулочное сечение

$$\beta_{1\text{вт}}^{\text{T}} = \begin{bmatrix} 49.541 & 51.493 & 48.884 & 46.779 & 44.813 & 43.027 & 41.427 & \ldots \end{bmatrix} \text{ deg}$$

$$\beta_{2\text{вт}}^{\text{T}} = \begin{bmatrix} 81.782 & -87.68 & 84.321 & 78.901 & 74.912 & 71.763 & 69.189 & \ldots \end{bmatrix} \text{ deg}$$

$$\alpha_{2\text{вт}}^{\text{T}} = \begin{bmatrix} 49.169 & 50.785 & 47.659 & 45.596 & 43.727 & 42.048 & 40.544 & \ldots \end{bmatrix} \text{ deg}$$

$$\alpha_{3\text{вт}}^{\text{T}} = \begin{bmatrix} 81.674 & -79.818 & 87.886 & 81.367 & 76.794 & 73.248 & \ldots \end{bmatrix} \text{ deg}$$

$$\varepsilon_{\text{РКвт}}^{\text{T}} = \begin{bmatrix} 32.242 & -139.173 & 35.437 & 32.122 & 30.099 & \ldots \end{bmatrix} \text{ deg}$$

$$\varepsilon_{\text{НАвт}}^{\text{T}} = \begin{bmatrix} 32.506 & -130.603 & 40.227 & 35.77 & 33.067 & \ldots \end{bmatrix} \text{ deg}$$

### Шаги и густоты (втулочное сечение)

$$t_{\text{РК.вт}_i} := \frac{\pi \cdot D_{\text{вт1}_i}}{Z_{\text{РК}_i}}$$

$$t_{\text{НА.вт}_i} := \frac{\pi \cdot D_{\text{вт2}_i}}{Z_{\text{НА}_i}}$$

$$t_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 0.0773 & 0.049 & 0.0439 & 0.0371 & 0.0334 & 0.0369 & 0.0315 & \ldots \end{bmatrix}$$

$$t_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 0.0469 & 0.0463 & 0.04 & 0.0343 & 0.0311 & 0.0283 & 0.0245 & \ldots \end{bmatrix}$$

---

<!-- page 7 -->

$$b\_t_{\text{РК.вт}_i} := \frac{0.9 \cdot b_{\text{РК}_i}}{t_{\text{РК.вт}_i}}$$

$$b\_t_{\text{НА.вт}_i} := \frac{1 \cdot b_{\text{НА}_i}}{t_{\text{НА.вт}_i}}$$

$$b\_t_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 1.42 & 1.838 & 1.501 & 1.438 & 1.404 & 1.138 & 1.15 & 1.185 & \ldots \end{bmatrix}$$

$$b\_t_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 1.788 & 1.852 & 1.65 & 1.583 & 1.548 & 1.536 & 1.541 & 1.568 & \ldots \end{bmatrix}$$

### Углы атаки (втулочное сечение)

$$i_{\text{РК.вт}_i} := 2.5 \left(b\_t_{\text{РК.вт}_i} - 1\right)$$

$$i_{\text{НА.вт}_i} := 2.5 \left(b\_t_{\text{НА.вт}_i} - 2\right)$$

$$i_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 1.0502 & 2.0953 & 1.252 & 1.0951 & 1.009 & 0.3456 & 0.3759 & \ldots \end{bmatrix}$$

$$i_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} -0.5302 & -0.3704 & -0.8762 & -1.0413 & -1.1288 & -1.1594 & \ldots \end{bmatrix}$$

## Угол изгиба средней линии (втулочное сечение)

Форма средней линии — дуга окружности.

$$\bar{x}_f := 0.5$$

$$m_{\text{РК.вт}_i} := 0.23 \cdot \left(2 \cdot \bar{x}_f\right)^2 + 0.18 - 0.002 \cdot \frac{\beta_{2\text{вт}_i}}{\text{deg}}$$

$$m_{\text{НА.вт}_i} := 0.23 \cdot \left(2 \cdot \bar{x}_f\right)^2 + 0.18 - 0.002 \cdot \frac{\alpha_{3\text{вт}_i}}{\text{deg}}$$

$$m_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 0.2464 & 0.5854 & 0.2414 & 0.2522 & 0.2602 & 0.2665 & 0.2716 & \ldots \end{bmatrix}$$

$$m_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 0.2467 & 0.5696 & 0.2342 & 0.2473 & 0.2564 & 0.2635 & 0.2692 & \ldots \end{bmatrix}$$

---

<!-- page 8 -->

$$\theta_{\text{РК.вт}_i} := \frac{\dfrac{\varepsilon_{\text{РКвт}_i}}{\text{deg}} - i_{\text{РК.вт}_i}}{1 - m_{\text{РК.вт}_i} \cdot \sqrt{\dfrac{1}{b\_t_{\text{РК.вт}_i}}}} \text{ градус}$$

$$\theta_{\text{НА.вт}_i} := \frac{\dfrac{\varepsilon_{\text{НАвт}_i}}{\text{deg}} - i_{\text{НА.вт}_i}}{1 - m_{\text{НА.вт}_i} \cdot \sqrt{\dfrac{1}{b\_t_{\text{НА.вт}_i}}}} \text{ градус}$$

$$\theta_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 39.323 & -248.604 & 42.573 & 39.29 & 37.276 & \ldots \end{bmatrix}$$

$$\theta_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 40.508 & -223.997 & 50.271 & 45.814 & 43.071 & \ldots \end{bmatrix}$$

### Углы отставания (втулочное сечение)

$$\delta_{\text{РК.вт}_i} := m_{\text{РК.вт}_i} \cdot \theta_{\text{РК.вт}_i} \cdot \sqrt{\frac{1}{b\_t_{\text{РК.вт}_i}}} \text{ градус}$$

$$\delta_{\text{НА.вт}_i} := m_{\text{НА.вт}_i} \cdot \theta_{\text{НА.вт}_i} \cdot \sqrt{\frac{1}{b\_t_{\text{НА.вт}_i}}} \text{ градус}$$

$$\delta_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 8.132 & -107.336 & 8.388 & 8.263 & 8.186 & \ldots \end{bmatrix}$$

$$\delta_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 7.472 & -93.764 & 9.168 & 9.002 & 8.875 & 8.737 & \ldots \end{bmatrix}$$

### Углы установки (втулочное сечение)

$$\upsilon_{\text{РК.вт}_i} := 0.5 \cdot \theta_{\text{РК.вт}_i} + \frac{\beta_{1\text{вт}_i}}{\text{deg}} + i_{\text{РК.вт}_i} \text{ градус}$$

$$\upsilon_{\text{НА.вт}_i} := 0.5 \cdot \theta_{\text{НА.вт}_i} + \frac{\alpha_{2\text{вт}_i}}{\text{deg}} + i_{\text{НА.вт}_i} \text{ градус}$$

---

<!-- page 9 -->

$$\upsilon_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 70.253 & -70.714 & 71.422 & 67.519 & 64.46 & 62.294 & \ldots \end{bmatrix}$$

$$\upsilon_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 68.892 & -61.583 & 71.919 & 67.462 & 64.134 & 61.437 & \ldots \end{bmatrix}$$

### Радиусы дуг средних линий (втулочное сечение)

$$R_{\text{сл.РК.вт}_i} := \frac{0.9 \cdot b_{\text{РК}_i}}{2 \cdot \sin\!\left(\dfrac{\theta_{\text{РК.вт}_i} \cdot \text{deg}}{2}\right)} \text{ м}$$

$$R_{\text{сл.НА.вт}_i} := \frac{1.2 \cdot b_{\text{НА}_i}}{2 \cdot \sin\!\left(\dfrac{\theta_{\text{НА.вт}_i} \cdot \text{deg}}{2}\right)} \text{ м}$$

$$R_{\text{сл.РК.вт}}^{\text{T}} = \begin{bmatrix} 0.1632 & -0.0546 & 0.0906 & 0.0793 & 0.0733 & 0.0648 & \ldots \end{bmatrix}$$

$$R_{\text{сл.НА.вт}}^{\text{T}} = \begin{bmatrix} 0.1455 & -0.0555 & 0.0933 & 0.0837 & 0.0787 & 0.0744 & \ldots \end{bmatrix}$$

### Сводные таблицы углов изгиба

$$\theta_{\text{РК.вт}}^{\text{T}} = \begin{bmatrix} 39.32 & -248.6 & 42.57 & 39.29 & 37.28 & 37.84 & 36.67 & \ldots \end{bmatrix}$$

$$\theta_{\text{НА.вт}}^{\text{T}} = \begin{bmatrix} 40.51 & -224 & 50.27 & 45.81 & 43.07 & 41.1 & 39.57 & 38.28 & \ldots \end{bmatrix}$$

$$\theta_{\text{РК.ср}}^{\text{T}} = \begin{bmatrix} 34.14 & 30.73 & 32.03 & 31.01 & 30.3 & 31.69 & 31.11 & 30.45 & \ldots \end{bmatrix}$$

$$\theta_{\text{НА.ср}}^{\text{T}} = \begin{bmatrix} 38.64 & 35.51 & 35.42 & 34.56 & 33.89 & 33.34 & 32.83 & 32.03 & \ldots \end{bmatrix}$$

$$\theta_{\text{РК.к}}^{\text{T}} = \begin{bmatrix} 12.91 & 20.1 & 22.56 & 23 & 23.35 & 25.49 & 25.5 & 25.33 & \ldots \end{bmatrix}$$

$$\theta_{\text{НА.к}}^{\text{T}} = \begin{bmatrix} 13.73 & 22.6 & 25.35 & 26.06 & 26.53 & 26.8 & 26.93 & 26.9 & \ldots \end{bmatrix}$$

---

<!-- page 10 -->

## Коэффициенты напора и потерь

### Средн РК

$$K_{\text{рк}} := \frac{c_{2\text{а}_0}}{c_{1\text{а}_0}} = 0.981$$

$$D_{\text{рк}} := \left(1 - K_{\text{рк}} \cdot \frac{\sin\!\left(\beta_{1_0}\right)}{\sin\!\left(\beta_{2_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\beta_{1_0}\right)} - K_{\text{рк}} \cdot \frac{1}{\tan\!\left(\beta_{2_0}\right)}\right) \cdot \frac{\sin\!\left(\beta_{1_0}\right)}{2 \cdot b\_t_{\text{РК.ср}_0}} = 0.476$$

### Пер РК

$$K_{\text{ркк}} := \frac{c_{2\text{ак}_0}}{c_{1\text{ак}_0}} = 0.885$$

$$D_{\text{ркк}} := \left(1 - K_{\text{ркк}} \cdot \frac{\sin\!\left(\beta_{1\text{к}_0}\right)}{\sin\!\left(\beta_{2\text{к}_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\beta_{1\text{к}_0}\right)} - K_{\text{ркк}} \cdot \frac{1}{\tan\!\left(\beta_{2\text{к}_0}\right)}\right) \cdot \frac{\sin\!\left(\beta_{1\text{к}_0}\right)}{2 \cdot b\_t_{\text{РК.к}_0}} = 0.579$$

### Втулка РК

$$K_{\text{рквт}} := \frac{c_{2\text{авт}_0}}{c_{1\text{авт}_0}} = 0.987$$

$$D_{\text{рквт}} := \left(1 - K_{\text{рквт}} \cdot \frac{\sin\!\left(\beta_{1\text{вт}_0}\right)}{\sin\!\left(\beta_{2\text{вт}_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\beta_{1\text{вт}_0}\right)} - K_{\text{рквт}} \cdot \frac{1}{\tan\!\left(\beta_{2\text{вт}_0}\right)}\right) \cdot \frac{\sin\!\left(\beta_{1\text{вт}_0}\right)}{2 \cdot b\_t_{\text{РК.вт}_0}} = 0.432$$

---

<!-- page 11 -->

### Средн НА

$$K_{\text{на}} := \frac{c_{3\text{а}_0}}{c_{2\text{а}_0}} = 0.98$$

$$D_{\text{рк}} := \left(1 - K_{\text{на}} \cdot \frac{\sin\!\left(\alpha_{2_0}\right)}{\sin\!\left(\alpha_{3_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\alpha_{2_0}\right)} - K_{\text{на}} \cdot \frac{1}{\tan\!\left(\alpha_{3_0}\right)}\right) \cdot \frac{\sin\!\left(\alpha_{2_0}\right)}{2 \cdot b\_t_{\text{НА.ср}_0}} = 0.455$$

### Пер НА

$$K_{\text{нак}} := \frac{c_{3\text{ак}_0}}{c_{2\text{ак}_0}} = 0.853$$

$$D_{\text{ркк}} := \left(1 - K_{\text{нак}} \cdot \frac{\sin\!\left(\alpha_{2\text{к}_0}\right)}{\sin\!\left(\alpha_{3\text{к}_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\alpha_{2\text{к}_0}\right)} - K_{\text{на}} \cdot \frac{1}{\tan\!\left(\alpha_{3\text{к}_0}\right)}\right) \cdot \frac{\sin\!\left(\alpha_{2\text{к}_0}\right)}{2 \cdot b\_t_{\text{НА.к}_0}} = 0.527$$

### Втулка НА

$$K_{\text{навт}} := \frac{c_{3\text{авт}_0}}{c_{2\text{авт}_0}} = 0.987$$

$$D_{\text{рквт}} := \left(1 - K_{\text{навт}} \cdot \frac{\sin\!\left(\alpha_{2\text{вт}_0}\right)}{\sin\!\left(\alpha_{3\text{вт}_0}\right)}\right) + \left(\frac{1}{\tan\!\left(\alpha_{2\text{вт}_0}\right)} - K_{\text{на}} \cdot \frac{1}{\tan\!\left(\alpha_{3\text{вт}_0}\right)}\right) \cdot \frac{\sin\!\left(\alpha_{2\text{вт}_0}\right)}{2 \cdot b\_t_{\text{НА.вт}_0}} = 0.398$$

---

<!-- page 12 -->

# Построение профилей решеток

## Построение профиля А40

### Сверхзвуковой профиль

$$i := 0$$

Запишем относительные координаты исходного сверхзвукового профиля:

$$x0\_b := \text{stack}(1, 1.5, 2.5, 5, 7.5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 95, 100)$$

$$y0\_b := \text{stack}(1.14, 1.43, 1.85, 2.55, 3.09, 3.525, 4.16, 4.55, 4.788, 4.927, 4.936, 5, 4.858, 4.44, \ldots)$$

$$x\_b := \frac{x0\_b}{100}$$

$$Sc := \text{lspline}\!\left(\frac{x0\_b}{100}, \frac{y0\_b}{100}\right)$$

$$y'\_b(x\_b) := \text{interp}\!\left(Sc, \frac{x0\_b}{100}, \frac{y0\_b}{100}, x\_b\right)$$

$$y\_b(x\_b, c') := y'\_b(x\_b) \cdot \frac{c'}{10}$$

### Уравнение средней линии в относительных координатах

$$y_{\text{ср}\_b}(x\_b, \theta) := \sqrt{\left(2 \cdot \sin(0.5 \cdot \theta \cdot \text{deg})\right)^{-2} - (x\_b - 0.5)^2} - \frac{0.5}{\tan[0.5 \cdot (\theta \cdot \text{deg})]}$$

---

<!-- page 13 -->

### Уравнение спинки и корыта в относительных координатах

$$c' := 10 \qquad \theta := 45$$

$$y\_b_{\text{спинки}}(x\_b, c', \theta) := y_{\text{ср}\_b}(x\_b, \theta) + y\_b(x\_b, c')$$

$$y\_b_{\text{корыта}(x\_b, c', \theta)} := y_{\text{ср}\_b}(x\_b, \theta) - y\_b(x\_b, c')$$

---

<!-- page 14 -->

## Среднее сечение РК

Относительная толщина профиля:

$$c' := 9$$

$$\theta := \theta_{\text{РК.ср}_i} = 34.137$$

$$b := b_{\text{РК}_i} = 0.122$$

$$\upsilon := 90 - \upsilon_{\text{РК.ср}_i} = 30.467 \qquad \upsilon_{\text{РК.ср}_i} = 59.533$$

$$r := \frac{D_{\text{ср1}_i} \cdot 1000}{2} = 287.513 \qquad D_{\text{ср1}_i} = 0.575$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

---

<!-- page 15 -->

### Нахождение центров масс

$$A_{\text{РКср}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 978.452$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 6864.149$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 53960.995$$

$$x_c := \frac{S_y}{A_{\text{РКср}}}} = 55.149$$

$$y_c := \frac{S_x}{A_{\text{РКср}}}} = 7.015$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.604$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.549$$

---

<!-- page 16 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

---

<!-- page 17 -->

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 18 -->

## Периферийное сечение РК

Относительная толщина профиля:

$$c' := 6$$

$$\theta := \theta_{\text{РК.к}_i} = 12.913$$

$$b := \left(1.2 \cdot b_{\text{РК}}\right)_i = 0.1464$$

$$\upsilon := 90 - \upsilon_{\text{РК.к}_i} = 65.348 \qquad \upsilon_{\text{РК.к}_i} = 24.652$$

$$r := \frac{D_{\text{k1\_вывод}_i} \cdot 1000}{2} = 348.66 \qquad D_{\text{k1\_вывод}_i} = 0.697$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

---

<!-- page 19 -->

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

### Нахождение центров масс

$$A_{\text{РКк}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 939.314$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 2963.032$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 62163.066$$

$$x_c := \frac{S_y}{A_{\text{РКк}}} = 66.179$$

$$y_c := \frac{S_x}{A_{\text{РКк}}} = 3.154$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.483$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.439$$

---

<!-- page 20 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

---

<!-- page 21 -->

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 22 -->

## Втулочное сечение РК

Относительная толщина профиля:

$$c' := 12$$

$$\theta := \theta_{\text{РК.вт}_i} = 39.323$$

$$b := 0.9 \cdot b_{\text{РК}_i} = 0.1098$$

$$\upsilon := 90 - \upsilon_{\text{РК.вт}_i} = 19.747 \qquad \upsilon_{\text{РК.вт}_i} = 70.253$$

$$r := \frac{D_{\text{вт1}_i} \cdot 1000}{2} = 209.196 \qquad D_{\text{вт1}_i} = 0.418$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

---

<!-- page 23 -->

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

### Нахождение центров масс

$$A_{\text{РКвт}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 1056.728$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 7713.577$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 52450.087$$

$$x_c := \frac{S_y}{A_{\text{РКвт}}} = 49.634$$

$$y_c := \frac{S_x}{A_{\text{РКвт}}} = 7.299$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.725$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.659$$

---

<!-- page 24 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 25 -->

## Построение профиля А40 (продолжение)

$$c' := 10$$

Запишем относительные координаты исходного профиля А40:

$$x0\_b := \text{stack}(1, 1.5, 2.5, 5, 7.5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 95, 100)$$

$$y0\_b := \text{stack}(1.14, 1.43, 1.85, 2.55, 3.09, 3.525, 4.16, 4.55, 4.788, 4.927, 4.936, 5, 4.858, 4.44, \ldots)$$

$$x\_b := \frac{x0\_b}{100}$$

$$Sc := \text{lspline}\!\left(\frac{x0\_b}{100}, \frac{y0\_b}{100}\right)$$

$$y'\_b(x\_b) := \text{interp}\!\left(Sc, \frac{x0\_b}{100}, \frac{y0\_b}{100}, x\_b\right)$$

$$y\_b(x\_b, c') := y'\_b(x\_b) \cdot \frac{c'}{10}$$

### Уравнение средней линии в относительных координатах

$$y_{\text{ср}\_b}(x\_b, \theta) := \sqrt{\left(2 \cdot \sin(0.5 \cdot \theta \cdot \text{deg})\right)^{-2} - (x\_b - 0.5)^2} - \frac{0.5}{\tan[0.5 \cdot (\theta \cdot \text{deg})]}$$

### Уравнение спинки и корыта в относительных координатах

$$c' := 10 \qquad \theta := 45$$

$$y\_b_{\text{спинки}}(x\_b, c', \theta) := y_{\text{ср}\_b}(x\_b, \theta) + y\_b(x\_b, c')$$

$$y\_b_{\text{корыта}(x\_b, c', \theta)} := y_{\text{ср}\_b}(x\_b, \theta) - y\_b(x\_b, c')$$

---

<!-- page 26 -->

## Среднее сечение НА

Относительная толщина профиля:

$$c' := 9$$

$$\theta := \theta_{\text{НА.ср}_i} = 38.642$$

$$b := b_{\text{НА}_i} = 0.0839$$

$$\upsilon := 90 - \upsilon_{\text{НА.ср}_i} = 30.769 \qquad \upsilon_{\text{НА.ср}_i} = 59.231$$

$$r := \frac{D_{\text{ср2}_i} \cdot 1000}{2} = 277.716 \qquad D_{\text{ср2}_i} = 0.555$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

---

<!-- page 27 -->

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

### Нахождение центров масс

$$A_{\text{НАср}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 463.083$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 2537.777$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 17569.471$$

$$x_c := \frac{S_y}{A_{\text{НАср}}} = 37.94$$

$$y_c := \frac{S_x}{A_{\text{НАср}}} = 5.48$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.415$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.378$$

---

<!-- page 28 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 29 -->

## Периферийное сечение НА

Относительная толщина профиля:

$$c' := 12$$

$$\theta := \theta_{\text{НА.к}_i} = 13.732$$

$$b := \left(0.9 \cdot b_{\text{НА}}\right)_i = 0.07554 \qquad \upsilon_{\text{НА.к}_i} = 20.882$$

$$\upsilon := 90 - \upsilon_{\text{НА.к}_i} = 69.118$$

$$r := \frac{D_{\text{k2}_i} \cdot 1000}{2} = 348.66 \qquad D_{\text{k2}_i} = 0.697$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

---

<!-- page 30 -->

### Нахождение центров масс

$$A_{\text{НАк}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 500.13$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 865.812$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 17077.526$$

$$x_c := \frac{S_y}{A_{\text{НАк}}} = 34.146$$

$$y_c := \frac{S_x}{A_{\text{НАк}}} = 1.731$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.499$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.453$$

---

<!-- page 31 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

---

<!-- page 32 -->

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 33 -->

## Втулочное сечение НА

Относительная толщина профиля:

$$c' := 6$$

$$\theta := \theta_{\text{НА.вт}_i} = 40.508$$

$$b := 1.2 \cdot b_{\text{НА}_i} = 0.10072 \qquad \upsilon_{\text{НА.вт}_i} = 68.892$$

$$\upsilon := 90 - \upsilon_{\text{НА.вт}_i} = 21.108$$

$$r := \frac{D_{\text{вт2}_i} \cdot 1000}{2} = 209.196 \qquad D_{\text{вт2}_i} = 0.418$$

### Абсолютные координаты профиля

$$X := x\_b \cdot b \cdot 1000$$

$$Y_{\text{спинки}} := y\_b_{\text{спинки}}(x\_b, c', \theta) \cdot b \cdot 1000$$

$$Y_{\text{корыта}} := y\_b_{\text{корыта}(x\_b, c', \theta)} \cdot b \cdot 1000$$

$$Y_{\text{ср.линии}} := y_{\text{ср}\_b}(x\_b, \theta) \cdot b \cdot 1000$$

---

<!-- page 34 -->

$$Sc := \text{lspline}(X, Y_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X, Y_{\text{спинки}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{корыта}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X, Y_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X, Y_{\text{ср.линии}}, x) & \text{if } \min(X) \le x \le \max(X) \\ \text{NaN} & \text{otherwise} \end{cases}$$

### Нахождение центров масс

$$A_{\text{НАвт}} := \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 444.56$$

$$S_x := 0.5 \cdot \int_{\min(X)}^{\max(X)} \left(y_{\text{спинки}}(x)^2 - y_{\text{корыта}(x)}^2\right) dx = 3069.075$$

$$S_y := \int_{\min(X)}^{\max(X)} x \cdot \left(y_{\text{спинки}}(x) - y_{\text{корыта}(x)}\right) dx = 20240.031$$

$$x_c := \frac{S_y}{A_{\text{НАвт}}} = 45.528$$

$$y_c := \frac{S_x}{A_{\text{НАвт}}} = 6.904$$

### Радиусы входной и выходной кромок

$$r_{\text{вх}} := 0.055 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.332$$

$$r_{\text{вых}} := 0.05 \cdot \frac{c'}{100} \cdot b \cdot 1000 = 0.302$$

---

<!-- page 35 -->

### Поворот профиля вокруг начала координат

$$XX'_{\text{спинки}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{спинки}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{спинки}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{спинки}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$XX'_{\text{корыта}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{корыта}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$YY'_{\text{корыта}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{корыта}} \cdot \cos(\upsilon \cdot \text{deg})$$

$$X'_{\text{ср.линии}} := X \cdot \cos(\upsilon \cdot \text{deg}) - Y_{\text{ср.линии}} \cdot \sin(\upsilon \cdot \text{deg})$$

$$Y'_{\text{ср.линии}} := X \cdot \sin(\upsilon \cdot \text{deg}) + Y_{\text{ср.линии}} \cdot \cos(\upsilon \cdot \text{deg})$$

### Довёрнутый центр тяжести

$$x'_c := x_c \cdot \cos(\upsilon \cdot \text{deg}) - y_c \cdot \sin(\upsilon \cdot \text{deg})$$

$$y'_c := x_c \cdot \sin(\upsilon \cdot \text{deg}) + y_c \cdot \cos(\upsilon \cdot \text{deg})$$

### Перемещение центра тяжести сечения в начало координат

$$X'_{\text{спинки}} := XX'_{\text{спинки}} - x'_c$$

$$Y'_{\text{спинки}} := YY'_{\text{спинки}} - y'_c$$

$$X'_{\text{корыта}} := XX'_{\text{корыта}} - x'_c$$

$$Y'_{\text{корыта}} := YY'_{\text{корыта}} - y'_c$$

$$X'_{\text{ср.линии}} := X'_{\text{ср.линии}} - x'_c$$

$$Y'_{\text{ср.линии}} := Y'_{\text{ср.линии}} - y'_c$$

---

<!-- page 36 -->

### Скорректированные функции

$$Sc := \text{lspline}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$y_{\text{спинки}}(x) := \begin{cases} \text{interp}(Sc, X'_{\text{спинки}}, Y'_{\text{спинки}}, x) & \text{if } \min(X'_{\text{спинки}}) \le x \le \max(X'_{\text{спинки}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$y_{\text{корыта}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{корыта}}, Y'_{\text{корыта}}, x) & \text{if } \min(X'_{\text{корыта}}) \le x \le \max(X'_{\text{корыта}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$Sc := \text{lspline}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

$$y_{\text{ср.линии}(x)} := \begin{cases} \text{interp}(Sc, X'_{\text{ср.линии}}, Y'_{\text{ср.линии}}, x) & \text{if } \min(X'_{\text{ср.линии}}) \le x \le \max(X'_{\text{ср.линии}}) \\ \text{NaN} & \text{otherwise} \end{cases}$$

$$\text{Спинка} := \text{augment}(X'_{\text{спинки}}, Y'_{\text{спинки}})$$

$$\text{Срлиния} := \text{augment}(X'_{\text{корыта}}, Y'_{\text{корыта}})$$

$$\text{Корытце} := \text{augment}(X'_{\text{ср.линии}}, Y'_{\text{ср.линии}})$$

---

<!-- page 37 -->

*(Конец документа — графики профилей всех сечений: среднее РК, периферийное РК, втулочное РК, среднее НА, периферийное НА, втулочное НА)*
