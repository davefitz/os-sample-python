from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! \n"

@application.route("/ready")
def hello():
    return "I am Ready! \n"

@application.route("/health")
def hello():
    return "I am Healthy! \n"

if __name__ == "__main__":
    application.run()
