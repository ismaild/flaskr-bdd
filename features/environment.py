import os
import sys
import tempfile

# Set Path
pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
activate_this = os.path.join(new_path,'flaskr')
sys.path.append(activate_this)

from flaskr import app, init_db

def before_feature(context, feature):
    app.config['TESTING'] = True
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    context.client = app.test_client()
    init_db()


def after_feature(context, feature):
    os.close(context.db)
    os.unlink(app.config['DATABASE'])

