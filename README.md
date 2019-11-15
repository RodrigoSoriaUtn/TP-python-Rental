# Trabajo Practico Metodologia de Sistemas III
![img](https://i.pinimg.com/originals/d9/70/36/d97036b366cf7dc60cebf3a4fee58463.png) ![img2](http://mareconversionpro.fr/wp-content/uploads/2017/05/bootstrap-logo-300x300.jpg) ![](https://freepngimg.com/thumb/python_logo/7-2-python-logo-free-download-png-thumb.png)

## Members :
 - Marcos Davidovich
 - Rodrigo Soria
## Tools :
 - Python 3.7
 - Django 2.2.7
 - Bootstrap 3
## Usage :
   Instalation :
   
    git clone https://github.com/RodrigoSoriaUtn/TP-python-Rental.git
    cd TP-python-Rental
    pip install Django==2.2.7
    pip install django-bootstrap3
 
  Run :
  
    py manage.py runserver
    
  Users:
  
     Username   | Password  | Type
     admin      | admin     | Super user
     SrCobranza | 123456ab  | Host
     HouseOwner | 123456ab  | Host
  Updating embedded db :
   
    py manage.py makemigrations
    py manage.py migrate
  
  Creating an admin (only if needed) :
  
    py manage.py createsuperuser
