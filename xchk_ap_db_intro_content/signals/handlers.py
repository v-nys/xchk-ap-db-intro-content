from django.conf import settings
from django.utils.translation import ugettext_noop as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import mysql.connector

@receiver(post_save)
def create_shared_db_user(sender, instance, **kwargs):
    from xchk_core.models import Repo
    print("pre_save handler")
    if sender is Repo:
        print("repo gemaakt")
        if instance.course == 'databankenintro':
            print("repo DBI gemaakt")
            print(f'user: {instance.user}')
            mydb = mysql.connector.connect(host='studentmysql',user='root',password=settings.STUDENTMYSQL_ROOT_PASSWORD)
            mycursor = mydb.cursor()
            mycursor.execute(f'create database if not exists {instance.user.username};')
            mycursor.execute(f"create user if not exists {instance.user.username} identified by '{instance.user.initial_pw}';")
            mycursor.execute(f'grant all on {instance.user.username} to {instance.user.username};')
            mycursor.close()
