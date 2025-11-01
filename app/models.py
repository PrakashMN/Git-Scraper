from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class GitHubProfile(db.Model):
    __tablename__ = 'github_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120))
    bio = db.Column(db.Text)
    bio_language = db.Column(db.String(20))
    bio_sentiment = db.Column(db.Float)
    public_repos = db.Column(db.Integer)
    followers = db.Column(db.Integer)
    following = db.Column(db.Integer)
    avatar_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    repositories = db.relationship('Repository', backref='profile', cascade='all, delete-orphan')
    exports = db.relationship('DataExport', backref='profile', cascade='all, delete-orphan')

class Repository(db.Model):
    __tablename__ = 'repositories'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('github_profiles.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    stars = db.Column(db.Integer, default=0)
    language = db.Column(db.String(50))
    html_url = db.Column(db.String(255))

class DataExport(db.Model):
    __tablename__ = 'data_exports'
    
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('github_profiles.id'), nullable=False)
    format = db.Column(db.String(10), nullable=False)  # json, csv
    file_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)