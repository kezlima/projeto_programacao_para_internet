from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as models


class Aluno(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(140))
    turma: so.Mapped[str] = so.mapped_column(sa.String(140))
   

   