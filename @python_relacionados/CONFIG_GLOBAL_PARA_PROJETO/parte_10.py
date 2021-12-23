

# Criação e configuração inicial no arquivo [ pa/urls.py ]
def parte_10():
    """
    - Ir ao pacote de aplicação e criar um arquivo python [ urls.py ]
    - Inserir os conteúdos abaixo

    ---------------------------------------------------- IMPORTAÇÃO ----------------------------------------------------
    from django.urls import path
    from .views import IndexTemplateView

    ----------------------------------------------- urlpatterns (criar) -----------------------------------------------
    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index')
    ]
    """
