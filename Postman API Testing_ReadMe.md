# Testing the API through Postman


This API is available at "http://127.0.0.1:5000"

## Endpoints ##

### Create Invoice ###

POST '/create_invoice'

#### To test the add_invoice_item route using Postman, you can follow these steps ####:

* Open Postman.

* Select the request you're trying to send (e.g., the POST request to /create_invoice).
	Example:
		Method: POST
		URL: http://127.0.0.1:5000/create_invoice

#### Example ####
```
POST '/create_invoice'

Response Body Sample-
Invoice created successfully
  
```

### Add an item to the invoice ###

POST '/api/invoice/<int:invoice_id>/invoice_item'

Gives the feasibility to add an item to the previously created Invoice ID.

Mandatory Query Parameter:
- id: ID of the created invoice (integer type)

#### To test the add_invoice_item route using Postman, you can follow these steps ####:

* Open Postman

* Select POST Method:
	Create a new request in Postman and make sure to select the POST method.

* Set Request URL:
	Enter the URL for the add_invoice_item route, replacing {{ invoice_id }} with the actual invoice ID. For example: http://127.0.0.1:5000/api/invoice/8/invoice_item.

* Set Request Body:
	In the request body section, select the "x-www-form-urlencoded" option. This is because the add_invoice_item route is using "request.form" to retrieve data, which corresponds to form data.

* Add Form Data:
	Add the required form data for the invoice item. You'll need to provide values for units, description, and amount.

* Send Request:
	Click the "Send" button to send the POST request to the add_invoice_item route.

* Example of how your Postman setup might look:

	Method: POST
	URL: http://127.0.0.1:5000/api/invoice/8/invoice_item
	Headers: None
	Body (x-www-form-urlencoded):
	Key: units, Value: 10
	Key: description, Value: Item description
	Key: amount, Value: 100

#### Example ####
```
POST '/api/invoice/8/invoice_item'

Request Body Sample-

Body Format: x-www-form-urlencoded

    'units': "78",
    'description': "Sample",
    'amount': 5
	
Response Body Sample-
Invoice item added successfully
  
```

### GET the invoice details ###

GET '/invoices'

Return the details of the all invoices in a JSON format, as well of the items nested with the invoice.

#### To test the add_invoice_item route using Postman, you can follow these steps ####:

* Open Postman:

* Create a New Request:
	Create a new request by clicking the "+ New" button or selecting "New Request" from the File menu.

* Select Request Type:
	In the request panel, select the appropriate request type. In this case, select "GET."

* Enter Request URL:
	Enter the URL for the get_invoices route. For example: http://127.0.0.1:5000/invoices

* Send the Request:
	Click the "Send" button to send the GET request to your Flask app.

* View Response:
	Once you've sent the request, you should see the response in the lower part of the Postman interface.

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

#### To test the add_invoice_item route using Postman, you can follow these steps ####:

* Open Postman:

* Create a New Request:
	Create a new request by clicking the "New" button and selecting "Request".

* Set Request Type and URL:
	Set the request type to GET and enter the URL for the get_invoice_items route. Replace {{ invoice_id }} with the actual invoice ID you want to retrieve items for. 
	Example: http://127.0.0.1:5000/api/invoice/<int:invoice_id>/invoice_items

* Send the Request:
	Click the "Send" button to send the GET request to the specified URL.

#### Example ####

```
GET api/invoice/8/invoice_items

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
