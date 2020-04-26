from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
	files = ['iptables.txt', 'nmap.txt', 'misc.txt', 'php.txt', 'sshd.txt', 'sysctl.txt', 'pw.txt']
	descFiles = ['iptablesDesc.txt', 'nmapDesc.txt', 'miscDesc.txt', 'phpDesc.txt', 'sshdDesc.txt', 'sysctlDesc.txt', 'pwDesc.txt']
	selected = random.randint(0, len(files) - 1)
	with open("files/" + files[selected]) as f:
	    bloc = f.readlines()
	with open("files/" + descFiles[selected]) as f:
	    desc = f.readlines()
	return render_template("index.html", bloc=bloc, desc=desc)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
