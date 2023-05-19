import sqlalchemy
from sqlalchemy import BigInteger, Column, Integer, create_engine, String, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column



class Base(DeclarativeBase):
    pass
class USER(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    active_user: Mapped[str] = mapped_column(String(5))
    has_roles: Mapped[str] = mapped_column(String(5))
    join_date: Mapped[int] = mapped_column(Integer)
