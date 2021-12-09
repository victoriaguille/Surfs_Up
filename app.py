

#import the dependency
from flask import Flask

#create a new flask app instance
app = Flask(__name__)

#create first flask route
@app.route("/")
def hello_world():
    return "Hello World"
# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
