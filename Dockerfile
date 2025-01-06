# Usando a imagem base do Python 3 mais recente
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando os arquivos necessários para dentro do contêiner
COPY . /app

# Instalando as dependências necessárias
RUN pip install --no-cache-dir -r packages.txt

# Expondo a porta 5000 para acesso à aplicação Flask
EXPOSE 8085

# Comando para rodar o aplicativo
CMD ["python", "main.py"]