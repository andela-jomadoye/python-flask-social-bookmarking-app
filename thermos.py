from flask import Flask, render_template, url_for, request, redirect, flash
# from logging import DEBUG
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = b'U[\ty\x0e\xbe\x83a\xe3\xa9\x19\x13\xf2\xfcOB;\x10~\xbd~\xfc`\xac'
bookmarks = []


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title passes via Jinja",
    text="Text passed via Jinja")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash('Stored bookmark: '+url)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server(e):
    return render_template('500.html'), 500


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user="reindert",
        date=datetime.utcnow()
    ))

if __name__ == "__main__":
    app.run(debug=True)

