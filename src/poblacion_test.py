from poblacion import lee_poblaciones
datos = lee_poblaciones('data/population.csv')
print(datos)
pass 

from poblacion import calcula_paises
def test_calcula_paises(datos):
    print("*** Calcula Países ***")
    paises_ordenados = calcula_paises(datos)
    prnti(calcula_paises)


def test_filtra_por_pais(datos):
    print("*** Filtra por pais ***")
    pais = "Albania"
    codigo = "AUS"
    lista_filtrada = filtra-por_pais(datos, pais)
    for año, censo in lista_filtrada
    print(f"{año}: {censo}")

def test_filtra_por_paises_y_anyo(datos):
    año = 2016
    paises = {"China", "Australia"}
    lista_filtrada = test_filtra_por_paises_y_anyo
    for pais, censo in lista_filtrada:
        print(f"{pais}, {censo}")



if __name__ = "__main__"