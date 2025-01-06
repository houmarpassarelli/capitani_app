#!/usr/bin/python
# -*- coding: latin-1 -*-

from flask import Flask, request, render_template, send_file
import csv
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Verifica se um arquivo foi enviado
        if 'file' not in request.files:
            return "Nenhum arquivo enviado."
        
        file = request.files['file']
        
        # Se o arquivo for vazio
        if file.filename == '':
            return 'Nenhum arquivo selecionado.'
        
        if file and file.filename.endswith('.txt'):
            # Lê o conteúdo do arquivo enviado
            content = file.read().decode('utf-8')

            # Processar o arquivo e gerar o CSV
            dados = processar_arquivo(content)
            
            # Gerar o CSV
            csv_output = gerar_csv(dados)

            # Criar um arquivo CSV temporário para download
            return send_file(
                io.BytesIO(csv_output),
                attachment_filename="dados_processados.csv",
                as_attachment=True
            )
        else:
            return "Por favor, envie um arquivo .txt."

    return render_template('form.html')

# Função para processar os dados do arquivo
def processar_arquivo(conteudo):
    dados = []

    # Verificando se o conteúdo contém quebras de linha
    if '\n' in conteudo:
        linhas = conteudo.split('\n')
        for linha in linhas:
            if linha:  # Verifica se a linha não está vazia
                dados.append(processar_dados(linha))
    else:
        # Se não houver quebras de linha, processa os dados a cada 25 caracteres
        for i in range(0, len(conteudo), 25):
            dados.append(processar_dados(conteudo[i:i+25]))
    
    # Ordenando os dados pelo valor do total de forma decrescente
    dados_ordenados = sorted(dados, key=lambda x: x['total'], reverse=True)

    # Selecionando apenas os 5 maiores totais
    dados_maiores = dados_ordenados[:5]
    
    return dados_maiores

# Função para processar os dados de cada entrada e calcular o total
def processar_dados(dados):
    referencia = dados[:10]
    quantidade = int(dados[10:15])  # Convertendo para inteiro
    preco = float(dados[15:]) / 100  # Convertendo para float e ajustando o preço
    
    # Garantindo que o preço tenha sempre 2 casas decimais
    preco_formatado = "{:.2f}".format(preco)

    # Calculando o total
    total = quantidade * preco

    # Garantindo que o total tenha sempre 2 casas decimais
    total_formatado = "{:.2f}".format(total)

    # Retorna os dados como um dicionário
    return {
        'referencia': referencia,
        'quantidade': quantidade,
        'preco': preco_formatado,
        'total': total_formatado
    }

# Função para gerar o arquivo CSV
def gerar_csv(dados):
    # Criando um arquivo CSV em memória
    output = io.BytesIO()
    writer = csv.DictWriter(output, fieldnames=['referencia', 'quantidade', 'preco', 'total'])
    
    # Escrevendo o cabeçalho
    writer.writeheader()
    
    # Escrevendo os dados no arquivo CSV
    writer.writerows(dados)
    
    # Mover o ponteiro do arquivo para o início para leitura
    output.seek(0)
    
    return output.read()

if __name__ == '__main__':
    app.run(debug=True)