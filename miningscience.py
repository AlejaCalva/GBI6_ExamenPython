import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

def download_pubmed (keyword):
    """
    Funcion que entrada pide la frase clave de busqueda y en output guarda un archivo que contiene los resultados de la 
    busqueda, considerando los titulos. 
    """ 
    Entrez.email = "ibeth.calva@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term=keyword+"[Title]",
                        retmax = 1000,
                        usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text",  
                       webenv=webenv,
                       query_key=query_key)
    out_handle = open("data/"+keyword, "w")
    data = handle.read()
    (id_list)
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list 

import re 
import csv 
import matplotlib.pyplot as plt
from collections import Counter

def science_plots(data):
    """
    Funcion que pide como entrada la busqueda de la funcion download_pubmeds y como resultado muestra un grafico de pastel 
    indicando a los cinco paises de origen de autores que aparecieron mas veces  . 
    """ 
    with open("data/"+data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    unique_countries = list(set(countries_1))
    conteo=Counter(countries_1)
    resultado={} ##creamos un diccionario vacio 
    ## Bucle agregamos los valores del diccionario
    for clave in conteo:
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ## ordenamos de forma ascendente 
    ## ordenamos de forma ascendente 
    sort = (sorted(resultado.values()))
    sort.sort(reverse=True) 
    import operator
    ## creamos dos listas vacias  
    pais = [] 
    frecuencia = []
    
    ## bucle que añade los valores pais y frecuencia a la listas vacias pais y frecuencia
    reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        pais.append(name[1][0])
        frecuencia.append(resultado[name[1][0]])
    max_pais = pais[0:5] ## seleccionamos los cinco primeros paises 
    max_frec = frecuencia [0:5] ## seleccionamos las cinco primero frecuencia respecto a los paises 
    fig = plt.figure(figsize =(10, 8))
    plt.pie(max_frec, labels = max_pais)
    (plt.savefig("img/"+data, dpi=100, bbox_inches='tight'))
    plt.show()
    



