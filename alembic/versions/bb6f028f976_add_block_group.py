"""add block group

Revision ID: bb6f028f976
Revises: 430eb0d9b0b9
Create Date: 2015-04-07 14:41:02.154080

"""

# revision identifiers, used by Alembic.
revision = 'bb6f028f976'
down_revision = '430eb0d9b0b9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('geography', sa.Column('blockgrp', sa.String))

def downgrade():
    op.drop_column('geography', 'geography')

