from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("staticPages/index.html",var1='toto')
@app.route("/about/")
def about():
	return render_template("staticPages/about.html")
@app.route("/tourdecontrol")
def tourdecontrol():
	timelines = ['This is the first event.',
                'This is the second event.',
                'This is the third event.'
                ]
	return render_template("boardPages/tourdecontrol.html",timelines=timelines)

if __name__ == '__main__':
	app.run(debug=True)