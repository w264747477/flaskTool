"""empty message

Revision ID: 52db1dc47d09
Revises: 
Create Date: 2022-12-10 14:20:19.313689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52db1dc47d09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('syuser',
    sa.Column('userName', sa.String(length=36), nullable=False),
    sa.Column('passWord', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('userName')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('syuser')
    # ### end Alembic commands ###