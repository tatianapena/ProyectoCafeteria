from flask import Flask, render_template, flash, request

import validate

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/register')
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            error = None

            if not validate.isUsernameValid(username):
                print('El usuario no es correcto')
                error = "El usuario debe ser alfanumérico"
                flash(error)
                return render_template('register.html')

            if not validate.isEmailValid(email):
                error = "Correo inválido"
                flash(error)
                return render_template('register.html')

            if not validate.isPasswordValid(password):
                error = "La contraseña debe tener por lo menos una mayúscula y una minúscula y 8 caracteres"
                flash(error)
                return render_template('register.html')

            return render_template('search.html')
        return render_template('register.html')
    except Exception as e:
        print("Ocurrió un error:", e)
        return render_template('register.html')


@app.route('/change')
def change_password():
    return render_template('change.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == '__main__':
    app.run()