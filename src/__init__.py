from alembic import op
from sqlalchemy.sql import text

def getAllSchemas():
  try:
    conn = op.get_bind()
    schemas = conn.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('information_schema', 'pg_catalog')")).fetchall()
    return [ str(x[0]) for x in schemas ]
  except:
    return []

def perSchema(schemas=getAllSchemas()):
  def externalWrapper(func):
    def wrapper(*args, **kwargs):
      for s in schemas:
        print(schemas)
        print("Executing on schema {}".format(s))
        try:
          op.execute(text("SET search_path TO {}".format(s)))
          func(*args, **kwargs)
          op.execute(text("SET search_path TO default"))
        except Exception as e:
          print(e)
          raise SystemExit
    return wrapper
  return externalWrapper
