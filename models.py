import sqlalchemy
from sqlalchemy import BigInteger, Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db = sqlalchemy()

engine = db.create_engine()

class USER(db.model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String, nullable = False)
    active_user = db.Column(db.Boolean, nullable = False)
    has_roles = db.Column(db.Boolean, nullable = False)
    join_date = db.Column(db.DateTime, nullable = False)

def connect_db(app):
    """Call this in your bot on startup to connect.
    This is code snagged from the flask app solution,
    so it may need to be messed with to connect to the
    discord app properly."""
    
    db.app = app
    db.init_app(app)