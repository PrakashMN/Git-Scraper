from flask import Blueprint, render_template, request, current_app, jsonify, Response
from .services import build_profile, export_profile_data
from .models import GitHubProfile, DataExport

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

@bp.get("/export")
def export_data():
    username = request.args.get("username", "").strip()
    format = request.args.get("format", "json").lower()
    
    if not username:
        return "Username required", 400
    
    data, code = export_profile_data(username, format)
    if code != 200:
        return "Profile not found", 404
    
    if format == "json":
        return Response(
            data,
            mimetype="application/json",
            headers={"Content-Disposition": f"attachment; filename={username}_profile.json"}
        )
    elif format == "csv":
        return Response(
            data,
            mimetype="text/csv",
            headers={"Content-Disposition": f"attachment; filename={username}_profile.csv"}
        )
    
    return "Invalid format", 400

@bp.get("/dashboard")
def dashboard():
    profiles = GitHubProfile.query.order_by(GitHubProfile.updated_at.desc()).limit(10).all()
    total_profiles = GitHubProfile.query.count()
    total_exports = DataExport.query.count()
    
    return render_template("dashboard.html", 
                         profiles=profiles, 
                         total_profiles=total_profiles,
                         total_exports=total_exports)
