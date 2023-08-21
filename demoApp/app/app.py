from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
from settings.settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI, DEBUG

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)