

# Configuração inicial no arquivo [ pp/urls.py ]
def parte_9():
    """
    ---------------------------------------------------- IMPORTAÇÃO ----------------------------------------------------
    from django.urls import include

    ---------------------------------------------- urlpatterns (inserir) ----------------------------------------------
    path('', include('pa.urls'))

    -> O argumento no método [ include() ] é referente ao [ pacote.arquivo ] que está sendo chamado
    -> O arquivo ainda não existe, mas pode ser configurado com antecedência e ser criado logo após, no pacote [ pa ]
    """
