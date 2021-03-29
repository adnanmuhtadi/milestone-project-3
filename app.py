import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# This tells the application where and how to run.
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)