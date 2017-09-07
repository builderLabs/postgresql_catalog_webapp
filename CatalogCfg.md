# Overview 

The item catalog project as deployed to a provisioned Linux server is a  
two-part project, the first of which involved the provision and setup of  
a bare-bones Linux server.  Detailed instructions for this part of the  
project may be found [here](https://github.com/builderLabs/psql_catalog/blob/master/LinuxSrvCfg.md).  
&emsp;  
The instructions below pertain to the second-part of the project - namely,  
the deployment of the item catalog web application to the newly provisioned  
server.  In order for the catalog item project to be deployed successfully, a  
number of packages need to be installed on our freshly provisioned Linux  
server.   
&emsp;  
Required installations can be divided up into system/site-wide packages  
and project-specific packages. For project-specific packages, we will  
install a Python Virtual Environment which will have all the necessary  
modules installed for running our particular application.  
&emsp;  

# I. Catalog Project - Required System Packages Setup  
&emsp;  
A). INSTALL APACHE2 SERVER:  
&emsp;&emsp;`sudo apt-get install apache2`

&emsp;&emsp;1). Installation generally automatically starts apache server.  
&emsp;&emsp;To test this, type the following command:  
&emsp;&emsp;`ps -ef | grep www`  
&emsp;    
&emsp;&emsp;Process names 'www-data' indicate apache daemons are running.  
&emsp;&emsp;If nothing is returned, use the following command to start the service:  
&emsp;&emsp;`sudo service apache2 start`  
&emsp;  
You can check to see if apache is serving the default web page by  
accessing our server and the default http port 80:  
&emsp;  
http://12.345.67.890:80
&emsp;  
If you see the apache welcome page with the words 'It works!' - it's up  
and running.  
&emsp;  
B). INSTALL THE APACHE WSGI MODULE:  
&emsp;  
&emsp;`sudo apt-get install libapache2-mod-wsgi`  
&emsp;  
&emsp;&emsp;a). Generally, the mod_wsgi is enabled after installation by default.  
&emsp;&emsp;&emsp;If not, the following command will enable it:  
&emsp;&emsp;&emsp;`sudo a2enmod wsgi`  
&emsp;  
C). INSTALL POSTGRESQL:  
&emsp;&emsp;`sudo apt-get install postgresql`  
&emsp;  
&emsp;&emsp;a). Check that PostgreSQL is up and running:  
&emsp;&emsp;&emsp;`ps -ef | grep post`  
&emsp;  
&emsp;&emsp;&emsp;this should return several lines with 'postgres'.  
&emsp;  
&emsp;&emsp;1). Configure PostgreSQL:  
&emsp;  
&emsp;&emsp;&emsp;a). Secure usage of our database: start off by creating a  
&emsp;&emsp;&emsp;non-standard root user other than postgres:  
&emsp;  
&emsp;&emsp;&emsp;Switch to psql root user:  
&emsp;&emsp;&emsp;`sudo su - postgres`  
&emsp;  
&emsp;&emsp;&emsp;launch application:  
&emsp;&emsp;&emsp;`psql`  
&emsp;  
&emsp;&emsp;&emsp;create a new user other than 'postgres':    
&emsp;&emsp;&emsp;`CREATE USER catuser WITH PASSWORD 'dbpass';`  
&emsp;  
&emsp;&emsp;&emsp;grant database creation permission to this user:  
&emsp;&emsp;&emsp;`ALTER USER catuser CREATEDB;`  
&emsp;   
&emsp;&emsp;&emsp;create our database:  
&emsp;&emsp;&emsp;`CREATE DATABASE instrumentgarage WITH OWNER catuser;`  
&emsp;  
&emsp;&emsp;&emsp;change to database to test existence:  
&emsp;&emsp;&emsp;`\c instrumentgarage;`  
&emsp;  
&emsp;&emsp;&emsp;grant rights and permissions to this user:  
&emsp;&emsp;&emsp;`REVOKE ALL ON SCHEMA public FROM public;`  
&emsp;&emsp;&emsp;`GRANT ALL ON SCHEMA public TO catuser;`  
&emsp;  
&emsp;&emsp;&emsp;finally, logout:  
&emsp;&emsp;&emsp;`\q`  
&emsp;  
&emsp;&emsp;&emsp;and exit postgres profile:  
&emsp;&emsp;&emsp;`exit`  
&emsp;  
&emsp;&emsp;&emsp;b). Check the PostgreSQL configuration file to ensure no remote  
&emsp;&emsp;&emsp;&emsp;connections are enabled. This is the default when installing  
&emsp;&emsp;&emsp;&emsp;PostgreSQL in Ubuntu.  
&emsp;&emsp;&emsp;&emsp;`sudo vim /etc/postgresql/9.5/main/pg_hba.conf`  
&emsp;  
&emsp;&emsp;&emsp;&emsp;towards the bottom you should see the actual configurations table.  
&emsp;&emsp;&emsp;&emsp;It's header begins with the following:  
&emsp;&emsp;&emsp;&emsp;`TYPE-DATABASE-USER-ADDRESS-METHOD`  
&emsp;  
&emsp;&emsp;&emsp;&emsp;The last two entries starting with the word 'host' indicate remote  
&emsp;&emsp;&emsp;&emsp;connections.  So long as these point to our localhost with the values    
&emsp;&emsp;&emsp;&emsp;similar to the following for column ADDRESS:  
&emsp;&emsp;&emsp;&emsp;`127.0.0.1/32 & ::1/128`  
&emsp;&emsp;&emsp;&emsp;we have no remote connections enabled.  
&emsp;  
&emsp;&emsp;&emsp;&emsp;*(If you see other values here, edit them to point to the localhost).*  
&emsp;  
D). INSTALL GIT:  
&emsp;We will need to install git on our server as we will be cloning this repository to it:  
&emsp;`sudo apt-get install git`  

