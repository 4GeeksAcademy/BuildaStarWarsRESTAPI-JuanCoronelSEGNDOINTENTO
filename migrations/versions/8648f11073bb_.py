"""empty message

Revision ID: 8648f11073bb
Revises: 14697336d5d6
Create Date: 2023-08-31 19:04:43.866556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8648f11073bb'
down_revision = '14697336d5d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['password'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('password')

    # ### end Alembic commands ###
