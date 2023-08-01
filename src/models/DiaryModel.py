from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime
from sqlalchemy import select
from .UserModel import User
from src.database import db
import sqlalchemy as sa

class Diary(db.Model):
    __tablename__ = "diaries"

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    user_id = sa.Column(sa.ForeignKey(User.id), nullable=False)
    title = sa.Column(sa.String(25), nullable=False)
    date = sa.Column(sa.Date, default=datetime.now, nullable=False)
    notes = sa.Column(LONGTEXT, nullable=False)

    @classmethod
    def read_diary_entry(cls, id):
        diary_entry = db.session.execute(select(Diary).filter_by(id=id)).scalar_one()
        return {"date": diary_entry.date, "notes": diary_entry.notes}

    @classmethod
    def create_diary_entry(cls, user_id, title, notes):
        diary = cls(
            user_id=user_id,
            title=title,
            notes=notes
        )
        db.session.add(diary)
        db.session.commit()
        return diary.id
    
    @classmethod
    def update_diary_entry(cls, id, title, notes):
        diary_entry = db.session.execute(select(Diary).filter_by(id=id)).scalar_one()
        old_notes = diary_entry.notes
        diary_entry.notes = notes
        diary_entry.title = notes
        db.session.commit()
        return old_notes

    @classmethod
    def delete_diary_entry(cls, id):
        diary_entry = db.session.execute(select(Diary).filter_by(id=id)).scalar_one()
        deleted_id = diary_entry.id
        db.session.delete(diary_entry)
        db.session.commit()
        return deleted_id