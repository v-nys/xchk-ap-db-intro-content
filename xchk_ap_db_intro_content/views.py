from django.shortcuts import render
from django.conf import settings
from xchk_core.models import Repo
import mysql.connector

# Create your views here.
def create_dbs_view:
    for db_repo in Repo.objects.filter(course='databankenintro'):
        uname = db_repo.user.username
        upw = db_repo.user.initial_pw
        mydb = mysql.connector.connect(host='studentmysql',database='sys',user='root',password=settings.STUDENTMYSQL_ROOT_PASSWORD)
        mycursor = mydb.cursor()
        mycursor.execute(f'create database if not exists {instance.user.username};')
        mycursor.execute(f"create user if not exists {instance.user.username} identified by '{instance.user.initial_pw}';")
        mycursor.execute(f"grant all on {instance.user.username}.* to {instance.user.username}@'%';")
        mycursor.close()
