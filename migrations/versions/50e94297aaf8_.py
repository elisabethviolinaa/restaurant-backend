"""empty message

Revision ID: 50e94297aaf8
Revises: cc5ce73fcfa3
Create Date: 2023-12-09 23:46:12.886873

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '50e94297aaf8'
down_revision = 'cc5ce73fcfa3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('food_and_beverage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('food')
    op.drop_table('beverage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beverage',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('food',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('food_and_beverage')
    # ### end Alembic commands ###