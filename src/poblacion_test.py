from poblacion import lee_poblaciones
datos = lee_poblaciones('data/population.csv')
print(datos)
pass 

from poblacion import calcula_paises
def test_calcula_paises(datos):
    print("*** Calcula Países ***")
    paises_ordenados = calcula_paises(datos)
    prnti(calcula_paises)




