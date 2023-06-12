from sqlalchemy import select
from sqlalchemy.orm import Session
import db, models

print(db.engine)



"""Write your queries here"""

"""build users table:
Initial table population: Get all users currently on server"""

# run this on bot launch, and re-run it daily to update
# do i need to delist kicked members? probably not

"""build purge_table:
users from the users table that haven't completed onboarding
after one week get sent to the purge table, which will
be drawn from when calling the kick function daily."""

"""build privileged roles table:
users that have the active_user role will be added to
the active_role table, wherein they will be granted
access to priveleged server content"""