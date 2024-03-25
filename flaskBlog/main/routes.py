from flask import render_template, request, Blueprint
from flaskBlog.models import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    order = request.args.get("order", "latest", type=str)

    if order == "latest":
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(
            page=page, per_page=5
        )
    elif order == "oldest":
        posts = Post.query.order_by(Post.date_posted).paginate(page=page, per_page=5)

    return render_template("home.html", posts=posts, order=order)


@main.route("/about")
def about():
    return render_template("about.html", title="About")


@main.route("/latest_posts")
def latest_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(10).all()
    return render_template("latest_posts.html", posts=posts, title="Latest Posts")
