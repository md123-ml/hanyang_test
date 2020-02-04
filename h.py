from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('h.html')

@app.route('/htaling')
def htaling():
    return render_template('htaling.html')
@app.route('/hhobbybox')
def hhobbybox():
    return render_template('hhobbybox.html')
@app.route('/hconects')
def hconects():
    return render_template('hconects.html')
@app.route('/hclass101')
def hclass101():
    return render_template('hclass101.html')

if __name__=='__main__':
    app.run()