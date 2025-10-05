import subprocess
import sys

# Формируем команду
cmd = [
    'flask-sqlacodegen',
    '--flask',
    '--schema', 'ob',
    'postgresql://remote:Klljoy99@localhost/db'
]

# Запускаем без capture_output
result = subprocess.run(
    cmd,
    stdout=subprocess.PIPE,   # перехватываем stdout
    stderr=subprocess.PIPE,   # перехватываем stderr (опционально)
    shell=False
)

# Получаем "сырой" вывод как байты
raw_output = result.stdout

# Декодируем с игнорированием ошибок
try:
    clean_output = raw_output.decode('utf-8')
except UnicodeDecodeError:
    # Если не UTF-8 — пробуем с игнорированием проблемных символов
    clean_output = raw_output.decode('utf-8', errors='ignore')

# Убираем BOM (если есть)
if clean_output.startswith('\ufeff'):
    clean_output = clean_output[1:]

# Записываем в файл в чистом UTF-8 без BOM
with open('app/models.py', 'w+', encoding='utf-8', newline='') as f:
    f.write(clean_output)

# Выводим ошибки (если были)
if result.stderr:
    print("Ошибки при генерации:", result.stderr.decode('utf-8', errors='ignore'))

print("✅ models.py успешно создан")