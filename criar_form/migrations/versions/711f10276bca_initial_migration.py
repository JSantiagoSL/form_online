"""Initial migration

Revision ID: 711f10276bca
Revises: 
Create Date: 2024-09-26 23:19:33.607478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711f10276bca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('formulario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=200), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pergunta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('texto', sa.Text(), nullable=False),
    sa.Column('tipo', sa.String(length=50), nullable=False),
    sa.Column('formulario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formulario_id'], ['formulario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pergunta')
    op.drop_table('formulario')
    # ### end Alembic commands ###
