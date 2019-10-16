
# alembic-multischema
This module provides the ability to act on multiple postgres schemas at once when using alembic.

# Functions:
### perSchema(**kwargs)
Used to decorate the upgrade() and downgrade() functions in a migration. When upgrade or downgrade are decorated with perSchema() the decorated function will be called for a list of schemas in the current database.
#### kwargs:
  * schemas
  A list of schema names to run the function against. If omitted perSchema() will automatically generate a list of non-system schemas from the current database by using getAllNonSystemSchemas()

### getAllSchemas()
  Returns a list of all schemas in the current database.

### getAllNonSystemSchemas()
  Returns a list of schemas in the current database, omitting information_schema and pg_catalog.  

## Example Usage:
```
"""CreatePatientTable

Revision ID: a6a219646b55
Revises:
Create Date: 2019-10-16 14:43:11.347575

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
from almebic_multischema import perSchema

# revision identifiers, used by Alembic.
revision = 'a6a219646b55'
down_revision = None
branch_labels = None
depends_on = None

@perSchema(schemas=["public", "foo", "bar"])
def upgrade():
    patients = text(
      """CREATE TABLE users
          (
            id serial PRIMARY KEY,
            firstname VARCHAR (50) UNIQUE,
            lastname VARCHAR (50)
          );
      """)
    op.execute(patients)

@perSchema(schemas=["public", "foo", "bar"])
def downgrade():
    op.execute(text("DROP TABLE users"))
```
