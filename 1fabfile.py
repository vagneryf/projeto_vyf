# PRIMEIRO ARQUIVO DO FAB PARA TESTES

from fabric.api import local #, run, cd, env, prefix, sudo, settings
# from fabric.contrib.files import contains, upload_template

def hello(name="World"):
    "Ola mundo"
    print ("Hello %s!" % name)


def prepare_deploy():
    print ("Preparando deploy")
    local("./manage.py test my_app")
    # local("git add -p && git commit")
    # local("git push")

def run():
    "Runserver local"
    local("manage.py runserver 0.0.0.0:8000")

def nova_pasta(name="Nova Pasta"):
    local('mkdir "%s"' % name)

def pull(server="origin"):
    local('git pull %s' % server)