import logging
import os
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from form import BookmarkForm
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = b'U[\ty\x0e\xbe\x83a\xe3\xa9\x19\x13\xf2\xfcOB;\x10~\xbd~\xfc`\xac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

# toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

bookmarks = []


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        title="Title passes via Jinja",
        text="Text passed via Jinja",
        new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    # import pdb; pdb.set_trace()
    # print(form.jedUrl)
    if form.validate_on_submit():
        url = form.jedUrl.data
        description = form.description.data
        store_bookmark(url, description)
        flash('Stored bookmark: '+url)
        return redirect(url_for('index'))
    else:
        print("False Bro")
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server(e):
    return render_template('500.html'), 500


def new_bookmarks(num):
    return sorted(
        bookmarks,
        key=lambda bm: bm['date'],
        reverse=True
    )[:num]


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description=description,
        user="reindert",
        date=datetime.utcnow()
    ))


if __name__ == "__main__":
    app.run(debug=True)
