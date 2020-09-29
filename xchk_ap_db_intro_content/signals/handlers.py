from django.conf import settings
from django.utils.translation import ugettext_noop as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from xchk_core import Repo
import mysql.connector

@receiver(pre_save)
def create_shared_db_user(sender, instance, **kwargs):
    if sender is Repo:
        if instance.course == 'databankenintro':
            mydb = mysql.connector.connect(host='studentmysql',user='root',password=settings.STUDENTMYSQL_ROOT_PW)
            mycursor = mydb.cursor()
            mycursor.execute(f'create database {user.username};')
            mycursor.execute(f'create user {user.username} identified by {user.initial_pw};')
            mycursor.execute(f'grant all {user.username} to {user.username};')
            mycursor.close()
