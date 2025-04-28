import random
import time


# Función para generar una cadena válida según la gramática S -> aSb | ε
def generate_valid_string(existing_strings):
    """
    Genera una cadena válida que pertenece al lenguaje definido por la gramática:
    S -> aSb | ε

    Parámetros:
    existing_strings (set): Conjunto de cadenas generadas para evitar duplicados.

    Retorna:
    str: Una cadena válida perteneciente al lenguaje.
    """
    while True:
        n = random.randint(0, 10)  # Permitir vacío y limitar el tamaño máximo
        if n == 0:
            string = ""
        else:
            string = "a" * n + "b" * n  # Construcción directa en vez de mezclar subcadenas

        if string not in existing_strings:  # Verifica que no haya repetidos
            existing_strings.add(string)
            return string


# Función para modificar una cadena válida y hacerla inválida
def mutate_invalid_string(string):
    """
    Modifica una cadena válida para hacerla inválida de manera más robusta.

    Parámetros:
    string (str): Cadena válida que se modificará.

    Retorna:
    str: Una cadena inválida generada a partir de una válida.
    """
    if len(string) > 1:
        string = list(string)
        indices = list(range(len(string)))
        random.shuffle(
            indices
        )  # Mezclar los índices para intercambiar posiciones al azar

        # Realizar múltiples intercambios en la cadena
        for _ in range(min(3, len(string) // 2)):
            i, j = random.sample(indices, 2)
            string[i], string[j] = string[j], string[i]

        string = "".join(string)
    return string


# Función para generar una cadena que no pertenezca al lenguaje
def generate_invalid_string(existing_strings, used_patterns):
    """
    Genera una cadena inválida que no pertenece al lenguaje.

    Parámetros:
    existing_strings (set): Conjunto de cadenas generadas para evitar duplicados.
    used_patterns (set): Conjunto de patrones ya utilizados para evitar repeticiones.

    Retorna:
    str: Una cadena que no pertenece al lenguaje.
    """
    while True:
        prob = random.random()
        if prob < 0.75:  # 75% de probabilidad de usar la forma ya implementada
            length = random.randint(
                4, 25)  # Aumentado el límite superior de caracteres
            string = ''.join(random.choices(
                'ab', k=length))  # Crea una cadena aleatoria de 'a' y 'b'
        elif prob < 0.80:  # 5% de probabilidad de obtener solo 'a' o solo 'b'
            string = random.choice(['a', 'b']) * random.randint(1, 10)
        else:
            # Generar patrones repetitivos como "abababa", "aabaabaabaa", "bbabbabbabba", "aaabbb", "bbbaaa"
            available_patterns = ["ab", "aab", "bba", "aaabbb", "bbbaaa"]
            if len(used_patterns) < len(available_patterns):
                pattern_type = random.choice(
                    [p for p in available_patterns if p not in used_patterns])
                used_patterns.add(
                    pattern_type
                )  # Registrar el patrón utilizado para evitar repeticiones
            else:
                pattern_type = random.choice(
                    available_patterns
                )  # Si ya se usaron todos, permitir repetición

            length = random.randint(4, 25)
            string = (pattern_type * (length // len(pattern_type) + 1)
                      )[:length]  # Ajusta la longitud

        count_a = string.count('a')
        count_b = string.count('b')

        # Si la cadena generada sigue la forma válida a^n b^n, la invalida mediante mutación
        if count_a == count_b and string[:count_a] == 'a' * count_a and string[
                count_a:] == 'b' * count_b:
            string = mutate_invalid_string(string)

        if string not in existing_strings:  # Asegura que la cadena no se haya generado antes
            existing_strings.add(string)
            return string


# Nueva función para obtener las cadenas mezcladas sin imprimirlas
def get_shuffled_strings():
    """
    Genera una lista con 4 cadenas válidas y 4 inválidas, mezcladas aleatoriamente.

    Retorna:
    list: Lista de 8 cadenas en orden aleatorio.
    """
    random.seed(
        time.time())  # Cambia la semilla en cada ejecución para más variedad
    existing_strings = set(
    )  # Conjunto para almacenar cadenas generadas y evitar duplicados
    used_patterns = set()  # Conjunto para almacenar patrones ya utilizados

    valid_strings = [
        generate_valid_string(existing_strings) for _ in range(4)
    ]  # Genera 4 cadenas válidas
    invalid_strings = [
        generate_invalid_string(existing_strings, used_patterns)
        for _ in range(4)
    ]  # Genera 4 cadenas inválidas

    # Mezclar las cadenas de forma aleatoria
    all_strings = valid_strings + invalid_strings
    random.shuffle(all_strings)

    return all_strings  # No imprime nada, solo devuelve la lista


# Función principal que genera y muestra cadenas válidas e inválidas
def main():
    """
    Función principal que genera y muestra cadenas válidas e inválidas.
    """
    random.seed(
        time.time())  # Cambia la semilla en cada ejecución para más variedad
    existing_strings = set(
    )  # Conjunto para almacenar cadenas generadas y evitar duplicados
    used_patterns = set()  # Conjunto para almacenar patrones ya utilizados

    valid_strings = [
        generate_valid_string(existing_strings) for _ in range(4)
    ]  # Genera 4 cadenas válidas
    invalid_strings = [
        generate_invalid_string(existing_strings, used_patterns)
        for _ in range(4)
    ]  # Genera 4 cadenas inválidas

    print("Valid chains:")
    for s in valid_strings:
        print(f"String: '{s}'")  # Imprime cada cadena válida

    print("\nInvalid chains:")
    for s in invalid_strings:
        print(f"String: '{s}'")  # Imprime cada cadena inválida


# Punto de entrada del programa
if __name__ == "__main__":
    main()
