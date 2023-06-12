import sqlalchemy
from sqlalchemy import BigInteger, Column, Integer, create_engine, String, Integer, text, database_exists, create_database
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

# connection boilerplate blatantly copied from https://www.geeksforgeeks.org/connecting-to-sql-database-using-sqlalchemy-in-python/

user = "postgres"
password = "12345"
host = "127.0.0.1"
port = 5432
database = "postgres"


def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


if __name__ == "__main__":
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


class Base(DeclarativeBase):
    pass


class USER(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    active_user: Mapped[str] = mapped_column(String(5))
    has_roles: Mapped[str] = mapped_column(String(5))
    join_date: Mapped[int] = mapped_column(Integer)
