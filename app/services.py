import os
import requests
from textblob import TextBlob
from langdetect import detect, DetectorFactory

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
    user, code = github_user(username, token)
    if not user:
        return None, code

    repos = github_repos(username, token)
    repos_sorted = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]

    bio = user.get("bio")
    profile = {
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
    return profile, 200
