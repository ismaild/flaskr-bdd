# Add flaskr to syspath

from behave import *

@given(u'flaskr is setup')
def flask_setup(context):
    assert context.client and context.db

@given(u'i login with "{username}" and "{password}"')
@when(u'i login with "{username}" and "{password}"')
def login(context, username, password):
    context.page = context.client.post('/login', data=dict(
        username=username,
        password=password
        ), follow_redirects=True)
    assert context.page

@when(u'i logout')
def logout(context):
    context.page = context.client.get('/logout', follow_redirects=True)
    assert context.page

@then(u'i should see the alert "{message}"')
def logged_in(context, message):
    assert message in context.page.data
