from flask import Flask, render_template
import requests

app = Flask(__name__)

# Get the API data
URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=URL)
response_info = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=response_info)


# Dynamic route where the <int:post_id> captures the post ID from the URL.
# Allows Flask to identify which blog post to display based on the post's unique ID.
@app.route("/post/<int:post_id>")
def post(post_id):
    # requested_post will hold the specific blog post that matches the post_id from the URL.
    requested_post = None
    for post in response_info:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
