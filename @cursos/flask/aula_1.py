

# REST API Explicado
def conteudo():
    """
    Site != Aplicativo p/ disp. móveis
    Arquiteturas !=
    Site = desenvolvedor web
    App  = desenvolvedor mobile

    Então vejamos como funciona as aplicações que possuem tanto a versão MOBILE quanto a WEB, porém eles não possuem
    REST APIs. Eles têm o mesmo banco de dados, pra que tudo seja integrado, de forma que, tanto o desenvolvedor MOBILE
    quanto o WEB, precisarão criar mecanismos de comunicações diferentes com bancos de dados, e por serem diferentes,
    causam erros, no site, no aplicativo, ambos, porém, cada um com suas peciliariedades, o que causa uma difícil
    manutenção, pois qualquer atualização na forma que alguma coisa é criada, acarreta em atualizar a versão WEB e
    MOBILE. Ninguém consegue criar nada para o site/aplicativo, sem que seja liberado o acesso ao banco de dados e a
    detalhes de incrementações do código, tanto WEB quanto MOBILE, o que não é nada seguro

    Porém, hoje em dia já há uma solução. O conceito de REST API foi desenvolvido por Roy Fielding, em 2000, e seu uso
    vêm crescendo. Hoje em dia, criar aplicações sem REST APIs é completamente inviável. Estes são criados para
    solucionar integrações móveis e web de forma excepcional, pois define-se as funcionalidades que a aplicação
    oferecerá, conhecidas como RECURSOS, criam-se e disponibilizam-se estes por via ENDPOINTS, que são os endereços WEB
    que receberão as requisições dos desenvolvedores (DESKTOP/MOBILE)

    As alterações backend: como o código vai passar/funcionar, para entregar um recurso, não afetará os desenvolvedores,
    pois os ENDPOINTS permanecerão os mesmos, facilitando a manutenção.

    Além disso, isso fornece a segurança da aplicação, pois os desenvolvedores terão acesso somente aos ENDPOINTS, e
    terão ciência somente doq ue entregam, mas não terão conhecimento de detalhes do código, nem qualquer acesso além do
    que foi determinado na criação do REST API

    O que permite a divulgação pública dos RECURSOS da API para qualquer desenvolvedor usar sua criatividade para criar
    aplicativos ou sites, que utilizem esses RECURSOS, e agreguem valor aos usuários finais, o que pode fornecer a
    escalabilidade da aplicação

    O que é bom para a empresa criadora do REST API, pois têm a aplicação divulgada, sem a necessidade de contratar
    desenvolvedores para criarem aplicativos diferentes. É bom para os desenvolvedores de aplicativos e sites
    independentes, que consomem os REST APIS divulgados, pois a criatividade pode levar a criar aplicativos muito
    atraentes, pois a simples modificação de como esses dados são mostrados, já é o suficiente para ganhar dinheiro na
    venda direta de aplicativos, ou com divulgação de anúncios dos seus aplicativos gratuitos

    É bom para os usuários, pois dá uma variedade de opções, retirando o monopólio de dependência da empresa principal
    """
