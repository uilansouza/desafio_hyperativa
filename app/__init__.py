from flask import Flask, jsonify

app = Flask(__name__)

from .model import Card, Usuario
from .controllers import ApiUserController, ApiCardController, ApiUserController
from .routes import routes
