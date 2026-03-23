<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:a855f7&height=200&section=header&text=GitHub%20Profile%20Scraper&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=ML-Powered%20Sentiment%20Analysis%20for%20Developer%20Insights&descAlignY=58&descSize=16&descColor=e2e8f0" width="100%"/>

<br/>

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-git--scraper--xtiq.onrender.com-6366f1?style=for-the-badge&logoColor=white)](https://git-scraper-xtiq.onrender.com/)
[![Research Paper](https://img.shields.io/badge/📄%20Research%20Paper-ResearchGate-00CCBB?style=for-the-badge)](https://www.researchgate.net)
[![License](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)

<br/>

> **Beyond stars and forks — understand how developers truly communicate.**  
> A peer-reviewed, open-source system combining GitHub scraping with NLP-based sentiment analysis,  
> presented in an interactive full-stack dashboard.

<br/>

</div>

---

## 🧠 What Is This?

**GitHub Profile Scraper** is an open-source research system that enriches developer profiling by layering **machine learning–based sentiment analysis** on top of standard GitHub metrics.

While most tools tell you *how much* a developer has built, this system reveals *how* they communicate — the tone of their commit messages, the positivity of their repository descriptions, and the emotional signals hidden in their bio. The findings are backed by a peer-reviewed research paper evaluated on **210 real GitHub profiles**.

```
Stars + Forks + Followers  →  What a developer built
Sentiment + Polarity + Tone →  Who a developer is
```

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔍 Profile Intelligence
- Fetch any public GitHub profile instantly
- Extract bio, location, organization, follower/following counts
- Detect **programming language distribution** across all repos
- Surface top repositories sorted by star count

</td>
<td width="50%">

### 🧬 Sentiment Analysis Engine
- **Polarity scoring** in range `[-1.0, +1.0]`
- **Subjectivity scoring** in range `[0.0, 1.0]`
- Three-class labeling: `Positive` · `Neutral` · `Negative`
- Weighted multi-source aggregation across bio, descriptions & commits

</td>
</tr>
<tr>
<td width="50%">

### 🌍 Multilingual Support
- Language detection via **langdetect** (96% coverage)
- Handles English, European, East Asian & mixed-language profiles
- Optional translation pipeline for non-English content

</td>
<td width="50%">

### ⚡ Performance & Scale
- **MongoDB caching** with 24-hour TTL
- OAuth token rotation pool for high-throughput scraping
- Exponential backoff on GitHub API rate limits
- Batch processing support for bulk profile analysis

</td>
</tr>
<tr>
<td width="50%">

### 📊 Interactive Dashboard
- Sentiment gauge with live color coding
- Activity timeline overlaid with polarity trends
- Language distribution bar charts
- Sortable repository table with per-repo sentiment scores

</td>
<td width="50%">

### 📦 Data Export
- Export results as **JSON** (full structured data)
- Export results as **CSV** (ready for R, SPSS, pandas)
- Includes polarity, subjectivity, metadata & engagement metrics

</td>
</tr>
</table>

---

## 📊 Research Highlights

This project is backed by a peer-reviewed paper. Key findings from analysis of **210 GitHub profiles**:

| Metric | Finding |
|--------|---------|
| 🟢 Positive sentiment in repo descriptions | **68%** |
| ⚪ Neutral sentiment | **22%** |
| 🔴 Negative sentiment | **10%** |
| 🎯 TextBlob classification accuracy | **78%** |
| 📈 Median followers (positive profiles) | **318** vs **49** (negative) |
| ⭐ Median stars (positive profiles) | **142** vs **18** (negative) |
| 📊 Statistical significance | **p < 0.001** (χ² test) |

> 💡 Profiles with consistently positive communication attract **6x more followers and stars** than negative-sentiment profiles.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT BROWSER                           │
│              Jinja2 Templates · Tailwind CSS · JS               │
│         index.html · profile.html · dashboard.html              │
└──────────────────────────┬──────────────────────────────────────┘
                           │ HTTP
┌──────────────────────────▼──────────────────────────────────────┐
│                    FLASK APP  (routes.py)                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    services.py                           │   │
│  │  GitHub API scraping · BeautifulSoup · Preprocessing     │   │
│  │  TextBlob · VADER · SentiStrength · langdetect           │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│  │  models.py   │  │  config.py   │  │      wsgi.py         │  │
│  │ Data schemas │  │  Env + setup │  │  Gunicorn entrypoint │  │
│  └──────────────┘  └──────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
          │
┌─────────▼───────────────────────────────────────────────────────┐
│                    GITHUB REST API v3                            │
│        /users · /repos · /commits · /readme                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.12, Flask 2.x, Gunicorn |
| **Frontend** | Jinja2 Templates, Tailwind CSS (CDN), Vanilla JS |
| **NLP / ML** | TextBlob, VADER, SentiStrength, langdetect, NLTK |
| **Data Source** | GitHub REST API v3 + BeautifulSoup |
| **Deployment** | Render (via `wsgi.py`) |

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.12+
GitHub Personal Access Token
```

### 1. Clone the Repository

```bash
git clone https://github.com/PrakashMN/github-profile-scraper.git
cd github-profile-scraper
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
GITHUB_TOKEN=your_github_personal_access_token
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

### 5. Run the App

```bash
# Development
flask run

# Production (Gunicorn)
gunicorn wsgi:app
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📁 Project Structure

```
github-profile-scraper/
├── app/
│   ├── __pycache__/           # Python bytecode cache
│   ├── static/
│   │   └── css/
│   │       └── styles.css     # Global stylesheet
│   ├── templates/
│   │   ├── base.html          # Base layout template
│   │   ├── index.html         # Home / search page
│   │   ├── profile.html       # Profile results & sentiment view
│   │   └── dashboard.html     # Aggregated stats dashboard
│   ├── __init__.py            # Flask app factory
│   ├── config.py              # App configuration & env vars
│   ├── models.py              # Data models & schema definitions
│   ├── routes.py              # URL routing & view functions
│   └── services.py            # GitHub API, scraping & sentiment logic
├── instance/                  # Instance-specific config (gitignored)
├── .env                       # Local environment variables (gitignored)
├── .env.example               # Environment variable template
├── .gitignore
├── README.md
├── requirements.txt           # Python dependencies
└── wsgi.py                    # WSGI entry point for Gunicorn/Render
```

---

## 🔌 Routes Reference

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Home page — GitHub username search |
| `GET/POST` | `/profile/<username>` | Fetch, analyze & display a profile |
| `GET` | `/dashboard` | Aggregated stats across all analyzed profiles |

### Core Logic — `services.py`

All scraping, preprocessing, and sentiment analysis lives in `services.py`:

```python
# Key functions
fetch_github_profile(username)   # GitHub API + BeautifulSoup
preprocess_text(text)            # Tokenize, lemmatize, strip code/URLs
detect_language(text)            # langdetect ISO 639-1 detection
analyze_sentiment(text)          # TextBlob polarity + subjectivity
aggregate_profile_sentiment(bio, descriptions, commits)  # Weighted score
```

---

## 📈 Sentiment Scoring Formula

Profile-level sentiment is computed as a weighted average across text sources:

$$P_{profile} = 0.5 \cdot P_{desc} + 0.3 \cdot P_{commit} + 0.2 \cdot P_{bio}$$

| Source | Weight | Rationale |
|--------|--------|-----------|
| Repository Descriptions | 0.50 | Highest volume & most intentional text |
| Commit Messages | 0.30 | Frequent but terse; lower signal density |
| Bio Text | 0.20 | Personal but short; limited corpus |

---

## 🧪 Tool Comparison

| Tool | Accuracy | Macro F1 | Best For |
|------|----------|----------|----------|
| **TextBlob** ✅ | **78%** | **0.74** | Structured descriptions & bios |
| VADER | 74% | 0.71 | Short informal text, commit messages |
| SentiStrength | 70% | 0.67 | Single-sentence sentiment |

*Evaluated on 60 manually annotated GitHub profiles (Cohen's κ = 0.73)*

---

## 🌐 Deployment

This project is deployed on **Render** using `wsgi.py` as the entry point. To deploy your own instance:

1. Fork this repository
2. Connect to [render.com](https://render.com) and create a new **Web Service**
3. Set the following:

| Setting | Value |
|---------|-------|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn wsgi:app` |

4. Add your environment variables (`GITHUB_TOKEN`, `SECRET_KEY`, `FLASK_ENV=production`) in the Render dashboard
5. Deploy — your app will be live at `https://your-app.onrender.com`

---

## 📄 Research Paper

This project is the subject of a peer-reviewed research paper:

> **Nagaral, P.** (2026). *GitHub Profile Scraper with Machine Learning–Based Sentiment Analysis for Developer Insights.* The Monster Labs.  
> 🔗 [Read on ResearchGate](#) · 🌐 [Live Tool](https://git-scraper-xtiq.onrender.com/)

**Dataset:** Processed results for all 210 profiles are available in `/dataset/` for reproducibility.

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/transformer-sentiment

# 3. Commit your changes
git commit -m "Add BERT-based sentiment model"

# 4. Push and open a Pull Request
git push origin feature/transformer-sentiment
```

**Roadmap contributions we'd love:**
- [ ] BERT/RoBERTa fine-tuned on SE corpora
- [ ] GitLab & Bitbucket support
- [ ] Issue tracker & PR sentiment analysis
- [ ] Celery + Redis async processing
- [ ] NLP explainability (phrase-level highlighting)

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ by [Prakash Nagaral](https://github.com/PrakashMN)**  
*The Monster Labs · hello@themonsterlabs.com*

[![GitHub](https://img.shields.io/badge/GitHub-PrakashMN-181717?style=flat-square&logo=github)](https://github.com/PrakashMN)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Profile-00CCBB?style=flat-square&logo=researchgate)](https://www.researchgate.net)
[![Live Demo](https://img.shields.io/badge/Live-Demo-6366f1?style=flat-square&logo=render)](https://git-scraper-xtiq.onrender.com/)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:a855f7,100:6366f1&height=100&section=footer" width="100%"/>

</div>