# Algoritmo Genético para Encontrar una Palabra Objetivo
Este repositorio contiene una implementacion de un algoritmo genetico diseñado para encontrar una palabra objetivo a partir de una poblacion inicial de cadenas aleatorias.

# Descripcion
Un algoritmo genetico es una tecnica de optimizacion inspirada en la evolucion biologica. En este caso, se usa para generar palabras que se aproximan progresivamente a una palabra objetivo mediante los principios de:
- Seleccion natural: Se eligen los mejores individuos.
- Cruce: Se combinan caracteristicas de los padres.
- Mutacion: Se introducen pequeñas variaciones aleatorias.
El programa ejecuta iteraciones hasta que se encuentra la palabra objetivo o se alcanza un nimero maximo de generaciones.

# Funcionamiento
- Generacion inicial: Se crea una poblacion de palabras aleatorias.
- Evaluacion: Se calcula la aptitud (fitness) de cada individuo, basada en la cantidad de letras correctas en la posicion correcta.
- Seleccion: Se eligen los mejores individuos para reproducirse.
- Cruzamiento: Se combinan dos individuos para generar descendencia.
- Mutacion: Se aplican cambios aleatorios a algunos caracteres.
- Repeticion: Se generan nuevas generaciones hasta encontrar la palabra objetivo.

# Personalizacion
- objetivo: La palabra que quieres encontrar.
- tamano_poblacion: Cantidad de individuos en cada generacion.
- generaciones_max: Número maximo de generaciones.
- tasa_mutacion: Probabilidad de mutacion en cada individuo.
