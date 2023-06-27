from sqlalchemy import select, text, insert, update, delete
from sqlalchemy.orm import Session, query
import models

def add_to_db(list):
    engine = models.get_connection()
    with Session(engine) as session:
      if models.USER:
         models.USER.__table__.drop(engine)
      models.Base.metadata.create_all(engine)
      session.commit()
      for member in list:
        session.add(member)
        session.commit()

def read_from_db(list):
   engine = models.get_connection()
   with Session(engine) as session:
      if models.USER:
         result = session.execute(text("SELECT * FROM users"))
         for row in result.mappings():
            list.append({"id": row.id})
      print(list)
