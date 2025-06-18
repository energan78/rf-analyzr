# RF Analyzer Web Interface

Веб-приложение для работы с HackRF One и анализа записанных файлов. Позволяет определять диапазон сигнала, тип, наличие шифрования, выполнять распознавание речи и преобразование в текст, обработку видео, анализ телеметрии.

## Возможности

- 📡 Работа с HackRF One через веб-интерфейс
- 📊 Визуализация сигналов в реальном времени
- 🔍 Анализ записанных файлов
- 🗣️ Распознавание речи и преобразование в текст
- 🎥 Обработка видео
- 📈 Анализ телеметрии
- 💾 Библиотека файлов с комментариями

## Технологии

### Frontend
- React + Vite
- TypeScript
- Material UI
- React Router
- Chart.js для визуализации

### Backend
- Python + Flask
- SQLite для хранения данных
- SQLAlchemy ORM
- Flask-SocketIO для real-time коммуникации

## Установка

### Требования
- Python 3.8+
- Node.js 16+
- HackRF One

### Backend

1. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv backend-venv
# Windows
.\backend-venv\Scripts\activate
# Linux/MacOS
source backend-venv/bin/activate
```

2. Установите зависимости:
```bash
cd backend
pip install -r requirements.txt
```

### Frontend

1. Установите зависимости:
```bash
cd frontend
npm install
```

## Запуск

### Режим разработки

1. Запустите backend:
```bash
# В директории backend
flask run --debug
```

2. Запустите frontend:
```bash
# В директории frontend
npm run dev
```

Приложение будет доступно по адресу http://localhost:5173

### Продакшн

1. Соберите frontend:
```bash
cd frontend
npm run build
```

2. Запустите backend:
```bash
# В директории backend
flask run
```

## Работа с GitHub

### Клонирование репозитория

1. Установите Git с [официального сайта](https://git-scm.com/downloads)

2. Склонируйте репозиторий:
```bash
# HTTPS
git clone https://github.com/energan78/rf-analyzr.git
# или SSH, если настроен SSH-ключ
git clone git@github.com:energan78/rf-analyzr.git

# Перейдите в директорию проекта
cd rf-analyzr
```

### Первоначальная настройка после клонирования

1. Установите зависимости backend:
```bash
# Создайте и активируйте виртуальное окружение Python
python -m venv backend-venv

# Windows
.\backend-venv\Scripts\activate
# Linux/MacOS
source backend-venv/bin/activate

# Установите зависимости
cd backend
pip install -r requirements.txt
```

2. Установите зависимости frontend:
```bash
cd frontend
npm install
```

### Обновление локальной копии

Чтобы получить последние изменения с GitHub:

```bash
# Получить изменения
git pull origin main

# Если есть изменения в зависимостях Python
cd backend
pip install -r requirements.txt

# Если есть изменения в зависимостях npm
cd frontend
npm install
```

### Отправка своих изменений

1. Проверьте статус изменений:
```bash
git status
```

2. Добавьте измененные файлы:
```bash
# Добавить все изменения
git add .
# Или добавить конкретный файл
git add путь/к/файлу
```

3. Создайте коммит:
```bash
git commit -m "Описание ваших изменений"
```

4. Отправьте изменения на GitHub:
```bash
git push origin main
```

### Решение проблем

1. Конфликты при pull:
```bash
# Сохраните свои изменения во временную область
git stash

# Получите последние изменения
git pull origin main

# Верните свои изменения
git stash pop

# Разрешите конфликты в файлах, если они возникли
# Затем добавьте и закоммитьте изменения
git add .
git commit -m "Resolve conflicts"
```

2. Отмена последнего коммита (если не отправлен на GitHub):
```bash
git reset --soft HEAD~1
```

3. Отмена изменений в файле:
```bash
git checkout -- путь/к/файлу
```

### Ветки

1. Создание новой ветки для разработки:
```bash
# Создать и переключиться на новую ветку
git checkout -b имя-ветки

# Пример для новой функции
git checkout -b feature/signal-analysis
```

2. Переключение между ветками:
```bash
git checkout имя-ветки
```

3. Слияние веток:
```bash
# Переключитесь на основную ветку
git checkout main

# Слейте изменения из другой ветки
git merge имя-ветки
```

### Обновление зависимостей

1. Python (backend):
```bash
# Активируйте виртуальное окружение
# Windows
.\backend-venv\Scripts\activate
# Linux/MacOS
source backend-venv/bin/activate

# Обновите все пакеты
pip install --upgrade -r requirements.txt
```

2. Node.js (frontend):
```bash
# Проверьте устаревшие пакеты
npm outdated

# Обновите все пакеты
npm update

# Или обновите конкретный пакет
npm update имя-пакета
```

## Структура проекта

```
.
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── utils/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── app.tsx
│   ├── public/
│   └── package.json
└── README.md
```

## Лицензия

MIT
