import os
import json
import csv
import io
from datetime import datetime
import requests
from textblob import TextBlob
from langdetect import detect, DetectorFactory
from .models import db, GitHubProfile, Repository, DataExport

DetectorFactory.seed = 0

BASE_URL = "https://api.github.com"

def get_headers(token: str | None):
    if token:
        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
    return {"Accept": "application/vnd.github+json"}

def github_user(username: str, token: str | None):
    r = requests.get(f"{BASE_URL}/users/{username}", headers=get_headers(token))
    if r.status_code == 404:
        return None, 404
    if r.status_code == 403 and "rate limit" in r.text.lower():
        return None, 429
    if r.status_code != 200:
        return None, r.status_code
    return r.json(), 200

def github_repos(username: str, token: str | None):
    r = requests.get(f"{BASE_URL}/users/{username}/repos", params={"per_page": 100}, headers=get_headers(token))
    if r.status_code != 200:
        return []
    return r.json()

def analyze_bio(bio: str | None):
    if bio and bio.strip():
        return TextBlob(bio).sentiment.polarity
    return None

def detect_bio_language(bio: str | None):
    try:
        if bio and bio.strip():
            return detect(bio)
        return "N/A"
    except Exception:
        return "Unknown"

def build_profile(username: str, token: str | None):
    # Check if profile exists in DB
    existing_profile = GitHubProfile.query.filter_by(username=username).first()
    
    user, code = github_user(username, token)
    if not user:
        return None, code

    repos = github_repos(username, token)
    repos_sorted = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]

    bio = user.get("bio")
    profile_data = {
        "username": user.get("login"),
        "name": user.get("name"),
        "bio": bio,
        "bio_language": detect_bio_language(bio),
        "bio_sentiment": analyze_bio(bio),
        "public_repos": user.get("public_repos", 0),
        "followers": user.get("followers", 0),
        "following": user.get("following", 0),
        "avatar_url": user.get("avatar_url", ""),
        "top_repos": [
            {
                "name": r.get("name", ""),
                "description": r.get("description"),
                "stars": r.get("stargazers_count", 0),
                "language": r.get("language"),
                "html_url": r.get("html_url", "")
            } for r in repos_sorted
        ]
    }
    
    # Save/Update in database
    save_profile_to_db(profile_data, repos_sorted)
    
    return profile_data, 200

def save_profile_to_db(profile_data, repos):
    profile = GitHubProfile.query.filter_by(username=profile_data['username']).first()
    
    if profile:
        # Update existing
        profile.name = profile_data['name']
        profile.bio = profile_data['bio']
        profile.bio_language = profile_data['bio_language']
        profile.bio_sentiment = profile_data['bio_sentiment']
        profile.public_repos = profile_data['public_repos']
        profile.followers = profile_data['followers']
        profile.following = profile_data['following']
        profile.avatar_url = profile_data['avatar_url']
        profile.updated_at = datetime.utcnow()
        
        # Clear old repos
        Repository.query.filter_by(profile_id=profile.id).delete()
    else:
        # Create new
        profile = GitHubProfile(
            username=profile_data['username'],
            name=profile_data['name'],
            bio=profile_data['bio'],
            bio_language=profile_data['bio_language'],
            bio_sentiment=profile_data['bio_sentiment'],
            public_repos=profile_data['public_repos'],
            followers=profile_data['followers'],
            following=profile_data['following'],
            avatar_url=profile_data['avatar_url']
        )
        db.session.add(profile)
        db.session.flush()  # Get the ID
    
    # Add repositories
    for repo in repos:
        repository = Repository(
            profile_id=profile.id,
            name=repo.get('name', ''),
            description=repo.get('description'),
            stars=repo.get('stargazers_count', 0),
            language=repo.get('language'),
            html_url=repo.get('html_url', '')
        )
        db.session.add(repository)
    
    db.session.commit()
    return profile

def export_profile_data(username: str, format: str = 'json'):
    profile = GitHubProfile.query.filter_by(username=username).first()
    if not profile:
        return None, 404
    
    # Prepare export data
    export_data = {
        'profile': {
            'username': profile.username,
            'name': profile.name,
            'bio': profile.bio,
            'bio_language': profile.bio_language,
            'bio_sentiment': profile.bio_sentiment,
            'public_repos': profile.public_repos,
            'followers': profile.followers,
            'following': profile.following,
            'avatar_url': profile.avatar_url,
            'last_updated': profile.updated_at.isoformat()
        },
        'repositories': [
            {
                'name': repo.name,
                'description': repo.description,
                'stars': repo.stars,
                'language': repo.language,
                'html_url': repo.html_url
            } for repo in profile.repositories
        ],
        'exported_at': datetime.utcnow().isoformat()
    }
    
    # Create export record
    export_record = DataExport(
        profile_id=profile.id,
        format=format
    )
    db.session.add(export_record)
    db.session.commit()
    
    if format == 'json':
        return json.dumps(export_data, indent=2), 200
    elif format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Profile header
        writer.writerow(['Profile Data'])
        writer.writerow(['Username', 'Name', 'Bio', 'Repos', 'Followers', 'Following'])
        writer.writerow([profile.username, profile.name, profile.bio, 
                        profile.public_repos, profile.followers, profile.following])
        
        # Repositories header
        writer.writerow([])
        writer.writerow(['Repositories'])
        writer.writerow(['Name', 'Description', 'Stars', 'Language', 'URL'])
        
        for repo in profile.repositories:
            writer.writerow([repo.name, repo.description, repo.stars, repo.language, repo.html_url])
        
        return output.getvalue(), 200
    
    return None, 400
