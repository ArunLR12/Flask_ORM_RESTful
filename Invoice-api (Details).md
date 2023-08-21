# Invoice API

This API allows you to create an invoice, add an item to the Invoice

This API is available at "http://127.0.0.1:5000"

## Endpoints ##

### Create Invoice ###

POST '/create_invoice'

Creates the invoice with a new Invoice ID.

#### Example ####
```
POST '/create_invoice'

Expected Response Sample-

Invoice created successfully (on Postman Interface)  
```

### Add an item to the invoice ###

POST '/api/invoice/<int:invoice_id>/invoice_item'

Gives the feasibility to add an item to the previously created Invoice ID.

Mandatory Query Parameter:
- id: ID of the created invoice (integer type)

#### Example ####
```
POST '/api/invoice/8/invoice_item'

Request Body Sample-

Body Format: x-www-form-urlencoded

    'units': "78",
    'description': "Sample",
    'amount': 5
  
```

### GET the invoice details ###

GET '/invoices'

Return the details of the all invoices in a JSON format

#### Example ####

```
GET /invoices/

Response Body Sample-

[
  {
    "date": "2023-08-17",
    "id": 1,
    "items": [
      {
        "amount": "100",
        "description": "Item 1",
        "id": 1,
        "units": 5
      },
      {
        "amount": "50",
        "description": "Item 2",
        "id": 2,
        "units": 3
      },
      {
        "amount": "450",
        "description": "Order_line_item",
        "id": 3,
        "units": 200
      }
    ]
  }
```

### GET a specific invoice details ###

GET '/api/invoice/<int:invoice_id>/invoice_items'

GET the details of a specific invoice in a JSON return format

#### Example ####

```
GET /api/invoice/8/invoice_items

Response Body Sample-

[
  {
    "amount": "78",
    "description": "YML",
    "id": 5,
    "units": 5
  },
  {
    "amount": "78",
    "description": "YML",
    "id": 6,
    "units": 5
  }
]
```
