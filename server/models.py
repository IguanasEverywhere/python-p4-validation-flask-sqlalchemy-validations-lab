from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name_val):
        if not name_val:
            raise ValueError("failed name validation")

    @validates("phone_number")
    def validate_phone_number(self, key, num_val):
        if len(num_val) != 10:
            raise ValueError("failed phone number validation")

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validate_content(self, key, content_val):
        if len(content_val) < 250:
            raise ValueError("failed content validation")

    @validates("summary")
    def validate_summary(self, key, summary_val):
        if len(summary_val) >= 250:
            raise ValueError("failed summary validation")

    @validates("category")
    def validate_category(self, key, category_val):
        if category_val != "Fiction" and category_val != "Non-Fiction":
            raise ValueError("failed category validation")

    @validates("title")
    def validate_title(self, key, title_val):
        phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any([phrase in title_val for phrase in phrases]):
            raise ValueError("failed title validation")


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
