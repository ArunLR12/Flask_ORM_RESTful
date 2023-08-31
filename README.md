# Flask_ORM_RESTful
An app to show the implementation of Flask framework, SQLAlchemy and REST API. It also gives the demonstration of testing this with Postman.

## Description ##

We have added two models in the code 'Invoice' and 'InvoiceItem'. When framework is started, the webpage opens and the 'Invoice' is created for the first time and the page gets re-directed to the 'Add Invoice Item'. Post this, we have also implemented the functionality of 'View Invoice' and the web page gets re-directed to this 'view invoice' where the currently added invoice is displayed. We have also demonstrated the usage of Restful API through some endpoints leveraging the GET method.

### Tech-Stack Used ###

* HTML

* Flask Framework

* ORM- SQLAlchemy

* DB: MySQL

* Language: Python & OOPS concept

* API Client Used (for tetsing): Postman

## Dependencies ##

* Download and install MySQL (Link: https://dev.mysql.com/downloads/installer/) with all the required configurations.
  
* Install python
  
* Install flask, flask_sqlalchemy (Commands written below)
  
  * pip install flask
    
  * pip install sqlalchemy
    
  * pip install flask-sqlalchemy

* Download and install Postman (You can download and install it from the official website)

## Instruction to run docker file ##

Go to main working directory where the 'docker-compose.yml' and 'Dockerfile' is located and run the below mentioned command:

* docker-compose up
