

"""
-------------------------------------------------------- FONTE --------------------------------------------------------
https://vrsystem.info/publico/manual_index.aspx
Outro - Como instalar o Microsoft SQL Server

Microsoft - SQL Server® 2014 Express
Local de instalação: [ C:\Users\seu_user\Desktop\SQLEXPR_x64_PTB\ ]
Nova instalação autônoma do SQL Server ou adicionar recursos a uma instalação existente
Aceito os termos da licença
Seleção de Recursos (inalterável) (avançar)
Configuração da instância -> Instância nomeada (marcar) -> SQL2014 -> [ avançar ]
Configuração do Servidor -> [ avançar ]

Configuração do mecanismo de banco de dados -> [ Modo misto (marcar) ]
    Digitar senha: senha
    Confirmar senha: senha
    [ avançar ]

-------------------------------------------------------- FONTE --------------------------------------------------------
https://vrsystem.info/publico/manual_index.aspx
Outro - Configurando o E-trade para trabalhar em rede

Abrir as configurações avançadas do firewall
Nova regra de entrada
Tipo de regra:      [ Porta ] [ avançar ]
Protocolo e Portas: [ TCP ] [ Portas locais específicas = 1434 ] [ Avançar ]
Ação:               [ Permitir a conexão ] [ Avançar ]
Perfil:             [ Não alterar ]
Nome:               [ subjetivo (ex: Etrade 1434 Entrada) ] [ Concluir ]

Abrir o SQL Server 2014 Configuration Manager (ADMIN)
- Configuração de rede do SQL Server -> Protocolos para SQL2014 -> TCP/IP (botão ->) (habilitar)
- Serviços do SQL Server -> SQL Server (botão ->) (reiniciar)
- Configuração de rede do SQL Server -> Protocolos para SQL2014 -> TCP/IP (botão ->) (propriedades) -> Endereços IP
  -> IPAll (Porta TCP = 1434) -> [ Aplicar ] -> [ OK ]

- Baixar o instalador do [ E-trade ], seguido da sua versão [ Stable ]
- Ir à pasta do Etrade (botão ->) [ Segurança (aba) ] [ Selecionar cada usuário ] [ Editar ] [ Controle Total (marcar) ]
  [ Aplicar ] [ OK ]
- Ir à pasta do Etrade -> abrir o arquivo [ ArqID ] e fazer uma configuração
- A configuração = ipv6\nome_instância_sql_server,id_porta (ex: 192.168.3.12\SQL2014,1434)

SE A CONEXÃO FOR EXTERNA (DDNS, IP DE INTERNET FIXO, HAMACHI E ETC...) UTILIZE A PORTA 8100, TIVEMOS RELATOS DA 1434 NÃO
FUNCIONAR CORRETAMENTE EM CONEXÕES EXTERNAS. LEMBRE-SE TAMBÉM DE ABRIR A PORTA 8100 NO ROTEADOR DO SERVIDOR. PARA
VERIFICAR SE A PORTA ESTÁ ABERTA, INDICAMOS [ https://www.yougetsignal.com/tools/open-ports/ ]

FEITAS AS CONFIGURAÇÕES DE PORTA NO SERVIDOR, ANOTE O IP DO MESMO, POIS IREMOS PRECISAR DELE. AGORA PODEMOS PROSSEGUIR
PARA A ESTAÇÃO.
168.227.19.151
"""
