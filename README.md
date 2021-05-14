<h1 align="center">
House-Renting-Solver (Aria)
</h1>

The idea of "House-Renting-Solver" solves the house searching problems in this modern time. The project intends to solve the ‘to-let’ issue by turning it into a web-based system. The system offers to the users a proper description of ‘to-let’ houses in his located area. This system will work as a middleware between the owner and the customer and, the platform tends to reduce the waste of users’ time and money, as well as owners, and they will be benefited as the system will faster the renting process. 
Using Python Framework(Django) at backend, SQLite as database with HTML, CSS, Javascript and bootstrap at the frontend. 

***

### Requirements:
 * #### [Python 3.8 or up](https://www.python.org/downloads/release/python-372/)
 * #### [Django 3.2.2](https://www.djangoproject.com/) 
 * #### Database : [SQLite](https://www.sqlite.org/index.html/)
 


***
### How to work:
 * Clone the project
 * Open command line in project base dir and install all dependency
   > `pip install -r requirements.txt`
   
***   
### Database setup:
By default we are using SQLite. For using any other relational database please install the package of that database
for django and change the database dependency on `settings.py`.

***
### Some django keyword:
* To migrations the model:
  > `python manage.py makemigrations [app_name]`
 
* To migrate the models to Database:
  > `python manage.py migrate`
  
* To run the project in localhost:
  > `python manage.py runserver`

***

