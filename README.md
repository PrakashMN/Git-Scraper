# GitHub Profile Explorer (Flask)

A **modern, sleek Flask web app** that lets you explore GitHub user profiles in style. Fetch a user’s details, analyze their bio, detect sentiment, view top repositories, and more — all presented in a **clean, responsive UI** powered by **Tailwind CSS (CDN)**. Perfect for developers, recruiters, or GitHub enthusiasts!  

---

## 🚀 Features

- **User Profile Fetching:** Input a GitHub username to view:
  - Name & username  
  - Avatar  
  - Bio  
  - Followers / Following  
  - Public repositories  

- **Bio Analysis:**  
  - Detects the **language** of the bio.  
  - Calculates a **sentiment score** (positive, negative, neutral).  

- **Top Repositories:**  
  - Lists repositories sorted by **stars**.  
  - Shows **primary language** and **description**.  

- **Data Export:**  
  - Download profile data as **CSV** for offline analysis.  
  - Optional **JSON API** endpoint for programmatic access.  

- **Performance Optimization:**  
  - **In-memory caching with TTL** to reduce GitHub API calls.  
  - Minimizes the risk of hitting rate limits.  

- **Modern UI:**  
  - Responsive and attractive layout using **Tailwind Play CDN**.  
  - Subtle animations and clean card-based design.  

- **Production Ready:**  
  - **Gunicorn** compatible.  
  - Ready to deploy on **Render** or any cloud platform.  