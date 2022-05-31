from flask import Blueprint, render_template, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
	current_app.logger.info("INFO level")
	return redirect(url_for('question._list'))
