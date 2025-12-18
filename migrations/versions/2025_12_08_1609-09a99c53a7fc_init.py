"""init

Revision ID: 09a99c53a7fc
Revises:
Create Date: 2025-12-08 16:09:53.681950

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "09a99c53a7fc"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: создаем таблицу post"""
    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("body", sa.Text, nullable=False),
        sa.Column("id_auth", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema: удаляем таблицу post"""
    op.drop_table("post")
