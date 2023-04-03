from flask import Flask, redirect, url_for, request, render_template, make_response, abort
from .views import index
from flask_bootstrap import Bootstrap5
from .models import db


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    # app.secret_key="klxjedj@ping997926."
    # app.config['WTF_CSRF_SECRET_KEY'] = 'a random string'
    app.config.from_object('hello.helloConfig')

    bootstrap = Bootstrap5(app)

    app.route('/', methods=['GET', 'POST'])(index.index)
    app.route('/index', methods=['GET', 'POST'])(index.index2)

    app.route('/study<group>', methods=['GET'])(index.study)
    app.route('/learn<group>', methods=['GET'])(index.learn)

    app.route('/welcome')(index.welcome)
    app.route('/api/<col>', methods=['PUT', 'GET', 'POST'])(index.api)
    app.route('/test', methods=['GET'])(index.test)
    app.route('/menu', methods=['GET'])(index.menu)
    return app


app = create_app()
db.init_app(app)
