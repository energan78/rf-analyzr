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
