from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/film/<film>')
def show_film(film):
    return f'film: {film}'

@app.route('/film_id/<int:film_id>')
def show_film_id(film_id):
    return 'film_id: {}'.format(film_id) 

app.run('0.0.0.0', 5000, True)
