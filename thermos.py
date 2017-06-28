from flask import Flask, render_template, url_for, request, redirect, flash
import logging
from datetime import datetime
from form import BookmarkForm
# from flask_wtf import Form
# from wtforms.fields import StringField
# from flask_wtf.html5 import URLField
# from wtforms.validators import DataRequired, url


app = Flask(__name__)

app.config['SECRET_KEY'] = b'U[\ty\x0e\xbe\x83a\xe3\xa9\x19\x13\xf2\xfcOB;\x10~\xbd~\xfc`\xac'
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
    print(form.jedUrl)
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


# def BookmarkForm():
#     url2 = URLField('url', validators=[DataRequired(), url()])
#     description = StringField('description')

if __name__ == "__main__":
    app.run(debug=True)
