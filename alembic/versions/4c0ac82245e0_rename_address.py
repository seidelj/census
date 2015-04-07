"""rename address

Revision ID: 4c0ac82245e0
Revises: 
Create Date: 2015-03-09 16:35:05.148596

"""

# revision identifiers, used by Alembic.
revision = '4c0ac82245e0'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column("address", "address", new_column_name="street")


def downgrade():
    pass
