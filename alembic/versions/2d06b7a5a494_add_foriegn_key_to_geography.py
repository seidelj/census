"""add foriegn key to geography

Revision ID: 2d06b7a5a494
Revises: bb6f028f976
Create Date: 2015-04-09 13:19:47.652071

"""

# revision identifiers, used by Alembic.
revision = '2d06b7a5a494'
down_revision = 'bb6f028f976'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	op.add_column('geography',
		sa.Column('censusdatablk_id', sa.Integer, sa.ForeignKey('censusdatablk.id'))
	)
	op.create_foreign_key(
		"censusdatablk", "geography",
		"censusdatablk", ["censusdatablk_id"], ["id"])



def downgrade():
    pass
