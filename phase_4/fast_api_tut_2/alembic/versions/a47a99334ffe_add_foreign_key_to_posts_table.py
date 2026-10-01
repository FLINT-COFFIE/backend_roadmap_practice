"""add foreign-key to posts table.

Revision ID: a47a99334ffe
Revises: 47231c1468ca
Create Date: 2026-09-27 20:44:50.730358

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a47a99334ffe"
down_revision: str | Sequence[str] | None = "47231c1468ca"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "user_id")
