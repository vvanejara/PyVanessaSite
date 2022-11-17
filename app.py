from flask import Flask , render_template
app = Flask(__name__)

# def readDetails(filepath):
#     with open(filepath, 'r') as f:
#         return [line for line in f]

@app.route('/')
def homePage():
   name = "Vanessa Jara"
   #details = readDetails('static/details.txt')
   return render_template("base.html", name=name)

   #lol