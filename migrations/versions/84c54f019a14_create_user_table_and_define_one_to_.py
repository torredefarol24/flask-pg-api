"""create user table and define one-to-many relation

Revision ID: 84c54f019a14
Revises: 7c896f6d15cf
Create Date: 2018-12-08 15:25:29.599045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84c54f019a14'
down_revision = '7c896f6d15cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullName', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('todo', sa.Column('user_id', sa.Integer(), nullable=False))
    op.alter_column('todo', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.create_foreign_key(None, 'todo', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.alter_column('todo', 'title',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.drop_column('todo', 'user_id')
    op.drop_table('user')
    # ### end Alembic commands ###
