from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, MetaData
from sqlalchemy.orm import Session, DeclarativeBase
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass

# Создаем движок базы данных
engine = create_engine(os.getenv('DATABASE_URL', 'sqlite:///rf_analyzer.db'))

class RFCapture(Base):
    __tablename__ = 'rf_captures'

    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    frequency = Column(Float, nullable=False)
    sample_rate = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    signal_type = Column(String(50))
    comments = Column(Text)
    meta_info = Column(Text)  # JSON строка с дополнительными метаданными

    def __repr__(self):
        return f"<RFCapture(filename='{self.filename}', frequency={self.frequency})>"

def init_db():
    """Создает все таблицы в базе данных"""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Возвращает сессию для работы с базой данных"""
    return Session(engine)
