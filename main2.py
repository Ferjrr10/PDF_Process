import pandas as pd
import pdfplumber
import tabula
import os
import re
import csv
from datetime import date

fecha = date.today()

#URL del archivo
url = "C:/Users/user/Desktop/prueba pdf/PDF/temp2.pdf"


##df = tabula.read_pdf(url)
data_list=[]
data_list2=[]

 

#defino los patrones a buscar en el PDF

string1 = "Pieza"
pattern1 = '000' + r"\d{2}"
pattern2 = '000'+ r"\d{2}" 
pattern6= r'(\d+)\s+([a-zA-Z0-9\s]+)'
pattern3 = r"\d{1} " + string1
#pattern4 = r"\d{2} " + string1
#pattern5 = r"\d{3} " + string1

#compilo los patrones en RE
nuevo_sap = re.compile(pattern1)
nuevo_sap1 = re.compile(pattern2)
nuevo_sap2 = re.compile(pattern3)
nuevo_sap6= re.compile(pattern6)
#nuevo_sap3 = re.compile(pattern4)
#nuevo_sap4 = re.compile(pattern5)

#Elijo destino del TXT
#file = open("C:/Users/argutierfe/Desktop/PDF/prueba.txt", "w")

#Se realiza filtro para asinación de columnas en el excel que también se genera.
string2="CAPITAL"
with pdfplumber.open(url) as pdf:
   for page in pdf.pages:
      for line in page.extract_text().split('\n'):
       if nuevo_sap.match(line) or nuevo_sap1.match(line) or nuevo_sap2.match(line):
        #a = file.write(line+','+'\n')
        parts = line.split() 
        if len(parts) >= 2 and parts[0].isdigit() and parts[1] != string2 and parts[1]!=string1:
          number = parts[0]
          description = ' '.join(parts[1:])
          data_list2.append([number, description])
          print(data_list2)
      
        else:
         if parts[1]==string1:
            cantidad = parts[0]
            tipo = parts[1]
            precio_unitario=parts[2]
            valor_total = parts[3]
            data_list.append([number, description,cantidad,tipo,precio_unitario,valor_total])
            df = pd.DataFrame(data_list, columns=["Posición", "Descripción","cantidad", "tipo", "Precio unitario", "valor total"])
            df.to_excel(f"C:/Users/user/Desktop/prueba pdf/PDF/{fecha}.xlsx", index=False)
            print(data_list)

        
        

