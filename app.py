from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
	ran = random.randint(0, 2)
	files = ['files/iptables.txt', 'files/cyber.txt', 'files/misc.txt']
	descFiles = ['files/iptablesDesc.txt', 'files/cyberDesc.txt', 'files/miscDesc.txt']
	with open(files[ran]) as f:
	    bloc = f.readlines()
	with open(descFiles[ran]) as f:
	    desc = f.readlines()

	return render_template("index.html", bloc=bloc, desc=desc)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")