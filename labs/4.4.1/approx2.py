import matplotlib.pyplot as plt

# Экспериментальные данные с погрешностью 1%
m_exp = [1, 2, 3]
D_exp = [32.32091207, 138.5181946, 285.3474809]
yerr = [d * 0.1 for d in D_exp]

# Теоретические данные
m_theory = [0, 1, 2, 3]
D_theory = [0, 52.26603042, 123.5806851, 306.0329566]

# Создание фигуры
plt.figure(figsize=(10, 6))

# Построение теоретических точек (квадраты)
plt.scatter(m_theory, D_theory, marker='s', s=80, color='red', 
            zorder=2, label='Теоретическая оценка')

# Экспериментальные точки с погрешностями (круги)
plt.errorbar(m_exp, D_exp, yerr=yerr, fmt='o', color='blue',
             markersize=8, capsize=5, capthick=2, elinewidth=2,
             zorder=3, label='Экспериментальные данные')

# Настройка графика
plt.xlim(-0.2, 4)
plt.ylim(0, 350)
plt.xlabel('m', fontsize=12)
plt.ylabel(r'D, $\AA$ / рад $\cdot 10^6$', fontsize=12)
plt.title('Зависимость D(m)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left')

plt.savefig('approx2.png')
