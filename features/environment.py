from os.path import abspath, dirname, join
import os
import sys
import tempfile

# Set Path
app_path = join(dirname(dirname(abspath(__file__))), 'flaskr')
sys.path.append(app_path)

from flaskr import app, init_db


def before_feature(context, feature):
    app.config['TESTING'] = True
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    context.client = app.test_client()
    init_db()


def after_feature(context, feature):
    os.close(context.db)
    os.unlink(app.config['DATABASE'])
