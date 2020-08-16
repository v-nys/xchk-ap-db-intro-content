import inspect
import sys
from django.urls import path

from . import contentviews
from xchk_core.contentviews import is_content_view

urlpatterns = [path(cv[1].uid, cv[1].as_view(), name=f'{cv[1].uid}_view') for cv in inspect.getmembers(sys.modules['xchk_ap_db_intro.contentviews'],is_content_view)]
