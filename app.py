from flask import Flask, render_template, request
from validator import validate_markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    issues = []
    if request.method == "POST":
        file = request.files["file"]
        if file:
            content = file.read().decode("utf-8")
            
            # save temp file
            with open("temp.md", "w", encoding="utf-8") as f:
                f.write(content)

            issues = validate_markdown("temp.md")

    return render_template("index.html", issues=issues)

if __name__ == "__main__":
    app.run(debug=True)
