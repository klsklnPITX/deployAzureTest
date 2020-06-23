from flask import Flask
import appconfig
import funcs
from pytransform import pyarmor_runtime


app = Flask(__name__)
app.config.from_object(appconfig)

@app.route("/")
def home():
    output = funcs.myfunc("<h1>Output from pyc PYARMOR</h1>")
    return output

if __name__ == "__main__":
    app.run()