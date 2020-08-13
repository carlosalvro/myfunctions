# -*- coding: utf-8 -*-
import pandas as pd 
from operator import itemgetter
from os import remove



def printing(table_name, header, query_elements):
    skeleton = [f'INSERT INTO {table_name}({header})']
    q = ','.join(query_elements[0])
    values = f'VALUES({q}),'
    skeleton.append(values)
    for query in query_elements[1:]:
        q = ','.join(query)
        s = f'({q}),'
        skeleton.append(s)
    skeleton[-1] = skeleton[-1][:-1]
    return skeleton

def separation_list(lista):
        lista2 = lista.split(',')
        return lista2

def converting(lista, elementos, beg = 1):
    lista_final =[]
    for i in range(beg, len(lista)):
        lista2 = lista[i].split(',')
        lista_f = lista2[:]
        for j in elementos:
            r = f'\'{lista2[j]}\''
            lista_f[j] = r
        lista_final.append(lista_f)

    return lista_final

def detect_strings():
    num = int(input('¿Cuantos son strings?: '))
    numeros = []
    for i in range(num):
        x = int(input('Numero: '))
        numeros.append(x-1)
    return numeros

def open_file():
    final = []
    with open('archivo.csv', 'r', encoding='utf8') as f:
        lineas = f.readlines()
    for linea in lineas:
        g = linea[:-1]
        final.append(g)
    return final

def made_csv(ruta):
    excel = pd.read_excel(ruta)
    csv_archive = excel.to_csv(r'.\archivo.csv', index=False)
    
def get_strings():
    global elements
    while True:
        print('Que elementos son strings')
        elements = detect_strings()
        print('los strings son')
        print(itemgetter(*elements)(headers))
        x = input('Es correcto? (y/n): ')
        if x.lower() == 'y':
            break
        print('Entonces'+ '\n')
        

if __name__ == '__main__':
    table_name = str(input('Nombre de la Tabla: '))
    ruta_excel = str(input('Donde esta el archivo?: '))
    #ruta_excel = r'C:\Users\carlo\Documents\basedata\ex1\ejemplo.xlsx'

    made_csv(ruta_excel)
    print('Archivo creado' + '\n')
    lista = open_file()
    remove("archivo.csv")
    print('Se agregaran los siguientes valores')
    headers = separation_list(lista[0])
    print(headers ,'\n')
    
    get_strings()
  
    headers = lista[0]
    query_elements = converting(lista, elements)
    queries = printing(table_name, headers, query_elements)

    for query in queries:
        print(query)

    # x = ['Nombre,Autor,Páginas,ISBN', 'La llamada de lo salvaje,Jack London,80,9788483089217', 'La Guerra de Los Mundos,H.G. Wells,224,9788491052371']
    
    
    
   
    


    