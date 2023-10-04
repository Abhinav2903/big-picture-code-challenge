
# Create Databse Model for the Library
from app import db

class Library(db.Model):
    __tablename__ = "books"
    #primary key for the database is isbn 
    isbn = db.Column(db.Integer, primary_key=True)
    # create columns for title,author,cover and summary
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    cover = db.Column(db.String(255))
    summary = db.Column(db.String(1000))
    
    def to_json(self):
        return {
            'isbn': self.isbn,
            'author': self.author,
            'title': self.title,
            'cover': self.cover,
            'summary': self.summary
        }
