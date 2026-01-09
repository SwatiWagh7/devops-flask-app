from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps CI/CD Auto Deployment</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            color: #333;
        }
        header {
            background: #0f172a;
            color: white;
            padding: 20px;
            text-align: center;
        }
        section {
            max-width: 900px;
            margin: auto;
            padding: 40px;
        }
        .card {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        h2 {
            color: #0f172a;
        }
        footer {
            background: #0f172a;
            color: white;
            text-align: center;
            padding: 15px;
            font-size: 14px;
        }
        .highlight {
            color: #2563eb;
            font-weight: bold;
        }
    </style>
</head>
<body>

<header>
    <h1>🚀 DevOps CI/CD Auto Deployment</h1>
    <p>Python Flask | Jenkins | Docker | Kubernetes</p>
</header>

<section>

    <div class="card">
        <h2>📌 Project Overview</h2>
        <p>
            This Python Flask application demonstrates a complete
            <span class="highlight">CI/CD automation workflow</span>
            using modern DevOps tools.
        </p>
    </div>

    <div class="card">
        <h2>⚙️ Tools Used : </h2>
        <ul>
            <li>Git – Source Code Management</li>
            <li>Jenkins – CI/CD Automation</li>
            <li>Docker – Containerization</li>
            <li>Container Registry – Image Storage</li>
            <li>Kubernetes – Orchestration</li>
        </ul>
    </div>

    <div class="card">
        <h2>🔁 Deployment Information</h2>
        <p>
            This application was <span class="highlight">automatically deployed</span>
            using a Jenkins pipeline.
        </p>
        <p>
            Deployment Time: {{ deploy_time }}
        </p>
    </div>

</section>

<footer>
    © 2026 | DevOps Intern Project
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML_TEMPLATE,
        deploy_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

