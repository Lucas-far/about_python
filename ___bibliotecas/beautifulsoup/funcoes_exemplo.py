

from bs4 import BeautifulSoup


def fix_html(skin):

    fixed = BeautifulSoup(skin, 'lxml')
    return fixed


def get_tag_all_content(do_filter, skin, tag, content):

    if do_filter:
        box = skin.find_all(tag)
        box_main = []
        for data in box:
            box_main.append(data.get(content))
        return box_main
    else:
        box = skin.find_all(tag)
        return box


def replace_content(is_iterable, target, this_, for_this):

    if is_iterable:
        target = [data.replace(this_, for_this) for data in target]
        return target


def download(url, file_path, file_name, file_format):
    import urllib.request

    full_path = file_path + file_name + file_format
    urllib.request.urlretrieve(url, full_path)


if __name__ == '__main__':

    #todo: Editável
    source = 'https://conteudo.colaboraread.com.br/201802/INTERATIVAS_2_0/MODELAGEM_DE_DADOS/U1/S3/images/'

    #todo: Editável
    html_string = """

<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  --><!--  Last Published: Wed Jul 10 2019 16:16:30 GMT+0000 (UTC)  --><html data-wf-page="5b3e3d36f5523c9682d50a4b" data-wf-site="5b3e3d36f5523c1cefd50a4c"><head>
  <meta charset="utf-8">
  <title>WA06182 - U1S3 - Modelagem de Dados</title>
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="Webflow" name="generator">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/webflow.css" rel="stylesheet" type="text/css">
  <link href="css/wa06182-u1s3-mda.webflow.css" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">WebFont.load({  google: {    families: ["Open Sans:300,300italic,400,400italic,600,600italic,700,700italic,800,800italic","Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic"]  }});</script>
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script>
  <link href="https://daks2k3a4ib2z.cloudfront.net/img/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="https://daks2k3a4ib2z.cloudfront.net/img/webclip.png" rel="apple-touch-icon">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous">
  <style>
	body{
  overflow-x: hidden;
  }
</style>
</head>
<body class="body">
  <div id="cover" class="cover">
    <div class="container w-container">
      <div class="cont-left-capa">
        <div class="content-cover">
          <div data-w-id="6ff92034-8eef-640e-54a9-b614ae5ebcef" style="opacity:0;-webkit-transform:translate3d(0, -500PX, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, -500PX, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, -500PX, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, -500PX, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)" class="buttom-cover">
            <div class="line"></div><a href="#01" data-w-id="222ec9dc-e72d-1394-1711-d8e530a842fe" class="btn w-button"><span class="fas fa-arrow-down"> </span></a></div>
          <div data-w-id="262d7ad2-c552-c031-b42a-036f5198b7ee" style="opacity:0;-webkit-transform:translate3d(-500PX, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(-500PX, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(-500PX, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(-500PX, 0, 0) scale3d(1, 1, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0)" class="txt-header">
            <div class="txt-top-capa">
              <h1 class="h1 mb">Modelagem<br>de Dados</h1>
              <h4 class="h4 bt">Dados como apoio a tomada de decis&#xE3;o.</h4>
            </div>
          </div>
        </div>
      </div>
      <div class="cont-rigth">
        <div data-w-id="298e8820-53ef-8de3-d9b9-a69365f3ba41" style="-webkit-transform:translate3d(0, 0, 0) scale3d(0, 0, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-moz-transform:translate3d(0, 0, 0) scale3d(0, 0, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);-ms-transform:translate3d(0, 0, 0) scale3d(0, 0, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);transform:translate3d(0, 0, 0) scale3d(0, 0, 1) rotateX(0) rotateY(0) rotateZ(0) skew(0, 0);opacity:0" class="content-img"></div>
      </div>
    </div><a href="documents/webaula.pdf" target="_blank" data-ix="menu-fechar" class="bt-pdf w-inline-block"></a></div>
  <div class="btn-sections"><a href="#cover" class="bullet w-inline-block"></a><a href="#01" class="bullet w-inline-block"></a><a href="#02" class="bullet w-inline-block"></a><a href="#03" class="bullet w-inline-block"></a><a href="#04" class="bullet w-inline-block"></a><a href="#05" class="bullet w-inline-block"></a><a href="#06" class="bullet w-inline-block"></a></div>
  <div id="01" class="section bg-gray v">
    <div class="contain w-container">
      <div class="div-block">
        <div class="div-block-txt center">
          <h1 class="heading-h">Sistemas de Apoio &#xE0; Decis&#xE3;o</h1>
          <div class="line-s"></div>
        </div>
        <div class="div-block-txt center">
          <p class="paragraph">Os dados podem influenciar na tomada de decis&#xE3;o das empresas e, para ajudar os gestores a tomar decis&#xF5;es e apontar problemas que possam ocorrer, existem os Sistemas de Apoio &#xE0; Decis&#xE3;o. Eles s&#xE3;o sistemas que ajudam na an&#xE1;lise de informa&#xE7;&#xE3;o do neg&#xF3;cio, baseados em informa&#xE7;&#xF5;es, em estat&#xED;sticas, em gr&#xE1;ficos de consumo, etc. , que s&#xE3;o obtidos a partir de informa&#xE7;&#xF5;es detalhadas armazenadas nos SGBD&#x2019;s.</p>
        </div>
      </div>
    </div>
  </div>
  <div id="02" class="section boxes">
    <div class="contain w-container">
      <div class="div-oculta-01" data-ix="esconde1">
        <div class="div-block-txt cmb">
          <div class="div-block-txt">
            <h4 class="heading-h4 _2">OLTP</h4>
            <p class="paragraph">Permite consultas do dia a dia da empresa.As transa&#xE7;&#xF5;es realizadas no banco de dados utilizam comandos do SQL (<em>Structured Query Language</em> ou Linguagem de Consulta Estruturada) como: INSERT, UPDATE e DELETE. Estas transa&#xE7;&#xF5;es s&#xE3;o realizadas em tempo real e n&#xE3;o armazenam um hist&#xF3;rico das consultas realizadas no banco de dados, dificultando o aux&#xED;lio &#xE0; tomada de decis&#xF5;es.</p>
          </div>
          <div class="line-s"></div>
          <p class="paragraph"><strong class="bold-text">Exemplo</strong>: Uma secret&#xE1;ria faz a matr&#xED;cula de um aluno do sistema de uma determinada faculdade, inserindo as informa&#xE7;&#xF5;es do discente (inser&#xE7;&#xE3;o). Caso o aluno se matricule num curso e se arrependa querendo troc&#xE1;-lo, a secretaria poder&#xE1; modificar (consulta de altera&#xE7;&#xE3;o).</p>
        </div>
      </div>
      <div class="div-oculta-02" data-ix="esconde-2">
        <div class="div-block-txt cmb">
          <div class="div-block-txt">
            <h4 class="heading-h4 _2 _3">OLAP</h4>
            <p class="paragraph">Processo interativo de criar, gerenciar, analisar e gerar relat&#xF3;rios sobre os dados de banco de dados. Os dados coletados s&#xE3;o armazenados em uma tabela multidimensional (ou <em>arrays</em> multidimensionais) para posterior an&#xE1;lise de algoritmos e <em>softwares</em> espec&#xED;ficos. Para fazer as an&#xE1;lises, os dados s&#xE3;o coletados do OLTP e isso acontece de acordo com a necessidade da empresa. O OLAP &#xE9; a capacidade de analisar grandes volumes de informa&#xE7;&#xF5;es dentro de um <em>Data Warehouse</em>, tamb&#xE9;m faz refer&#xEA;ncia &#xE0;s ferramentas anal&#xED;ticas utilizadas no BI para a visualiza&#xE7;&#xE3;o das informa&#xE7;&#xF5;es gerenciais e d&#xE1; suporte para as fun&#xE7;&#xF5;es de an&#xE1;lises do neg&#xF3;cio organizacional.</p>
          </div>
          <div class="line-s"></div>
          <p class="paragraph"><strong class="bold-text _2">Exemplo</strong>: No final no bimestre, o diretor desta mesma faculdade precisa de um relat&#xF3;rio com o perfil dos alunos nos &#xFA;ltimos tr&#xEA;s anos. No relat&#xF3;rio, ser&#xE3;o analisados: idade, curso, semestres cancelados e situa&#xE7;&#xE3;o financeira. Essas &#xA0;informa&#xE7;&#xF5;es servir&#xE3;o para a tomada de decis&#xE3;o de oferta de novos cursos e para defini&#xE7;&#xE3;o do perfil de aluno desejado.</p>
        </div>
      </div>
      <div class="row-2 mg w-row">
        <div class="column-2 w-col w-col-6">
          <div class="div-box bg-boxe">
            <div class="box-content">
              <div class="div-block-txt cmb"><img src="images/icon3.png" width="100" alt class="image-3">
                <div class="div-block-txt">
                  <h4 class="heading-h4 _2">OLTP</h4>
                  <h6 class="heading-h4 h5"><em>On-line Transaction Processing</em> ou Processamento de Transa&#xE7;&#xF5;es em Tempo Real</h6>
                </div>
                <p class="paragraph-7">S&#xE3;o opera&#xE7;&#xF5;es realizadas no SGBD que permitem realizar consultas na base de dados de forma repetitiva, a n&#xED;vel operacional e administrativo. O OLTP permite consultas do dia a dia da empresa.</p>
              </div>
              <div class="btn-mais" data-ix="divoculta">
                <p class="paragraph-5">Saiba Mais</p>
              </div>
            </div>
          </div>
        </div>
        <div class="column-2 w-col w-col-6">
          <div class="div-box bg-boxe">
            <div class="box-content">
              <div class="div-block-txt cmb"><img src="images/icon2.png" width="100" alt class="image-3">
                <div class="div-block-txt">
                  <h4 class="heading-h4 _2">OLAP</h4>
                  <h6 class="heading-h4 h5"><em>On-line Analytical Processing</em> ou Processamento Anal&#xED;tico On-line</h6>
                </div>
                <p class="paragraph-7">&#xC9; o processo de an&#xE1;lise dos dados dos sistemas transacionais OLTP, que permite a m&#xFA;ltipla an&#xE1;lise da informa&#xE7;&#xE3;o, possibilitando que gestores possam tomar decis&#xF5;es mais assertivas.</p>
              </div>
              <div class="btn-mais" data-ix="divoculta-2">
                <p class="paragraph-5">Saiba Mais</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box-msg">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-01.png" width="150" height="150" alt></div>
    <div class="box-msg2">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-02.png" width="150" height="150" alt></div>
  </div>
  <div id="03" class="section bg-gray">
    <div class="contain w-container">
      <div class="line-01">
        <div class="line-img"><img src="images/icon-10.png" width="100" alt class="image-3">
          <h4 class="heading-h4">DATA <br>WAREHOUSE</h4>
        </div>
        <div class="line-txt sml">
          <p class="paragraph-6">Data Warehouse ou Dep&#xF3;sito de Dados &#xE9; um tipo especial de banco de dados. &#xC9; um arquivo ou reposit&#xF3;rio de informa&#xE7;&#xF5;es obtidas de v&#xE1;rias origens (de v&#xE1;rios bancos de dados) e armazenadas em um &#xFA;nico local (preserva o banco de dados original da empresa). &#xC9; orientado por assunto, integrado e n&#xE3;o vol&#xE1;til, permitindo consultas para ajudar na tomada de decis&#xE3;o.</p>
        </div>
      </div>
      <div class="line-01">
        <div class="line-img"><img src="images/icon-data.png" width="100" alt class="image-3">
          <h4 class="heading-h4">DATA <br>MINING</h4>
        </div>
        <div class="line-txt">
          <p class="paragraph-6">Data Mining ou minera&#xE7;&#xE3;o de dados refere-se &#xE0; descoberta de novas informa&#xE7;&#xF5;es em fun&#xE7;&#xE3;o de regras ou padr&#xF5;es em grandes quantidades de dados e pode ser aplicado em pesquisas cient&#xED;ficas ou em empresas com o objetivo de aumentar significativamente a lucratividade.</p>
        </div>
      </div>
      <div class="line-01">
        <div class="line-img"><img src="images/icon-data2.png" width="100" alt class="image-3">
          <h4 class="heading-h4">BI</h4>
        </div>
        <div class="line-txt">
          <p class="paragraph-6"><em>Business Intelligence</em> (Intelig&#xEA;ncia de Neg&#xF3;cios) &#xE9; o processo de coleta, an&#xE1;lise, monitoria e compartilhamento de informa&#xE7;&#xF5;es para a gest&#xE3;o de neg&#xF3;cios. O BI analisa dados brutos operacionais para encontrar informa&#xE7;&#xE3;o &#xFA;til e auxiliar na tomada de decis&#xE3;o.</p>
        </div>
      </div>
    </div>
    <div class="box-msg">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-01.png" width="150" height="150" alt></div>
    <div class="box-msg2">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-02.png" width="150" height="150" alt></div>
  </div>
  <div id="04" class="section boxes _2">
    <div class="contain w-container">
      <div class="div-block">
        <div class="div-block-txt center">
          <h1 class="heading-h h-white">Redund&#xE2;ncia</h1>
          <p class="paragraph white-mg">Redund&#xE2;ncia significa repeti&#xE7;&#xE3;o.</p>
          <div class="line-s"></div>
        </div>
        <div class="div-block-txt center">
          <p class="paragraph white-mg">O grande n&#xFA;mero de dados e a modelagem de um banco de dados pode levar a redund&#xE2;ncias, ocasionando problemas futuros. O controle da redund&#xE2;ncia de um banco de dados &#xE9; uma tarefa que deve ser realizada a partir da sua modelagem.</p>
        </div>
      </div>
      <div class="row-5 w-row">
        <div class="c w-col w-col-6">
          <div class="line-01 _2">
            <div class="line-img _2"><img src="images/icon-analise.png" width="100" alt class="image-3"></div>
            <div class="line-txt _2">
              <h4 class="heading-h4">An&#xE1;lise dos atributos</h4>
              <p class="paragraph-6"><em class="italic-text">A mesma informa&#xE7;&#xE3;o pode ser armazenada em v&#xE1;rias entidades diferentes, levando muitas vezes &#xE0; inconsist&#xEA;ncia do banco de dados.</em></p>
            </div>
          </div>
        </div>
        <div class="c w-col w-col-6">
          <div class="line-01 _2">
            <div class="line-img _2"><img src="images/icon-backup.png" width="100" alt class="image-3"></div>
            <div class="line-txt _2">
              <h4 class="heading-h4">Backup do banco de dados</h4>
              <p class="paragraph-6"><em>As c&#xF3;pias f&#xED;sicas do banco de dados geram redund&#xE2;ncia. Esse tipo de redund&#xE2;ncia &#xE9; controlada, visto que as c&#xF3;pias s&#xE3;o necess&#xE1;rias para manter a seguran&#xE7;a do banco de dados.</em></p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="box-msg">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-01.png" width="150" height="150" alt></div>
    <div class="box-msg2">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-02.png" width="150" height="150" alt></div>
  </div>
  <div id="05" class="section boxes _2 gray">
    <div class="contain w-container">
      <div class="div-block">
        <div class="div-block-txt center">
          <div class="line-img _2"><img src="images/cadeadp.png" width="100" alt class="image-3 w"></div>
          <h1 class="heading-h">Seguran&#xE7;a</h1>
          <div class="line-s white"></div>
        </div>
        <div class="div-block-txt center">
          <p class="paragraph">A seguran&#xE7;a da informa&#xE7;&#xE3;o ganhou notoriedade nestas &#xFA;ltimas d&#xE9;cadas. Riscos de ataques internos e externos podem afetar os dados e a pr&#xF3;pria administra&#xE7;&#xE3;o da empresa. As empresas precisam criar regras que possam garantir a seguran&#xE7;a aos seus dados, surgindo, assim, a pol&#xED;tica de seguran&#xE7;a da empresa. As regras s&#xE3;o criadas conforme as necessidades de cada organiza&#xE7;&#xE3;o, estabelecendo crit&#xE9;rios de acesso f&#xED;sico e remoto ao banco de dados.</p>
        </div>
      </div>
    </div>
    <div class="box-msg">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-01.png" width="150" height="150" alt></div>
    <div class="box-msg2">
      <p class="txt-box">Um banco de dados ou base de dados &#xE9; um conjunto de arquivos integrados que s&#xE3;o usados pelos sistemas de aplica&#xE7;&#xE3;o de uma determinada empresa. O termo faz refer&#xEA;ncia ao armazenamento dos dados.</p><img src="images/bc-02.png" width="150" height="150" alt></div>
  </div>
  <div id="06" class="section bg-gray-2 _2">
    <div class="contain-2 w-container">
      <div class="div-block-2 ml">
        <div class="div-block-txt center">
          <h1 class="heading-h h-white">Pol&#xED;ticas de Seguran&#xE7;a</h1>
          <div class="line-s"></div>
          <p class="paragraph white-mg _2">Clique em cada bot&#xE3;o para saber como as empresas precisam se prevenir, estabelecendo uma pol&#xED;tica de backup, de seguran&#xE7;a de acesso ao banco de dados e de permiss&#xF5;es e acessos &#xE0;s tabelas.</p>
        </div>
        <div data-duration-in="300" data-duration-out="100" class="tabs w-tabs">
          <div class="tabs-menu-2 w-tab-menu">
            <a data-w-tab="Tab 1" class="tab-link-tab-1-2 bg w-inline-block w-tab-link">
              <div class="text-block-3">Backup</div>
            </a>
            <a data-w-tab="Tab 2" class="tab-link-tab-2-2 bg w-inline-block w-tab-link">
              <div class="text-block-3">Senhas</div>
            </a>
            <a data-w-tab="Tab 3" class="tab-link-tab-3-2 bg w-inline-block w-tab-link">
              <div class="text-block-3">Permiss&#xF5;es</div>
            </a>
          </div>
          <div class="w-tab-content">
            <div data-w-tab="Tab 1" class="w-tab-pane">
              <div class="box-txt">
                <h4 class="heading-h4">REGRAS PARA BACKUP</h4>
                <p class="paragraph-center">Em caso de falhas, a c&#xF3;pia backup do banco de dados &#xE9; realizada.</p>
              </div>
              <div class="row-3 w-row">
                <div class="collum-2 w-col w-col-4"><img src="images/database.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">RESPONSABILIDADES</strong><br><br>Quem far&#xE1; o backup? Quem ter&#xE1; acesso a ele?</p>
                </div>
                <div class="collum-2 w-col w-col-4"><img src="images/cloud.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">MEIOS</strong><br><br>De que forma o backup ser&#xE1; feito? Qual m&#xED;dia ou nuvem usar? Qual software? Qual hardware?</p>
                </div>
                <div class="collum-2 w-col w-col-4"><img src="images/calendar-1.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">PER&#xCD;ODO</strong><br><br>Qual o intervalo dos backups? Diariamente, semanalmente, mensalmente?</p>
                </div>
              </div>
              <div class="row-3 w-row">
                <div class="collum-2 w-col w-col-6"><img src="images/server-13.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">RETEN&#xC7;&#xC3;O</strong><br><br>Quanto tempo o backup deve ficar armazenado na mesma m&#xED;dia?</p>
                </div>
                <div class="collum-2 w-col w-col-6"><img src="images/database-16.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">ARMAZENAMENTO</strong><br><br>Onde ser&#xE3;o armazenados os backups? Quais locais seguros dever&#xE3;o ser indicados?</p>
                </div>
              </div>
            </div>
            <div data-w-tab="Tab 2" class="w-tab-pane">
              <div class="box-txt">
                <h4 class="heading-h4">SENHAS DE ACESSO</h4>
                <p class="paragraph-center">Controlam o acesso ao banco de dados.</p>
              </div>
              <div class="row-2c w-row">
                <div class="collum-2 w-col w-col-4"><img src="images/lock-1.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">INTEGRIDADE<br>&#x200D;<br></strong>Garantia que as informa&#xE7;&#xF5;es ser&#xE3;o mantidas de forma &#xED;ntegra e sem modifica&#xE7;&#xF5;es indevidas de pessoas n&#xE3;o autorizadas.</p>
                </div>
                <div class="collum-2 w-col w-col-4"><img src="images/login-1.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">CONFIABILIDADE<br>&#x200D;</strong><br>Garantia que as informa&#xE7;&#xF5;es armazenadas no banco somente ser&#xE3;o acessadas por pessoas autorizadas previamente.</p>
                </div>
                <div class="collum-2 w-col w-col-4"><img src="images/private-folder-hand-drawn-outline.png" alt class="img-tab">
                  <p class="paragraph-center"><strong class="bold-text-2">DISPONIBILIDADE<br><br></strong>Garantia de disponibilizar a informa&#xE7;&#xE3;o somente &#xE0;s pessoas com permiss&#xE3;o de acesso e de modifica&#xE7;&#xE3;o.</p>
                </div>
              </div>
            </div>
            <div data-w-tab="Tab 3" class="w-tab-pane">
              <div class="box-txt">
                <h4 class="heading-h4">AUTENTICA&#xC7;&#xC3;O DO USU&#xC1;RIO</h4>
                <p class="paragraph-center">Permiss&#xE3;o para acessar e executar somente os trabalhos com autoriza&#xE7;&#xE3;o pr&#xE9;via, conforme o seu n&#xED;vel hier&#xE1;rquico dentro da empresa.</p>
              </div>
              <div class="row-3 w-row">
                <div class="collum-2 w-col w-col-3"><img src="images/database-17.png" alt class="img-tab">
                  <p class="paragraph-center">Somente leitura dos dados</p>
                </div>
                <div class="collum-2 w-col w-col-3"><img src="images/database-18.png" alt class="img-tab">
                  <p class="paragraph-center">Inserir novos dados</p>
                </div>
                <div class="collum-2 w-col w-col-3"><img src="images/database-19.png" alt class="img-tab">
                  <p class="paragraph-center">Atualizar novos dados</p>
                </div>
                <div class="collum-2 w-col w-col-3"><img src="images/database-21.png" alt class="img-tab">
                  <p class="paragraph-center">Excluir <br>dados</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div id="06" class="section bg-gray-2 video">
    <div class="contain-2 w-container">
      <div class="div-block-2 ml encerramento">
        <h1 class="heading-h h-white center">V&#xED;deo de Encerramento</h1>
        <div class="video-encerramento w-embed w-iframe"><iframe allowfullscreen webkitallowfullscreen mozallowfullscreen width="100%" height="100%" src="https://mdstrm.com/embed/5ea4b2180421ce070b97aca6" scrolling="no" frameborder="0" allow="geolocation; microphone; camera; encrypted-media; midi"></iframe></div>
      </div>
    </div>
  </div>
  <div id="07" class="section bg-degrade _2">
    <div class="contain w-container">
      <p class="paragraph-2 mg">O bem mais valioso de uma empresa &#xE9; a informa&#xE7;&#xE3;o, dessa forma, um SGBD deve oferecer ferramentas espec&#xED;ficas para a tomada de decis&#xE3;o e auxiliar na gest&#xE3;o de informa&#xE7;&#xE3;o da base de dados, bem como permitir que v&#xE1;rias formas de seguran&#xE7;a possam ser implementadas para proteger o banco de dados e preservar o seu conte&#xFA;do.</p>
      <div class="div-block ml">
        <div class="div-block-txt center fim">
          <h1 class="heading-h fim">Bons estudos!</h1><a href="#cover" class="home w-inline-block"><img src="images/home_1home.png" alt class="top"></a></div>
      </div>
    </div>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.4.1.min.220afd743d.js" type="text/javascript" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
  <script>
$(document).ready(function(){
    $(".btn-mais").click(function(){
        $(this).find('.img-mais').toggleClass('menos');
    });
});
</script>

</body></html>
        """

    html_fixed = fix_html(skin=html_string)
    html_all_images = get_tag_all_content(do_filter=True, skin=html_fixed, tag='img', content='src')
    content_main = replace_content(is_iterable=True,
                                   target=html_all_images,
                                   this_='images/',
                                   for_this=source)

    # print(content_main)
    for number, index in enumerate(content_main):
        number = number + 1
        download(url=index,
                 file_path='caixa/',
                 file_name=f'_3_cw_1_pt_2_img{number}',  # todo: Editável,
                 file_format='.png')
