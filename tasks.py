from invoke import task
from invoke.exceptions import UnexpectedExit

from config.settings.local import DATABASES


db_container_name = 'dev_realitymismatch'
node_version = '10'


@task
def installdocker(c):
    c.run('curl -fsSL https://get.docker.com -o /tmp/get-docker.sh')
    c.run('sudo sh /tmp/get-docker.sh')


@task
def install_nvm(c):
    "Install Node Version Manager"
    c.run('curl -o- \
    https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash')
    c.run(". ~./bashrc")


@task
def install_project_node(c):
    "Install Project Node Version (required NVM)"
    c.run('nvm install ' + node_version)


@task
def startdevelopment(c):

    db_name = DATABASES['default']['NAME']
    db_user = DATABASES['default']['USER']
    db_pw = DATABASES['default']['PASSWORD']
    container_tag = '11.3-alpine'
    exposed_port = '5432'

    print('Trying to raise database container')
    try:
        c.run(f'sudo docker start {db_container_name}')
    except UnexpectedExit:
        print('\033[1;31mContainer did\'nt exist before.\033[0m\n\
Creating database container.')
        c.run(
            f'sudo docker run -d --name {db_container_name} \
            -e POSTGRES_DB={db_name} -e POSTGRES_USER={db_user}\
            -e POSTGRES_PASSWORD={db_pw}\
            -p 127.0.0.1:{exposed_port}:5432 postgres:{container_tag}')


@task
def finishdevelopment(c):
    print('Powering off database')
    c.run(
        f'sudo docker stop {db_container_name}'
    )
