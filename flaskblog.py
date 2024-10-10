from flask import Flask, render_template, url_for

app = Flask(__name__)

posts  = [
    {
        'author': f"Author{i}",
        'title': f'Blog post {i}',
        'Content': f'content of  blog post {i}',
        'date_posted': f'April {i} 2018'
    }

    for i in range(1, 21)
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)