from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
        return '<p>Hello, World!</p>'
        <a href="/about">About page</a>
@app.route('/about')
def about():
        return '<p>This is an about page about the Flask web app running in a Linux VM.</p>'

if __name__ == '__main__':
        app.run(hosts=0.0.0.0', port=8080)
