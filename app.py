from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Module 3 Cloud Web App</title>
        </head>
        <body>
            <h1>Welcome to My Cloud Web Application</h1>
            <p>Module 3 - Cloud Services & Web App Deployment</p>
            <p>Built using Python and Flask.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)