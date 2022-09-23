Project relative to WebSecurity Exam. 

Steps:

1. Clone this repo with: <br>
	$ git clone https:github.com/NicolaIomm/ws-django_vulnerable<br>

2. Extract the "data.zip" in a new folder "data". In this way you will have already initialized the database.<br>

3. Run:<br>
	$ docker compose build<br>
	$ docker compose up<br>

Note: <br>
The first time you run the image you will get an error caused by postgres database initialization.
The second time it will work :)