"""rename department

Revision ID: 159421e66d97
Revises: 355f906be9ba
Create Date: 2024-11-21 23:15:53.876818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '159421e66d97'
down_revision = '355f906be9ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