# II. Project-Specific Packages:
&emsp;  
A). INSTALL & CONFIGURE PYTHON VIRTUAL ENVIRONMENT:  
&emsp;  
&emsp;&emsp;1). Install the Python package installer pip:  
&emsp;&emsp;`sudo apt-get install python-pip`  
&emsp;  
&emsp;&emsp;2). Install the Python virtual environment installer:  
&emsp;&emsp;`sudo -H pip install virtualenv`  
&emsp;  
&emsp;&emsp;3). Make the project directory, navigate to it, and create the virtual  
&emsp;&emsp;python environment in that location:  
&emsp;&emsp;`cd /var/www`  
&emsp;&emsp;`sudo mkdir catalog`  
&emsp;  
&emsp;&emsp;change permissions so that user 'grader' owns it:  
&emsp;&emsp;`sudo chown -R grader:grader catalog`  
&emsp;  
&emsp;&emsp;now let's create our python virtual environment in the project  
&emsp;&emsp;directory:  
&emsp;&emsp;`cd /var/www/catalog`  
&emsp;&emsp;`sudo virtualenv venv`  
&emsp;  
&emsp;&emsp;now launch/activate the virtual environment:  
&emsp;&emsp;`source venv/bin/activate`  
&emsp;  
&emsp;&emsp;This will create the virtual environment folder: 'venv'  
&emsp;&emsp;Allow read/write/execute permissions on this directory:  
&emsp;&emsp;`sudo chmod -R 777 venv`  
&emsp;  
&emsp;&emsp;Since we have activated the virtual environment, at this point we should  
&emsp;&emsp;be executing all commands within the environment. This should be obvious  
&emsp;&emsp;as our command line should be prefaced with (venv), as in:  
&emsp;&emsp;`(venv) grader@localhost:/var/www/catalog`  
&emsp;  
&emsp;&emsp;4). This means that we can now install any/all required packages and  
&emsp;&emsp;&emsp;dependencies for the catalog project at hand.
&emsp;  
&emsp;&emsp;&emsp;Let's start off installing flask:  
&emsp;&emsp;&emsp;`pip install Flask`  
&emsp;  
&emsp;&emsp;&emsp;and now for the remaining dependencies which are as follows for this  
&emsp;&emsp;&emsp;particular web application:  
```
pip install httplib2, oauth2client, psycopg2, requests, sqlalchemy, sqlalchemy_utils
```
&emsp;  
B). GIT CLONE PROJECT  
&emsp;  
With our Python virtual environment setup and our dependencies/required  
packages installed, we now need to import this project:  
`git clone https://github.com/builderLabs/psql_catalog.git`  
&emsp;  
&emsp;1). Modify project configurations to match our new environment.  
&emsp;  
&emsp;&emsp;a).Update the location of the client_secrets file to reflect our  
&emsp;&emsp;&emsp;current directory structure  
&emsp;&emsp;&emsp;`cd /var/www/catalog/psql_catalog`  
&emsp;&emsp;&emsp;`sudo vim catalog.py`  
&emsp;  
&emsp;&emsp;&emsp;search and replace any lines with 'client_secrets' in it to read the  
&emsp;&emsp;&emsp;absolute path to our client_secrets.json file (under psql_category) like so:  
&emsp;&emsp;&emsp;`/var/www/catalog/psql_catalog/client_secrets.json`  
&emsp;  
&emsp;2). Setup the project:  
&emsp;  
&emsp;&emsp;a). First, we'll need to create our project database:  
&emsp;&emsp;&emsp;`cd psqlsql_catalog`  
&emsp;&emsp;&emsp;`python create_db.py`  
&emsp;  
&emsp;&emsp;b). Now seed the database tables with data in the initData module:  
&emsp;&emsp;&emsp;`python populate_db.py`  
&emsp;  
&emsp;&emsp;We should now have our project database instrumentgarage setup and  
&emsp;&emsp;populated in PostgreSQL on our server.  
&emsp;  
C). CONFIGURE A NEW VIRTUAL HOST FOR APACHE TO SERVE  
&emsp;  
Now we need to set up the requirements for hosting our web application  
via Apache server with our newly setup database at the back-end.  
&emsp;  
&emsp;1). First, create a *.wsgi file which governs execution of our project scripts.  
&emsp;  
&emsp;&emsp;Our git clone already includes such a script but we need to edit it to ensure  
&emsp;&emsp;its contents match those of our current environment.  
&emsp;&emsp;`cd /var/www/catalog/psql_catalog`  
&emsp;&emsp;`vim controller.wsgi`  
&emsp;  
&emsp;&emsp;change the line:  
&emsp;&emsp;`sys.path.insert(0,"/var/www/html/")`  
&emsp;  
&emsp;&emsp;to read:  
&emsp;&emsp;`sys.path.insert(0,"/var/www/catalog/psql_catalog/")`  
&emsp;  
&emsp;&emsp;and save and quit  
&emsp;&emsp;`:wq`  
&emsp;  
&emsp;2). Ensure Apache activates virtual environment when running:  
&emsp;  
&emsp;&emsp;Since we are dealing with a virtual environment, these two lines are  
&emsp;&emsp;required at the top of our wsgi file:  
```
activate_this = '/path/to/env/bin/activate_this.py' 
execfile(activate_this, dict(__file__=activate_this)) 
```
&emsp;&emsp;otherwise apache will default to reading the non-virtual path.  
&emsp;&emsp;as this is where our project script 'catalog.py' resides.  
&emsp;  
&emsp;&emsp;Note this directory (/var/www/catalog/psql_catalog/) is also where our  
&emsp;&emsp;controller .wsgi script resides as we'll be needing that in the next step.  
&emsp;  
&emsp;&emsp;The .wsgi tends to be enabled by default but you can run:  
&emsp;&emsp;`sudo a2enmod wsgi`  
&emsp;  
&emsp;&emsp;to ensure that it is.   
&emsp;  
&emsp;3). Create a new virtual host configuration file.  
&emsp;  
&emsp;&emsp;`sudo vim /etc/apache2/sites-available/catalog.conf`  
&emsp;  
&emsp;&emsp;paste the following information inside this file:  

