from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/')
def index():
    """Main"""
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    """Welcome))"""
    name = request.form['name']
    email = request.form['email']

    response = make_response(redirect('/greet'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)

    return response


@app.route('/greet')
def greet():
    """Greet"""
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('greet.html', name=user_name)
    return redirect('/')


@app.route('/logout')
def logout():
    """Logout"""
    response = make_response(redirect('/'))
    response.set_cookie('user_name', '', expires=0)
    response.set_cookie('user_email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
