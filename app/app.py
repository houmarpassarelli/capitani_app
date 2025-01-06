# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, send_file
from .file_processor import FileProcessor
import io

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                
                if 'file' not in request.files:
                    return "Nenhum arquivo enviado."
                
                file = request.files['file']
                
                if file.filename == '':
                    return 'Nenhum arquivo selecionado.'
                
                if file and file.filename.endswith('.txt'):
                    
                    content = file.read()

                    content = content.decode('utf-8')

                    file_processor = FileProcessor(content)

                    data = file_processor.processFile()

                    csv_output = file_processor.generateCSV(data)

                    csv_bytes = io.BytesIO(csv_output.encode('utf-8'))

                    return send_file(
                        csv_bytes,
                        attachment_filename="dados_processados.csv",
                        as_attachment=True
                    )
                else:
                    return "Somente arquivo .txt"

            return render_template('file.html')

    def init(self):
        self.app.run(port=8085, host="0.0.0.0", debug=True)