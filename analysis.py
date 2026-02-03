import pandas as pd

# Загрузка данных
df = pd.read_json('events.json')

# Основная информация
print("Размер таблицы:", df.shape)
print("\nПервые 3 строки:")
print(df.head(3))

# Распределение по полю signature
print("\nРаспределение событий по типам (signature):")
print(df['signature'].value_counts().to_frame(name='Количество'))

# Распределение по уровню опасности
print("\nРаспределение по severity:")
print(df['severity'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

# Дополнительно: самые частые IP-источники атак
print("\nТоп-5 источников атак (source_ip):")
print(df['source_ip'].value_counts().head(5))

# Среднее время ответа при блокировке
print("\nСреднее время ответа (мс) при action = 'blocked':")
print(df[df['action'] == 'blocked']['response_time'].mean().round(1))