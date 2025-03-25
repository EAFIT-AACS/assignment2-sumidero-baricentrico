import Algorithm_1  # Importamos el archivo que genera las cadenas


class PDA:
    """
    Implementa un Autómata de Pila Determinista (PDA) que reconoce cadenas de la gramática G.
    Este autómata verifica si una cadena sigue el patrón de 'a's seguidas por la misma cantidad de 'b's.
    """

    def __init__(self):
        """Inicializa la pila, el estado inicial y define las transiciones del PDA."""
        self.starting_state = "q0"  # Estado inicial
        self.stack = []  # Pila vacía al inicio
        self.transitions = {
            ("q0", "a"): ("q0", "push"),  # Al leer 'a', apilar en la pila
            ("q0", "b"): ("q1", "pop"),  # Al leer 'b', cambiar de estado y desapilar
            ("q1", "b"): ("q1", "pop")  # Continuar desapilando con cada 'b'
        }

    def process_symbol(self, state, symbol):
        """
        Procesa un símbolo de la cadena y realiza la transición correspondiente.

        Parámetros:
        - state: Estado actual del autómata.
        - symbol: Símbolo actual de la cadena.

        Retorna:
        - El nuevo estado si la transición es válida.
        - None si la transición no es válida, lo que indica que la cadena es rechazada.
        """
        if (state, symbol) in self.transitions:
            new_state, action = self.transitions[(state, symbol)]

            if action == "push":
                self.stack.append("a")  # Apilar 'a' en la pila
            elif action == "pop":
                if self.stack:
                    self.stack.pop()  # Desapilar si hay elementos
                else:
                    return None  # Si la pila está vacía y se intenta desapilar, la cadena es inválida

            return new_state  # Retornar el nuevo estado
        return None  # Si la transición no está definida, la cadena es inválida

    def process_string(self, input_string):
        """
        Procesa una cadena completa y determina si es aceptada por el PDA.

        Parámetros:
        - input_string: Cadena a evaluar.

        Retorna:
        - True si la cadena es aceptada (pila vacía al final).
        - False si la cadena es rechazada.
        """
        self.stack = []  # Reiniciar la pila antes de procesar la cadena
        state = self.starting_state  # Estado inicial

        for symbol in input_string:
            state = self.process_symbol(state, symbol)
            if state is None:
                return False  # Si encontramos un error en las transiciones, la cadena es inválida

        return len(self.stack) == 0  # La pila debe quedar vacía al final para ser aceptada


def main():
    """
    Función principal que obtiene las cadenas generadas por Algorithm_1 y las evalúa con el PDA.
    """
    pda = PDA()

    # Obtener las cadenas generadas desde Algorithm_1
    strings = Algorithm_1.get_shuffled_strings()

    print("Resultados del análisis por el PDA:")
    for s in strings:
        resultado = "es aceptado" if pda.process_string(s) else "es rechazado"
        print(f"String: '{s}' {resultado} por el PDA.")


if __name__ == "__main__":
    main()