```
<VirtualHost *:80>  
ServerName 12.345.67.890  
ServerAdmin admin@12.345.67.890  
WSGIDaemonProcess catalog python-path=/var/www/catalog:/var/www/catalog/venv/lib/python2.7/site-packages  
WSGIScriptAlias / /var/www/catalog/psql_catalog/controller.wsgi  
<Directory /var/www/catalog/psql_catalog/>  
Order allow,deny  
Allow from all  
</Directory>  
Alias /static /var/www/catalog/psql_catalog/static  
<Directory /var/www/catalog/psql_catalog/static/>  
Order allow,  
deny Allow from all  
</Directory>  
ErrorLog ${APACHE_LOG_DIR}/error.log  
CustomLog  
${APACHE_LOG_DIR}/access.log combined  
LogLevel warn  
</VirtualHost>
```

&emsp;&emsp;In order for this new virtual host to be effectuated, run:

&emsp;&emsp;`sudo a2ensite catalog`

&emsp;&emsp;and then restart the apache service:

&emsp;&emsp;`sudo service apache2 reload`

&emsp;&emsp;(or `sudo apache2ctl restart`)

&emsp;&emsp;The site should now be up and running, we can check that in any browser:

&emsp;&emsp;http://12.345.67.890:80

&emsp;&emsp;Finally, in order to render the Google sign-in functionality of the  
&emsp;&emsp;site, we need to add our new server as an authorized host.  
&emsp;&emsp;To do this, go to the API credentials section for the current application  
&emsp;&emsp;in the Google console dashboard.  
&emsp;  
&emsp;&emsp;Add our host to the list of authorized origins to avoid the 'origin_mismatch' error:  
&emsp;&emsp;`http://12.345.67.890`  
&emsp;  
&emsp;&emsp;The site should now accept Oauth 2.0 via Google sign-in.  
&emsp;  
&emsp;  
With the site now fully deployed and functionality enabled, please refer to the  
instructions in the [README.md](https://github.com/builderLabs/psql_catalog/blob/master/README.md) for app-specific guidance.
