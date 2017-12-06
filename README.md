# team-management
Api for manage team members

## Please follow the below steps for setup the project
1. Create database "instawork" in mysql. 
2. Clone the project and cd team-management.
3. Update database config in settings.py
2. Create the virtualenv and activate.
3. pip install -r requirement.txt
4. python manage.py migrate
5. python manage.py runserver

## API 
1. curl   -X   POST   -H   "Content-Type:application/json" http://127.0.0.1:8000/team   -d   '{"first_name": "ravi", "last_name": "ranjan", "email": "ravi@test.com", "phone": "9535594442", "role": "regular"}'
2. curl   -X   PUT   -H   "Content-Type:application/json" http://127.0.0.1:8000/team   -d   '{"id":1, "last_name": "ranjan kumar", "email": "raviranjan@test.com"}'
3. curl   -X   GET   -H   "Content-Type:application/json" http://127.0.0.1:8000/team
4. curl   -X   DELETE  -H   "Content-Type:application/json" http://127.0.0.1:8000/team   -d   '{"id":1}'
