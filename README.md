# TESTE DE APP EM PYTHON
> O projeto consiste em uma aplicação monólito usando flask. <br />
> A interface é bem simples, somente para receber um arquivo no formato .txt.
> Após o processamento existe um retorno para download do arquivo CSV.
<br /><br />
> Há duas formas de execução: usando o docker e via terminal.<br />
> A porta foi alterada para ser executado em 8085.
<br /><br />
> O apontamento é para o host http://localhost:8085

## Requisitos

> Python 3.x<br />
> Docker

## Execução do projeto

### Executar com Docker

```bash
# Execute o docker localmente 
$ docker compose up -d
```

### Executar fora do docker

```bash
# Instalar flask
$ pip install flask

# Execute o arquivo principal
$ python main.py
```