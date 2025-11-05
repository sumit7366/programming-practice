# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin
# from datetime import datetime

# db = SQLAlchemy()

# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)

# class Topic(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     description = db.Column(db.Text)
#     # Temporarily comment out created_at to avoid migration issues
#     # created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     questions = db.relationship('Question', backref='topic', lazy=True, cascade='all, delete-orphan')

# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question = db.Column(db.Text, nullable=False)
#     answer = db.Column(db.Text, nullable=False)
#     difficulty = db.Column(db.String(20), default='Basic')
#     topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

# class UserProgress(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
#     completed = db.Column(db.Boolean, default=False)
#     completed_at = db.Column(db.DateTime)

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    progress = db.relationship('UserProgress', backref='user', lazy=True)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    questions = db.relationship('Question', backref='topic', lazy=True, cascade='all, delete-orphan')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    difficulty = db.Column(db.String(20), default='Basic')
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_progress = db.relationship('UserProgress', backref='question', lazy=True)

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime)
    
    # Ensure one progress record per user per question
    __table_args__ = (db.UniqueConstraint('user_id', 'question_id', name='unique_user_question'),)