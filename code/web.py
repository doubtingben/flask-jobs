from flask import Flask
from flask import request, redirect, url_for
import flask.ext.login as flask_login
from auth import User, users, login_manager

app = Flask(__name__)
app.debug = True
app.secret_key = 'EDREF238747828567285*^*$#%*^&(super secret string'

login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='pw' id='pw' placeholder='password'></input>
                <input type='submit' name='submit'></input>
               </form>
               '''

    email = request.form['email']
    if request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@app.route('/')
def main():
    return 'hi'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
