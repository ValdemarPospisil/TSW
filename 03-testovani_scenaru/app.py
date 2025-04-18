from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/api/author')
def api_author():
    return jsonify({'author': 'John Doe'})

if __name__ == '__main__':
    app.run(port=8050, debug=True)
