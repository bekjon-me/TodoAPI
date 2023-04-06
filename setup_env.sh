

activate(){
  source venv/bin/activate # activete python env
  if [ -n "$VIRTUAL_ENV" ]; then
    echo "==> Activated environment"

    echo "==> Installing requirements to virtual environment"
    pip install -r requirements.txt

    echo "==> Applying migrations"
    python manage.py migrate
    
    python manage.py runscript -v3 auto_configure
    python manage.py collectstatic
  else
    echo "===> Error activating"
  fi
  
}

if [ -f ./manage.py ]; then
    if [ ! -f ./venv/bin/activate ]; then
      echo "==> Create python environment"
      python -m venv venv
    fi
    activate
fi
