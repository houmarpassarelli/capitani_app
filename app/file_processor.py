# -*- coding: utf-8 -*-

import csv
import io

class FileProcessor:
    def __init__(self, file_content):
        self.file_content = file_content

    def processFile(self):
        data = []

        if '\n' in self.file_content:
            rows = self.file_content.split('\n')
            for row in rows:
                if row:
                    data.append(self.processData(row))
        else:
            for i in range(0, len(self.file_content), 25):
                data.append(self.processData(self.file_content[i:i+25]))
        
        ordened_data = sorted(data, key=lambda x: x['total'], reverse=True)

        return ordened_data[:5]

    def processData(self, payload):

        reference = payload[:10]
        quantity = int(payload[10:15])
        price = float(payload[15:]) / 100
        
        formated_price = "{:.2f}".format(price)

        total = quantity * price

        formated_total = "{:.2f}".format(total)

        return {
            'referencia': reference,
            'quantidade': quantity,
            'preco': formated_price,
            'total': formated_total
        }

    def generateCSV(self, payload):
        
        output = io.BytesIO()
        writer = csv.DictWriter(output, fieldnames=['referencia', 'quantidade', 'preco', 'total'])
        
        writer.writeheader()
        writer.writerows(payload)
        
        output.seek(0)
        
        return output.read()