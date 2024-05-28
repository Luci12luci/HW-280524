from app import db


class Author(db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.Text)