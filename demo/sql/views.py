from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template import loader

from django.db.models import Max, Count

from .forms import CreateExamForm
from .forms import QueryForm

from .models import User
from .models import Exam

import random

def index(request):

	users = User.objects.all()
	exams = Exam.objects.all()
	examForm = CreateExamForm()
	queryForm = QueryForm()
	query_response = "No query evaluated yet."

	if request.method == 'POST' and 'name' in request.POST :
		examForm = CreateExamForm(request.POST)
		if examForm.is_valid():
			exam = Exam(name=request.POST['name'])
			exam.save()

	elif request.method == 'POST' and 'query_type' in request.POST:
		if request.POST['query_type'] == 'Aggregate':
			column_alias = request.POST['column_alias']

			#legit_input = 'max'
			#custom_input = 'max" FROM "sql_user"; INSERT INTO sql_exam (name) VALUES ('SQLi'); --'
			
			data = {
					column_alias : Max('age'),
			}

			try:
				query_response = User.objects.aggregate(**data)
			except: 
				query_response = "Void result"

		elif request.POST['query_type'] == 'Annotate':
			column_alias = request.POST['column_alias']

			#legit_input = 'stud_count'
			#custom_input = 'stud_count" FROM "sql_exam", "sql_user_exams" GROUP BY "sql_exam"."id"; DELETE FROM "sql_exam" WHERE "name" = 'SQLi'; --'
			data = {
				column_alias : Count('user'),
			}

			try:
				query_response = Exam.objects.annotate(**data)
				print(query_response)
			except: 
				query_response = "Void result"

		elif request.POST['query_type'] == 'Extra':
			column_alias = request.POST['column_alias']

			#legit_input = 'old_student'
			#custom_input = 'old_student" FROM "sql_user"; UPDATE "sql_exam" SET name = 'AnotherSQLi' WHERE name = 'EXAM'; -- '

			data = {
				"select": {column_alias: "name"},
				"tables": {"sql_user"},
				"where": ["age > 45"]
			}

			try:
				query_response = User.objects.extra(**data)
				print(query_response)
			except: 
				query_response = "Void Result"

	template = loader.get_template('sql/index.html')
	context = { 'users': users,
				'exams': exams,
				'exam_form': examForm,
				'query_response': query_response,
				'query_form': QueryForm}

	return HttpResponse(template.render(context, request))

def init(request):
	if request.method == 'POST':

		students = []
		for i in range(20):
			n = "student"+str(i+1)
			a = random.randint(18, 60)

			user = User(name=n, age=a)
			user.save()
			students.append(user)

		exams = []
		for exam in ['WSaP', 'DM', 'SES', 'CNS', 'AD', 'DS']:
			e = Exam(name=exam)
			e.save();
			exams.append(e)
		
		e = Exam(name="EXAM")
		e.save()

		for s in students:
			num_exams = random.randint(0, 5)
			random.shuffle(exams)
			for el in exams[:num_exams]:
				s.exams.add(el)

		return HttpResponseRedirect('/sql')

def reset(request):
	if request.method == 'POST':
		
		exams = Exam.objects.all().delete()

		users = User.objects.all().delete()

		return HttpResponseRedirect('/sql')
