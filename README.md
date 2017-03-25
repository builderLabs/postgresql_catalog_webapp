### INTRODUCTION


This collection of scripts is a web application developed in Python which uses  
the Flask web framework and a persistent PostgreSQL back-end along with  
basic HTML form elements and JavaScript to demonstrate a web application which  
performs common database operations.  

This project differs from its SQLite-backed variant in that it incorporates a  
persistent database and involved procuring a bare-bones Linux server which has  
been configured from scratch to host the application.  The deployed version of this  
app can be found [here](http://50.116.53.185/).  

As a result, instructions for this project *in its entirey* have been created in  
the following three documents:

1). Provisioning and configuration of a Linux server from scratch: [LinuxSrvCfg.md](https://github.com/builderLabs/psql_catalog/blob/master/LinuxSrvCfg.md).  
2). Configuration and setup of the project on the server: [CatalogCfg.md](https://github.com/builderLabs/psql_catalog/blob/master/CatalogCfg.md).  
3). Finally, application-specific instructions/guidance: [(this document)](https://github.com/builderLabs/psql_catalog/blob/master/README.md).  

To replicate this project in its entirety, follow the instructions listed in  
the guides listed above (documents 1 and 2 - in that order) before cloning this  
project to your destination repository.  
&emsp;  
**Pertinent Information:**  
Server IP address: 50.116.53.185  
SSH port: 2200  
Application URL: http://50.116.53.185/
&emsp;  

### DESCRIPTION

The application is for a fictional store called "The Instrument Garage" which  
lists the new and used musical instruments members might have to offer or  
trade (buy/sell) with one another.  

Functionality on the site depends on user registration/logged-in status which  
is handled through 3rd party OAuth 2.0 authorization for security purposes.  

Taken together, this project demonstrates the following key aspects of  
fullstack development:

#### Application Setup:  
-setup and configuration of a **bare-bones Linux server** (including setting basic  
&nbsp;security measures and configuring the firewall)  
-installation and configuration of **Apache2 server**  
-configuration of a new **Apache virtual host**  
-installation and configuration of the apache Web Server Gateway Interface  
&nbsp;module: **mod_wsgi**  
-installation and configuration of **PostgreSQL**  
-installation and configuration of the **Python virtual environment**: *virtualenv*  
-the setup of all Python dependencies for our project in the virtual environment  


#### Project-Specific:

-use of the versatile **Flask** framework and the **SQLAlchemy ORM**  
-database create/read/update/delete operations (CRUD)  
-basic **RESTful API** endpoints to access application data in **JSON/XML**  
-industry-standard **OAuth 2.0** 3rd-party authorization (via **Google Sign-In**)  
-standard **SQL queries** crafted for the PostgreSQL database engine  
-data integrity operations and navigational/error-checking logic  
-some **JavaScript** for controlling client-side form behavior  


### APPLICATION DEPENDENCIES

This application is developed in Python 2.7.x and makes use of the following  
modules/libraries:  

-python 2.7.x: random, string, httplib2, json, requests  
-flask: flash, jsonify  
-sqlalchemy: asc, create_engine, func  
-sqlalchemy.orm: sessionmaker  
-oauth2client.client: flow_from_clientsecrets, FlowExchangeError  

Database definitions for the fictional datbase reside in the script create_db.py  
from which the following customized components must also be imported after the  
database has been initialized (created and populated):  

-create_db: Base, User, Category, Subcategory, Brand, Instrument  
-instrumentgarage.db (sqlite database created per instructions below)

## SITE USAGE:

*(Note: to replicate the project, refer to the instructions and help guides  
listed in the introduction)*  

**Navigation Basics**

The main page lists categories of musical instruments which may be clicked  
on to list individual instruments in the category.  As an alternative, users  
may also view instruments as listed by brand,  similar to the display alternative  
many online music retailers also offer.

Clicking on either a brand or a category heading will return a listing of the  
instruments available in either that category or brand.  The entries which  
appear here are summarizes/highlights of the instrument entries for which more  
detail may be accessed by following the 'More' link under each instrument.

Clicking on a 'More' link will render a full page dedicated to that particular  
instrument with full descriptive details including postage by user.

Instrument-page functionality is restricted to viewing-only if the user is  
either not registered or not logged-in.  Registering and/or logging-in gives  
the user the ability to post/edit/delete instrument listings.

Registration and sign-in is done via OAuth 2.0 using Google sign-in and new  
users are added to the user database based on authorizations agreed to by the  
client.

Posting functionality is made available to any signed-in user.  However,  
editing/deleting functionality is restricted to original posters of the  
respective items with a confirmation page used for deletions.  

A token 'Purchase' button reveals the contact information of the poster of  
the item (which in production would likely require an agreement in terms of  
use or be otherwise centrally handled for privacy purposes).


**Posting/Editing Items**

A category-subcategory parent-child relationship is enforced during  
the posting/editing process such that the specified subcategory for the posting  
(pianos) must be a child of the specified parent category (keyboards).  

Required fields are annotated with an asterisk on the posting page and include  
category, subcategory, brand, and condition.  The fields model, description, and  
price are optional for posting/editing purposes.

Errors are raised when any combination of missing required fields are 
not provided.  

In addition to the pre-canned categories/subcategories and instruments which  
come with the initial database, custom categories/subcategories/brands may be  
added.  Error checks are performed in these instances as well, to ensure  
data integrity/consistency.

Enjoy the demo project!
