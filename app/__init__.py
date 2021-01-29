from flask import Flask

app = Flask(__name__)
app.secret_key = "mysecretkey"

from app.routes import routes