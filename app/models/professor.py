from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional

class ProfessorModel(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    materia: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    senha: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))