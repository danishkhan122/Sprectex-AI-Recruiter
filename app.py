from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/jobs")
def jobs():
    return render_template("job_position.html")

@app.route("/candidates")
def candidates():
    return render_template("candidates.html")

@app.route("/ats")
def ats():
    return render_template("ats.html")

@app.route("/ai-interview")
def ai_interview():
    return render_template("ai_interview.html")

@app.route("/pipeline")
def pipeline():
    return render_template("pipeline.html")

@app.route("/tools")
def tools():
    return render_template("tools.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)
