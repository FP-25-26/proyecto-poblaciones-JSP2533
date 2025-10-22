from collections import namedtuple
import csv
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    poblaciones = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)

        for pais, codigo, año, censo in lector:
            try:
                año = int(año)
                censo = int(censo)
                poblaciones.append(RegistroPoblacion(pais, codigo, año, censo))
            except ValueError:
                
                continue

    return poblaciones




def calcula_paises(poblaciones):
    conjunto_paises = set()
    for tupla_reg_pob in poblaciones:
        conjunto_paises.add(tupla_reg_pob.pais)
    return sorted(conjunto_paises)


def filtra_por_pais(poblaciones, nombre_o_codigo):
    lista_filtrada = []
    for p in poblaciones:
        if p.pais == nombre_o_codigo or p.codigo == nombre_o_codigo:
            tupla = (p.año, p.censo)
            lista_filtrada.append(tupla)
        return lista_filtrada

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    lista_filtrada = []
    for p in poblaciones:
        if p.año == anyo and p.pais in paises:
            tupla = (p.pais, p.censo)
            lista_filtrada.append(tupla)
    return lista_filtrada




#def filtra_por_paises_y_anyo(poblaciones, anyo, paises):




#def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):