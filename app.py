from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return ('index.html')

@app.route('/page')
def page():
    return ("Pages page 5.0")

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
