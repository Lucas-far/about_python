

# FONTE: 7. URIs baseados em recursos
def conceito():
    """
    ------- SIGNIFICADO -------
    Uniform Resource Identifier

    ------- CONCEITO -------
    Um caminho de url que aponta para acessar algo, podendo tornar o escopo cada vez mais específico

    ------- EXEMPLOS -------
    /usuarios                              || coleção
    /usuarios/{nomeUsuario}                || instância
    /usuarios/{nomeUsuario}/postagens      || instância
    /usuarios/{nomeUsuario}/postagens/{ID} || instância
    /postagens                             || coleção
    /postagens/{ID}                        || instância
    /postagens/{ID}/comentarios            || instância
    /postagens/{ID}/curtidas               || instância
    /postagens/{ID}/compartilhamentos      || instância
    """


# FONTE: 8. Coleções de recursos
def infos():
    """
    ------- URI -------
    Com recurso único || Instância (Instance)
    Com recursos      || Coleção (Collection)
    Com recursos      || Usam parâmetros de consulta (Query Parameters)

    ------- DETALHE -------
    URI - curto - menos específico - mais abrangente  - COLEÇÃO   - /postagens
    URI - longo - mais específico  - menos abrangente - INSTÃNCIA - /postagens/{ID}

    ------- DETALHE -------
    Coleção devem ser um texto substantivo no plural
    """