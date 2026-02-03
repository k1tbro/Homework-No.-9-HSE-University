import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('events.json')

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Столбчатая диаграмма — распределение типов событий
plt.figure()
ax = sns.countplot(
    data=df,
    y='signature',
    order=df['signature'].value_counts().index,
    palette='viridis',
    hue='signature'  # чтобы избежать предупреждения в новых версиях seaborn
)
ax.set_title('Распределение событий информационной безопасности по типам', fontsize=14, pad=15)
ax.set_xlabel('Количество событий')
ax.set_ylabel('Тип события (signature)')

# Подписи значений на столбиках
for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

# 2. Круговая диаграмма по уровню серьёзности
plt.figure()
df['severity'].value_counts().plot.pie(
    autopct='%1.1f%%',
    colors=['#ff6b6b', '#ffd93d', '#6bcB77'],
    explode=[0.05, 0.05, 0.05],
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12}
)
plt.title('Распределение событий по уровню серьёзности', fontsize=14)
plt.ylabel('')
plt.show()

# 3. Дополнительно: график по протоколам и действиям (если интересно)
plt.figure()
sns.countplot(
    data=df,
    x='protocol',
    hue='action',
    palette='Set2'
)
plt.title('События по протоколам и выполненным действиям')
plt.xlabel('Протокол')
plt.ylabel('Количество событий')
plt.legend(title='Действие')
plt.show()