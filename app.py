from flask import Flask, render_template, request
import subprocess
import pdfplumber
import pandas as pd
from datetime import date

fecha_hoy = date.today()

path=f"C:/Users/user/Desktop/prueba pdf/PDF/{fecha_hoy}.xlsx"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return 'No PDF file uploaded.'

    pdf_file = request.files['pdfFile'] 

    if pdf_file.filename == '':
        return 'No selected PDF file.'

    # Save the PDF file to a temporary location
    pdf_path = 'temp.pdf'
    pdf_file.save(pdf_path)
    python_path = 'C:/Users/user/Desktop/prueba pdf/PDF/venv/Scripts/python.exe'

    # Run the main.py script with the saved PDF file as an argument
    subprocess.check_call(['python', 'main.py', pdf_path])
    return f'El PDF fue procesado con éxito y se encuentra el en siguiente link: {path}'
    


@app.route('/upload1', methods=['POST'])
def upload1():
    if 'pdfFile' not in request.files:
        return 'No PDF file uploaded.'

    pdf_file = request.files['pdfFile'] 

    if pdf_file.filename == '':
        return 'No selected PDF file.'

    # Save the PDF file to a temporary location
    pdf_path = 'temp2.pdf'
    pdf_file.save(pdf_path)
    python_path1 = 'C:/Users/user/Desktop/prueba pdf/PDF/venv/Scripts/python.exe'

    # Run the main.py script with the saved PDF file as an argument
    subprocess.run(['python', 'main2.py', pdf_path], shell=True)
    return f'El PDF fue procesado con éxito y se encuentra el en siguiente link: {path}'

if __name__ == '_main_':

    app.run(debug=False)