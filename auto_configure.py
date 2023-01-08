"""
Command:

    $ python manage.py shell < auto_configure.py
"""
from django.core.management.utils import get_random_secret_key
# from django.contrib.auth import get_user_model
from django.apps import apps

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


# autoset envs
def set_random_generate_secret_key(env):
    try:
        env.str("SECRET_KEY")
    except:
        secret_key = get_random_secret_key()
        with open("./.env", "a+") as envfile:
            envfile.write(f"SECRET_KEY='{secret_key}'\n")
            print("Create SECRET_KEY variable in .env")
        env.read_env()


def set_default_keys(env):
    # ALLOWED_HOSTS
    try:
        env.str("ALLOWED_HOSTS")
    except:
        with open("./.env", "a+") as envfile:
            envfile.write("ALLOWED_HOSTS=localhost,127.0.0.1\n")
            print("Create ALLOWED_HOSTS variable in .env")
        env.read_env()

    # DEBUG
    try:
        env.str("DEBUG")
    except:
        with open("./.env", "a+") as envfile:
            envfile.write("DEBUG=false\n")
            print("Create DEBUG variable in .env")
        env.read_env()


def autoCreateSuperUser():
    user_model = get_user_model()
    super_users = user_model.objects.filter(is_superuser=True)
    if not super_users:
        super_uer = user_model.create_superuser(
            username='superuser', password='superuser')
        if super_user.id:
            print(f'Successful create superuser -> {superuser.username}')


# def autoCreateDjangoSite():
#     site_model = apps.get_model('sites', 'Site')
#     sites = site_model.objects.all()
#     example_site = site_model.objects.filter(name='example.com')
#     if not sites.exists() or (example_site.exists() and sites.count() == 1):
#         new_site = site_model.objects.create(
#             domain='127.0.0.1:8000', name='127.0.0.1:8000')
#         if new_site.id:
#             print(f'Saccessful create site -> {new_site.name}')
#         try:
#             env.str("SITE_ID")
#         except:
#             with open("./.env", "a+") as envfile:
#                 envfile.write(f"SITE_ID={new_site.id}\n")
#                 print("Create SITE_ID variable in .env")
#             env.read_env()


def auto_configure(env):
    set_default_keys(env)
    autoCreateSuperUser()
    # autoCreateDjangoSite()


if __name__ == '__main__':
    import environs
    env = environs.Env()
    env.read_env()

    auto_configure(env)
