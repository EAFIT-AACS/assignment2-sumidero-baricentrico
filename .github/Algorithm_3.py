import Algorithm_1
import Algorithm_2
from tabulate import tabulate

class PDA_Tracer(Algorithm_2.PDA):
    """
    Extiende la clase PDA para registrar la ejecución del autómata,
    guardando el historial de transiciones, cambios en la pila y reglas aplicadas.
    """
    def __init__(self):
        super().__init__()
        self.history = []
        self.rules = {
            1: "(q0, a) -> push",  # Leer 'a' y apilar
            2: "(q0, b) -> pop",   # Leer 'b' y desapilar
            3: "(q1, b) -> pop"    # Continuar desapilando con 'b'
        }

    def process_symbol(self, state, symbol):
        """
        Procesa un símbolo y guarda la configuración en la historia con la regla aplicada.
        """
        result = super().process_symbol(state, symbol)
        rule_applied = self.get_rule(state, symbol)
        self.history.append([''.join(self.input_string), ''.join(self.stack), rule_applied])
        self.input_string = self.input_string[1:]  # Reducir la cadena
        return result

    def process_string(self, input_string):
        """
        Procesa una cadena completa y almacena el historial.
        """
        self.history = []
        self.input_string = input_string  # Almacena la cadena en proceso
        state = self.starting_state
        for symbol in input_string:
            state = self.process_symbol(state, symbol)
            if state is None:
                return False
        self.history.append([self.input_string, ''.join(self.stack), "Final"])
        return len(self.stack) == 0

    def get_rule(self, state, symbol):
        """
        Obtiene la regla aplicada en la transición basada en Algorithm_2.
        """
        transitions_to_rules = {
            ("q0", "a"): 1,  # (q0, a) -> push
            ("q0", "b"): 2,  # (q0, b) -> pop
            ("q1", "b"): 3   # (q1, b) -> pop
        }
        return transitions_to_rules.get((state, symbol), "Unknown")

def display_rules(pda_tracer):
    """
    Muestra las reglas del PDA enumeradas antes de procesar las cadenas.
    """
    print("\nReglas del PDA:")
    for num, rule in pda_tracer.rules.items():
        print(f"{num}: {rule}")

def display_trace(input_string, tracer):
    """
    Muestra la configuración del autómata paso a paso en un formato más claro.
    """
    table_data = []
    for index, (tree, stack, rule) in enumerate(tracer.history):
        table_data.append([index, tree, stack, rule])

    print(f"\nCadena aceptada: {input_string}")
    print(tabulate(table_data, headers=["Tree", "Stack", "Rules"], tablefmt="grid"))

def main():
    """
    Ejecuta el PDA con las cadenas generadas por Algorithm_1 y filtradas por Algorithm_2.
    """
    pda_tracer = PDA_Tracer()

    # Mostrar reglas antes de procesar las cadenas
    display_rules(pda_tracer)

    generated_strings = Algorithm_1.get_shuffled_strings()
    accepted_strings = [s for s in generated_strings if Algorithm_2.PDA().process_string(s)]

    for string in accepted_strings:
        pda_tracer.process_string(string)
        display_trace(string, pda_tracer)

if __name__ == "__main__":
    main()
