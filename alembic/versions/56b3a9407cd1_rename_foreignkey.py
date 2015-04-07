"""rename foreignkey

Revision ID: 56b3a9407cd1
Revises: 1d0147288225
Create Date: 2015-03-19 09:45:19.128118

"""

# revision identifiers, used by Alembic.
revision = '56b3a9407cd1'
down_revision = '1d0147288225'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	op.drop_column('address', 'geography_id')
	op.add_column("address",
		sa.Column('geography_id', sa.Integer, sa.ForeignKey('geography.id'))
	)

def downgrade():
    pass
