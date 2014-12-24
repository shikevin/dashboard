from flask import Flask, flash, render_template

app = Flask(__name__)
app.secret_key = 'set_secret_key'

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    if (name=='tony'):
        return render_template('tony.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
