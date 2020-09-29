from django.apps import AppConfig


class APDBIntrocontentConfig(AppConfig):
    name = 'xchk_ap_db_intro_content'

    def ready(self):
        from .signals import handlers
