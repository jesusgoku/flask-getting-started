from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

if __name__ == '__main__':
    app.run()
