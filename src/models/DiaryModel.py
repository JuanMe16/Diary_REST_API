from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime
from .UserModel import User
import sqlalchemy as sa
from src.database import db

class Diary(db.Model):
    __tablename__ = "diaries"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    user_id = sa.Column(sa.ForeignKey(User.id), nullable=False)
    title = sa.Column(sa.String(25), nullable=False)
    date = sa.Column(sa.Date, default=datetime.now, nullable=False)
    notes = sa.Column(LONGTEXT, nullable=False)

    @classmethod
    def create_diary_entry(cls, user_id, title, notes):
        diary = cls(
            user_id=user_id,
            title=title,
            notes=notes
        )
        db.session.add(diary)
        db.session.commit()
        return diary