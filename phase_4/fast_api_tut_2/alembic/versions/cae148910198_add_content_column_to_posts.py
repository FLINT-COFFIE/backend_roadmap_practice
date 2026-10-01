"""add content column to posts

Revision ID: cae148910198
Revises: 3b19705fa330
Create Date: 2026-09-27 20:10:02.808839

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cae148910198"
down_revision: Union[str, Sequence[str], None] = "3b19705fa330"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
