from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():
	return "loves contributing to ScoreLabb"

if __name__ == "__main__":
	app.run(debug=True, port=8080)