Project relative to WebSecurity Exam. 

Steps:

1. Clone this repo with:
	$ git clone https:github.com/NicolaIomm/ws-django-vulnerable

2. Extract the "data.zip" in a new folder "data". In this way you will have already initialized the database.

3. Run:
	$ docker compose build
	$ docker compose up

Note: 
The first time you run the image you will get an error caused by postgres database initialization.
The second time it will work :)