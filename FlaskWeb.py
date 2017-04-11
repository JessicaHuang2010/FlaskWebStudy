from flask import Flask, render_template
# from flask_script import Manager
from flask_bootstrap import Bootstrap

# http://jinja.pocoo.org/docs/templates/#builtin-filters

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    # return '<h1>Hello World!</h1>
        return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello,%s!</h1>' % name
        return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
