from flask import Flask, redirect, Response
from config import Config
import os

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config())

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	app.add_url_rule('/favicon.ico', view_func=handle_icon)

	return app

def handle_icon():
	return redirect('static/favicon.ico')
