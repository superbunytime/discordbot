from sqlalchemy import select, text, insert
from sqlalchemy.orm import Session
import db, models

print(db.engine)


def temp_name(list):
  engine = models.get_connection()
  con = engine.connect()
  for member in list:
    print(f'this is line 10: {member}')
    # insert(models.USER).values(id = member.id, name = member.name, has_roles = len(member.roles) == 2, join_date = member.joined_at.strftime("%c"))
    sql = insert(models.USER).values(**member)
    con.execute(sql)

# should loop through and add all members to the member list database

#for member in mem_list:
  # now = datetime.now()
  # then = now - timedelta(days = 7)
  # if member.joined_at.strftime("%c") > then
    #insert("has_not_onboarded").values(id = member.id, name = member.name, has_roles = len(member.roles) == 2, join_date = member.joined_at.strftime("%c"))

# should grab all the users who haven't completed onboarding after one week

# kickable = has_not_onboarded.query.all()
#for kickee in kickable:
  # await kickee.kick(reason = "has not onboarded within timeframe")

# should kick all members from has_not_onboarded table




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