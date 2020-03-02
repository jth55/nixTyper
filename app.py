from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
	ran = random.randint(0, 2)
	files = ['files/iptables.txt', 'files/script.txt', 'files/misc.txt']
	with open(files[ran]) as f:
	    bloc = f.readlines()

	return render_template("index.html", bloc=bloc)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
