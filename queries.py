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

# run this on bot launch, and re-run it daily to update
# do i need to delist kicked members? probably not