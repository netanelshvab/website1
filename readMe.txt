venv activte:
        cd C:\Users\netan\PycharmProjects\djago_project1
        myworld\Scripts\activate.bat
     
        cd C:\Users\netan\PycharmProjects\djago_project1\myworld\my_dj_project_1
        py manage.py runserver

master - html - templat:
        {% extends "master.html" %}

        {% block title %}
        /// head
        {% endblock %}


        {% block content %}
        ///body
        {% endblock %}