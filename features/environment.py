import os
import tempfile
from flaskr import app, init_db


def before_feature(context, feature):
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
    with app.app_context():
        init_db()


def after_feature(context, feature):
    os.close(context.db)
    os.unlink(app.config['DATABASE'])
