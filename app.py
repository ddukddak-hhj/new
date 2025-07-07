from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333333;
                margin-bottom: 10px;
            }
            p {
                color: #666666;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Hello from DevOps!</h1>
            <p>This site is automatically deployed via GitHub Actions & Docker.</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
