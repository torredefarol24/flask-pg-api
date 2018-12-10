"""update field in orders table

Revision ID: d121e63f1f6b
Revises: 4cce7a6791d2
Create Date: 2018-12-10 18:41:27.229881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd121e63f1f6b'
down_revision = '4cce7a6791d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order', 'created_at',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('order', 'status',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('order_product', 'order_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order_product', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_product', 'product_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order_product', 'order_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order', 'status',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('order', 'created_at',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###