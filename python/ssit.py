from flask import Flask,url_for,redirect,render_template,render_template_string

app = Flask(__name__)

@app.route('/ssti')
def hello_world():
    return render_template('qing.html',string="qing qing qing")

if __name__ == '__main__':
    app.run()