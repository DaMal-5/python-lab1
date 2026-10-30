# Для запуска нужен uv
git clone https://github.com/DaMal-5/python-lab1.git
cd python-lab1
# Генерация файла с данными
uv run data/generate_measurements.py N -o measurements_*.txt
# Изменение кодировки (при ошибке на windows)
## $env:PYTHONIOENCODING="utf-8"
# Запуск программы
uv run main.py data/measurements_*.txt
# Проверка
uv run main.py data/measurements_*.txt \
    | python data/check.py data/measurements_*.out