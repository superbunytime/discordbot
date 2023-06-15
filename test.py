from datetime import datetime
from models import USER
import queries

mem_list = list()
members = [
    {
        "id": 1,
        "name": "joe",
        "roles":  [1,2],
        "joined_at": datetime.now()
    },
    {
        "id": 2,
        "name": "john",
        "roles":  [1,2],
        "joined_at": datetime.now()
    }
]

members.append({"id": 3,
                "name": "dasklhfaef",
                "roles": [1],
                "joined_at": datetime.now()})

for member in members:
    new_user = USER(id = member['id'], name = member['name'], has_roles = len(member['roles']) == 2, join_date = member['joined_at'].strftime("%c"))
    mem_list.append(new_user)

queries.add_to_db(mem_list)

print(type(members))
print(members)
