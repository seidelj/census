"""add block table

Revision ID: 1d0147288225
Revises: 4c0ac82245e0
Create Date: 2015-03-10 13:35:46.853824

"""

# revision identifiers, used by Alembic.
revision = '1d0147288225'
down_revision = '4c0ac82245e0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
	op.create_table(
		'geography',
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('state', sa.String),
		sa.Column('county', sa.String),
		sa.Column('tract', sa.String),
		sa.Column('block', sa.String),
	)
	op.drop_column('address', 'block')
	op.add_column('address', 
		sa.Column('geography_id', sa.Integer, sa.ForeignKey('address.id'))
	) 
	


def downgrade():
    op.drop_table('geography')

