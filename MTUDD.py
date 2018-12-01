from flask import Flask, render_template
from MDD import disc

app = Flask(__name__)

@app.route('/')
def index():
	output = disc()
	return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)