from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/<name>")
def hello_person(name):
    return render_template('hello_person.html', uname=name)


@app.route("/<first>/<second>")
def jedi(first,second):
    jedi=second[0:3]+first[0:2]
    return render_template('jedi.html', jedi=jedi)
    
    
if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=8080)