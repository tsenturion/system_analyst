import pandas as pd
import openpyxl


df = pd.read_csv('sales.csv') #Загружаем CSV

print(df)

df.to_csv('sales_new.csv', index=False)

df = pd.read_excel('sales.xlsx')

print(df)

df.to_excel('sales_new.xlsx', index=False)

import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)

with open('data_new.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

import xml.etree.ElementTree as ET

tree = ET.parse('sales.xml')
root = tree.getroot()

for month in root:
    print(month.attrib, month.text)

root = ET.Element('Продажи')

month1 = ET.SubElement(root, 'Месяц', name='Январь', категория='Электроника')
month1.text = '1200'

tree = ET.ElementTree(root)
tree.write('sales_new.xml', encoding='utf-8', xml_declaration=True)


with open('Sistemnyi_analitik.pdf', 'rb') as file:
    content = file.read()
    print(f'Длина файла: {len(content)} байт')

with open('copy.pdf', 'wb') as file:
    file.write(content)

df = pd.read_csv('sales.csv')
df.to_excel('sales.xlsx', index=False)

tables = pd.read_html('table.html')
df = tables[0]  # берем первую таблицу на странице
print(df)

import zipfile
import pandas as pd

with zipfile.ZipFile('data.zip', 'r') as z:
    with z.open('sales.csv') as file:
        df = pd.read_csv(file)
        print(df)

import logging


with open("data.txt", "r") as file:
    content = file.read()
    print(content)
