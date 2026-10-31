# Global Olympic Sports Analysis – Flask + Tableau

## Files
- `app.py`: Flask application and view routing
- `templates/index.html`: responsive page with Story / Dashboard 1 / Dashboard 2 tabs
- `requirements.txt`: Python dependencies
- `Procfile`: Render start command
- `runtime.txt`: Python runtime

## Run locally
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Deploy on Render
1. Push these files to a GitHub repository.
2. In Render, choose **New + → Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Choose a free/appropriate instance and deploy.

The Tableau views must be published and publicly embeddable on Tableau Public.
