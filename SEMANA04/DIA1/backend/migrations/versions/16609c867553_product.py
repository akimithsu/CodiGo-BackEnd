"""product

Revision ID: 16609c867553
Revises: 
Create Date: 2023-06-06 21:36:11.495171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16609c867553'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=254), nullable=True),
    sa.Column('price', sa.Double(), nullable=True),
    sa.Column('image', sa.String(length=254), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_product')
    # ### end Alembic commands ###
