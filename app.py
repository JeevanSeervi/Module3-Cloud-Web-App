import os
from flask import Flask

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "development")

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Module 3 Cloud Web App</title>
        </head>
        <body>
            <h1>Welcome to My Cloud Web Application</h1>
            <p>Module 3 - Cloud Services & Web App Deployment</p>
            <p>Built using Python and Flask.</p>
            <p>Environment: {APP_ENV}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)