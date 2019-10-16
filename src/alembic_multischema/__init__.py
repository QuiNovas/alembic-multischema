from alembic import op
from sqlalchemy.sql import text

def getNonSystemSchemas(exclude=[]):
    try:
      conn = op.get_bind()
      schemas = conn.execute(text("SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('information_schema', 'pg_catalog')")).fetchall()
      return [ str(x[0]) for x in schemas if x not in exclude]
    except:
      return []

def getSchemas(exclude=[]):
    try:
      conn = op.get_bind()
      schemas = conn.execute(text("SELECT schema_name FROM information_schema.schemata")).fetchall()
      return [ str(x[0]) for x in schemas if x not in exclude ]
    except:
      return []

def perSchema(schemas=getNonSystemSchemas(), exclude=[]):
  def externalWrapper(func):
    def wrapper(*args, **kwargs):
      for s in schemas if s not in exclude:
        print("Executing on schema {}".format(s))
        try:
          op.execute(text("SET search_path TO {}".format(s)))
          func(*args, **kwargs)
          op.execute(text("SET search_path TO default"))
        except Exception as e:
          op.execute(text("SET search_path TO default"))
          raise e
    return wrapper
  return externalWrapper
