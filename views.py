from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from HelloWorld.form import BookmarkForm, LoginForm
from HelloWorld import app, db
from HelloWorld.models import User, Bookmark
from flask_login import login_required, login_manager

bookmarks = []


# fake login
# def logged_in_user():
#     return User.query.filter_by(username='ww').first()


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title="Title passes via Jinja",
        text="Text passed via Jinja",
        # new_bookmarks=new_bookmarks(5))
        new_bookmarks=Bookmark.newest(5))


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    # import pdb; pdb.set_trace()
    # print(form.jedUrl)
    if form.validate_on_submit():
        url = form.jedUrl.data
        description = form.description.data
        bm = Bookmark(
            user=logged_in_user(),
            url=url,
            description=description)
        db.session.add(bm)
        db.session.commit()
        # store_bookmark(url, description)
        flash('Stored bookmark: '+url)
        return redirect(url_for('index'))
    else:
        print("False Bro")
    return render_template('add.html', form=form)


@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user, form.remember_me.data)
            flash("Logged in successfully as {}".format(user.username))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password.')
    return render_template("login.html", form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server(e):
    return render_template('500.html'), 500


# def new_bookmarks(num):
#     return sorted(
#         bookmarks,
#         key=lambda bm: bm['date'],
#         reverse=True
#     )[:num]


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description=description,
        user="reindert",
        date=datetime.utcnow()
    ))


if __name__ == "__main__":
    app.run(debug=True)
