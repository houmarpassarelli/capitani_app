# TESTE DE APP EM PYTHON
> O projeto consiste em uma aplicação monólito usando flask. <br />
> A interface é bem simples, somente para receber um arquivo no formato .txt.
> Após o processamento existe um retorno para download do arquivo CSV.
<br /><br />
> Há duas formas de execução: usando o docker e via terminal.<br />
> A porta foi alterada para ser executado em 8085.
<br /><br />
> O apontamento é para o host http://localhost:8085

## Melhorias futuras

> Para futuras melhorias pode-se implementar um solução que aceite mais tipos de arquivos e/ou registro temporário no formulário, criando uma listagem manual por exemplo.<br />
> Outra abordagem seria a possibilidade de criar um processo de extração de outras fontes de dados.

## Decisões do projeto

> Uma das decisões que tomei foi implementar um pequeno processo de execução via Docker, pois eu mesmo tive problemas com a versão do python, onde eu tenho duas no meu ambiente de trabalho. 

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