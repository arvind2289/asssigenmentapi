# asssigenmentapi
assignment test
#setp 1 
git clone https://github.com/arvind2289/asssigenmentapi.git

cd asssigenmentapi
#Now create a virtual environment
virtualenv venv
#active virtual environment
setup 4
#install requrements dependency
#go requrements.text file location
pip install -r requrements.text
#setp 5
#runserver
python manage.py runserver
# makemigrations
python manange.py makemigrations

#migrate 
python manage.py migarte

# create super user
python manage.py createsuperuser
# now  go postman api
import api collection json file
assignment.postman_collection.json
# login by api 
http://127.0.0.1:8000/api/login/
email 
password
#create user by api
http://127.0.0.1:8000/api/createuser/
#list user same url by method get
#question post by user
http://127.0.0.1:8000/api/question/
#parameter send by Post method
question = "string"
user_id = int 
#main setting projects name is questions
user is app dir 






