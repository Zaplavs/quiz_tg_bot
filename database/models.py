from sqlalchemy import BigInteger, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime

# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass

# Модель пользователя
class User(Base):
    __tablename__ = 'users'

    # Поля таблицы
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=True) # username может отсутствовать
    full_name: Mapped[str] = mapped_column(String(150))
    
    # Данные для квиза
    best_score: Mapped[int] = mapped_column(default=0)
    attempts_left: Mapped[int] = mapped_column(default=3)

    invited_by_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    
    # Дата регистрации с автоматическим заполнением
    registration_date: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return f"<User {self.user_id} {self.username}>"