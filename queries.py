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
            print(row.id) # gets the ID. we're in business.  Now just rebuild the user from the ID.
            list.append({"id": row.id})
# run this on bot launch, and re-run it daily to update
# do i need to delist kicked members? probably not