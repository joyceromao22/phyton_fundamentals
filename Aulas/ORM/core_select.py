from sqlalchemy import select
from core import user_table

selecione = select([user_table])

print([x for x in selecione.execute()])
  