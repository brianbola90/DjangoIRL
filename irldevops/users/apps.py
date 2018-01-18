from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'irldevops.users'
    verbose_name = "Users"

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('user'))



