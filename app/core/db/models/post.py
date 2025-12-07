from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Post(Base):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    id_auth: Mapped[int] = mapped_column(nullable=False, unique=True)