from app.app import app, db
from models.models import Invoice, InvoiceItem
from routers.routers import create_invoice,add_invoice_item,get_invoices,get_invoice_items

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5000,debug=True)
