"""add backref

Revision ID: 430eb0d9b0b9
Revises: 56b3a9407cd1
Create Date: 2015-03-19 10:44:56.118412

"""

# revision identifiers, used by Alembic.
revision = '430eb0d9b0b9'
down_revision = '56b3a9407cd1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref


def upgrade():
	op.drop_column('address', "geography_id")
	op.add_column('address',
		sa.Column('geography_id', sa.Integer, sa.ForeignKey('geography.id'))
	)
	op.create_foreign_key(
		"geography", "address",
		"geography", ['geography_id'], ["id"])

def downgrade():
    pass
