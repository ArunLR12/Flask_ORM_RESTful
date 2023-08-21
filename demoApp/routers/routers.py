from app.app import app,db,date
from models.models import Invoice, InvoiceItem
from settings.settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from app.app import jsonify,request



@app.route('/create_invoice', methods=['POST'])
def create_invoice():
    data = request.json  # JSON data has to be sent in the request body
    provided_invoice_id = data.get('invoice_id')  # Extract custom invoice ID

    # Check if the provided invoice ID already exists
    existing_invoice = Invoice.query.get(provided_invoice_id)
    if existing_invoice:
        return "Invoice ID already exists"

    new_invoice = Invoice(id=provided_invoice_id, date=date.today())
    db.session.add(new_invoice)
    db.session.commit()
    return "Invoice created successfully"
    

@app.route('/add_invoice_item/<int:invoice_id>', methods=['POST'])
def add_invoice_item(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return "Invoice not found", 404  # Return a 404 status code for not found
    
    if request.method == 'POST':
        print(request.form)
        data = request.form
        item = InvoiceItem(
            units=data['units'],
            description=data['description'],
            amount=data['amount'],
            invoice=invoice
        )
        db.session.add(item)
        db.session.commit()
        
        return "Invoice item added successfully", 201 
    
    return "Invalid request", 400


#Below 2 functions are created for some endpoints to demonstrate and GET the created data. It demonstrates RESTful API.

@app.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    invoice_list = []
    for invoice in invoices:
        invoice_list.append({
            'id': invoice.id,
            'date': invoice.date.strftime('%Y-%m-%d')
        })
    return jsonify(invoice_list)

@app.route('/invoice_items/<int:invoice_id>', methods=['GET'])
def get_invoice_items(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return "Invoice not found"
    
    items = invoice.items
    item_list = []
    for item in items:
        item_list.append({
            'id': item.id,
            'units': item.units,
            'description': item.description,
            'amount': str(item.amount)
        })
    return jsonify(item_list)