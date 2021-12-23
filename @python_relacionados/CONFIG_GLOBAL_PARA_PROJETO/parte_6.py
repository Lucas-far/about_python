

# Instalar dependências para iniciar um projeto Django
def parte_6():
    """
    Registrar as dependências do projeto
        pip freeze > requirements.txt

    Iniciar o pacote projeto de um projeto Django (pp = nome do pacote é subjetivo)
        django-admin startproject pp .

    Iniciar o pacote aplicação de um projeto Django (pa = nome do pacote é subjetivo)
        django-admin startapp pa

    Efetuar migrações de modelos e plugins
        python manage.py migrate

    Criar um usuário admin para gerenciar dados a serem inseridos no projeto
        python manage.py createsuperuser
    """
