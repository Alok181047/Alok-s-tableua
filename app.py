import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Tableau Public views supplied by you.
VIEWS = {
    "story": {
        "label": "Story",
        "path": "Global_Olympic_Sports_Analysis_13/Story1",
    },
    "dashboard1": {
        "label": "Dashboard 1",
        "path": "Global_Olympic_Sports_Analysis_13/Dashboard1",
    },
    "dashboard2": {
        "label": "Dashboard 2",
        "path": "Global_Olympic_Sports_Analysis_13/Dashboard2",
    },
}

@app.route("/")
def index():
    selected = request.args.get("view", "story").lower()
    if selected not in VIEWS:
        selected = "story"

    # Tableau's /views/ URL is the standard embeddable URL for Tableau Public.
    tableau_url = (
        "https://public.tableau.com/views/"
        + VIEWS[selected]["path"]
        + "?:showVizHome=no&:embed=true&:toolbar=yes&:tabs=no"
    )
    return render_template(
        "index.html",
        views=VIEWS,
        selected=selected,
        tableau_url=tableau_url,
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)