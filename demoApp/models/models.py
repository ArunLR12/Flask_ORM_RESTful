from app.app import app
from settings.settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from app.app import db

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    items = db.relationship('InvoiceItem', backref='invoice', lazy=True)

class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    units = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)