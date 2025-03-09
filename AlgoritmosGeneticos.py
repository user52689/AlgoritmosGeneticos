import random
import string

def calcular_fitness(individuo, objetivo):
    return sum(1 for i, c in enumerate(individuo) if c == objetivo[i])

def generar_individuo(longitud):
    return ''.join(random.choices(string.ascii_uppercase, k=longitud))

def generar_poblacion(tamano, longitud_objetivo):
    return [generar_individuo(longitud_objetivo) for _ in range(tamano)]

def cruzar(padre1, padre2):
    punto_corte = random.randint(1, len(padre1) - 1)
    return padre1[:punto_corte] + padre2[punto_corte:]

def mutar(individuo, tasa_mutacion=0.1):
    if random.random() < tasa_mutacion:
        indice = random.randint(0, len(individuo) - 1)
        nueva_letra = random.choice(string.ascii_uppercase)
        individuo = individuo[:indice] + nueva_letra + individuo[indice+1:]
    return individuo

def algoritmo_genetico(objetivo, tamano_poblacion=100, generaciones_max=1000, tasa_mutacion=0.1):
    longitud_objetivo = len(objetivo)
    poblacion = generar_poblacion(tamano_poblacion, longitud_objetivo)

    for generacion in range(generaciones_max):
        poblacion = sorted(poblacion, key=lambda x: calcular_fitness(x, objetivo), reverse=True)

        mejor_individuo = poblacion[0]
        mejor_fitness = calcular_fitness(mejor_individuo, objetivo)
        fitness_promedio = sum(calcular_fitness(ind, objetivo) for ind in poblacion) / tamano_poblacion

        # 🔹 Mostrar el mejor individuo y la aptitud promedio en cada generacion
        print(f"Generacion {generacion}: Mejor = {mejor_individuo}, Aptitud Promedio = {fitness_promedio:.2f}")

        if mejor_fitness == longitud_objetivo:
            print(f"Encontrado en generacion {generacion}: {mejor_individuo}")
            return mejor_individuo

        nueva_poblacion = poblacion[:10]  # Selección de élite
        while len(nueva_poblacion) < tamano_poblacion:
            padre1, padre2 = random.sample(poblacion[:50], 2)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo, tasa_mutacion)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    print("No se encontro la palabra objetivo.")
    return None

objetivo = "OBJETIVO"
algoritmo_genetico(objetivo)