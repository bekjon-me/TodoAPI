from django.core.management.utils import get_random_secret_key


def set_random_generate_secret_key(env):
    try:
        env.str("SECRET_KEY")
    except:
        secret_key = get_random_secret_key()
        with open("./.env", "a+") as envfile:
            envfile.write(f"SECRET_KEY='{secret_key}'\n")
        env.read_env()


def set_default_keys(env):
    # set ALLOWED_HOSTS
    try:
        env.str("ALLOWED_HOSTS")
    except:
        with open("./.env", "a+") as envfile:
            envfile.write("ALLOWED_HOSTS=localhost,127.0.0.1\n")
        env.read_env()

    # set DEBUG
    try:
        env.str("DEBUG")
    except:
        with open("./.env", "a+") as envfile:
            envfile.write("DEBUG=true\n")
        env.read_env()
