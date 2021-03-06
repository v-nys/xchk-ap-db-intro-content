from django.shortcuts import render
from django.conf import settings
from xchk_core.models import Repo
import mysql.connector

# Create your views here.
def create_dbs_view(request):
    for db_repo in Repo.objects.filter(course='databankenintro'):
        try:
            uname = db_repo.user.username
            upw = db_repo.user.initial_pw
            mydb = mysql.connector.connect(host='studentmysql',database='sys',user='root',password=settings.STUDENTMYSQL_ROOT_PASSWORD)
            mycursor = mydb.cursor()
            mycursor.execute(f'create database if not exists {uname};')
            mycursor.execute(f"create user if not exists {uname} identified by '{upw}';")
            mycursor.execute(f"grant all on {uname}.* to {uname}@'%';")
            mycursor.close()
        except Exception as e:
            print(e)
    return render(request,'xchk_ap_db_intro_content/created.html',{})
