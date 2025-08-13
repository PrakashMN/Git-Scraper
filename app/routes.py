from flask import Blueprint, render_template, request, current_app, jsonify
from .services import build_profile

bp = Blueprint("main", __name__)

@bp.get("/")
def index():
    return render_template("index.html")

@bp.get("/profile")
def profile_page():
    username = request.args.get("username", "").strip()
    if not username:
        return render_template("index.html", error="Please enter a username"), 400

    profile, code = build_profile(username, current_app.config.get("GITHUB_TOKEN"))
    if code != 200:
        msg = "User not found" if code == 404 else ("Rate limit exceeded" if code == 429 else "GitHub API error")
        return render_template("index.html", error=msg, last_username=username), code

    return render_template("profile.html", data=profile)
