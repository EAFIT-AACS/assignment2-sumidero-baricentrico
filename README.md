## Integrantes:

- Kadiha Muhamad Orta
- David Alejandro Gutiérrez Leal

- **Código de clase:** 7308
  
**Sistema Operativo:** Windows 10

**Lenguaje de programación utilizado:** Python 3.12

**Herramientas:** PyCharm 2024.2.4 / onlineGDB

# ALGORITMO#1 Generación de Cadenas Según Gramática S -> aSb | ε

## Descripción
Este código implementa un algoritmo en Python que genera cadenas válidas e inválidas según la gramática:

```
S -> aSb | ε
```

Las cadenas generadas pueden seguir la estructura correcta de la gramática (válidas) o ser alteradas para no pertenecer al lenguaje (inválidas). 

## Estructura del código
El código fuente se encuentra en la carpeta `Scripts` y el archivo principal es:

```
Scripts/Algorithm_1.py
```


## Instrucciones de Ejecución
Para ejecutar el algoritmo, sigue estos pasos:

1. Clona el repositorio desde GitHub:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Accede a la carpeta del proyecto:
   ```sh
   cd <NOMBRE_DEL_PROYECTO>/Scripts
   ```

3. Asegúrate de tener Python instalado. Puedes verificarlo con:
   ```sh
   python --version
   ```

4. Ejecuta el script:
   ```sh
   python Algorithm_1.py
   ```

## Explicación del Algoritmo

El algoritmo tiene las siguientes funciones principales:

- **`generate_valid_string(existing_strings)`**: Genera una cadena válida que sigue la forma `a^n b^n`.
- **`mutate_invalid_string(string)`**: Modifica una cadena válida para hacerla inválida alterando su estructura.
- **`generate_invalid_string(existing_strings, used_patterns)`**: Crea cadenas inválidas usando diferentes estrategias (desorden de caracteres, patrones incorrectos, etc.).
- **`get_shuffled_strings()`**: Genera y mezcla cadenas válidas e inválidas sin imprimirlas.
- **`main()`**: Genera 4 cadenas válidas y 4 inválidas, y las imprime en la consola.

## Ejemplo de Salida
Ejecutando el script, podrías obtener un resultado similar a:

```
Cadenas válidas:
String: 'aabb'
String: 'aaaabbbb'
String: 'ab'
String: ''

Cadenas inválidas:
String: 'abab'
String: 'bbaa'
String: 'aaaabb'
String: 'bbbbaaaa'
```

# ALGORITMO#2 PDA: Autómata de Pila Determinista

Este código implementa un Autómata de Pila Determinista (PDA) que verifica si una cadena sigue el patrón de 'a's seguidas por la misma cantidad de 'b's.

## Requisitos
Este código está desarrollado en Python y no requiere bibliotecas externas.

## Instalación
Clona el repositorio en tu máquina local:
```bash
git clone <URL_DEL_REPOSITORIO>
cd Proyecto
```

## Uso
Ejecuta el script `Algorithm_2.py` para analizar las cadenas generadas por `Algorithm_1.py`:
```bash
python Scripts/Algorithm_2.py
```
El programa mostrará si cada cadena es aceptada o rechazada por el PDA.

## Descripción del PDA
El PDA funciona con los siguientes estados y transiciones:
- Estado `q0`:
  - Si lee 'a', la apila y permanece en `q0`.
  - Si lee 'b', cambia a `q1` y desapila.
- Estado `q1`:
  - Si lee 'b', sigue desapilando.
  - Si la pila queda vacía al final, la cadena es aceptada.

## Funcionamiento del Programa
1. El script `Algorithm_1.py` genera cadenas con combinaciones de 'a' y 'b'.
2. `Algorithm_2.py` procesa cada cadena y determina si cumple la gramática esperada.

## Ejemplo de Salida
```bash
Resultados del análisis por el PDA:
String: 'aabb' es aceptado por el PDA.
String: 'abab' es rechazado por el PDA.
String: 'aaabb' es rechazado por el PDA.
```


