# Minerador_Ativos
# Script para buscar cotação de ativos.

#### Necessário ter instalado a biblioteca Pyautogui -> https://pyautogui.readthedocs.io/en/latest/.

#### Necessário ter instalado a biblioteca PyMySQL -> https://pymysql.readthedocs.io/en/latest/user/installation.html.

#### Banco de dados utilizado -> MySQL

#### Executar o arquivo config.py e seguir as instruções.

1. Com o navegador Google Chrome aberto, posicionar o mouse de forma que o símbolo de recarregar não seja obstruído. Posicionar o mouse no vértice inferior direito do retângulo vermelho.

![image](https://user-images.githubusercontent.com/54442159/78452075-97dc7680-765f-11ea-9bbd-a3426b051509.png)

2. Abrir o site < https://www.tradingview.com/symbols/BMFBOVESPA-PETR4/ >, após carregado totalmente, apertar Ctrl + Shift + I, para exibir o HTML da página. Posicionar o mouse no vértice superior esquerdo do retângulo vermelho.

![image](https://user-images.githubusercontent.com/54442159/78452163-0cafb080-7660-11ea-88a8-aa570192b108.png)

3. Na barra de tarefas, posicionar o mouse sobre o símbolo do navegador Google Chrome.

![image](https://user-images.githubusercontent.com/54442159/78452202-4b456b00-7660-11ea-8ff6-2f1b65bbc386.png)

4. Dentro da pasta da aplicação, existe um arquivo chamado ciclo.py, copiar o diretório.

Exemplo: C:\users\user\Desktop\Minerador_Ativos

5. As informações referentes ao banco de dados MySQL são de responsabilidade individual. Utilizei um host que fornece um BD em nuvem de forma simples -> clever-cloud.com
Após configurar o BD, se tudo estiver correto, você poderá criar as tabelas e começar a utilizar a aplicação. Caso ocorra algum erro, será necessário configurar tudo novamente.

6. Após realizar as configurações executar o arquivo adicionarAtivo.py, nele você poderá selecionar os ativos que deseja monitorar. Na segunda execução, caso não tenha interesse em adicionar nenhum ativo, é possível executar somente o arquivo ciclo.py.

Na pasta imagens, dentro da pasta raíz, se encontram algumas imagens que são utilizadas para fazer a comparação, caso o programa só abra as guias, mas não dê inicio, será necessário recortar o D do site < https://www.tradingview.com/symbols/BMFBOVESPA-PETR4/ > e substituir pelo que se encontra na pasta. A imagem deverá conter somente o D.

Localizaçã do D -> ![image](https://user-images.githubusercontent.com/54442159/78452541-336ee680-7662-11ea-86fb-424da13fb688.png)

Exemplo de recorte -> ![image](https://user-images.githubusercontent.com/54442159/78452501-e559e300-7661-11ea-8353-db8892ffc4ff.png)

