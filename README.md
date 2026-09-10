## Analisador de Histórico do Terminal

Projeto simples de análise de dados desenvolvido como exercício prático de Python. O script processa o histórico do shell para mapear as ferramentas mais utilizadas na linha de comando e gerar um gráfico demonstrativo.

## O que o projeto faz

- Lê o arquivo de histórico do terminal (.bash_history ou .zsh_history).
- Realiza a limpeza e extração dos comandos principais via pandas.
- Calcula o volume e percentual de uso das ferramentas.
- Gera um gráfico de barras (uso_terminal.png) com o top 10 comandos mais acessados.

## Pré-requisitos

- Python 3.8+

## Como rodar

1. Clone o repositório e acesse a pasta do projeto:
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>

2. Crie e ative o ambiente virtual:
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Crie o arquivo .env baseado no caminho do seu histórico:
   echo "HIST_FILE=$HOME/.bash_history" > .env
   (Substitua .bash_history por .zsh_history se utilizar Zsh)

5. Execute o script:
   python analisar_history_pandas.py terminal-history-analysis
