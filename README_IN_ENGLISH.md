## Members:

- Kadiha Muhamad Orta
- David Alejandro Gutierrez Leal

- **Class code:** 7308

**Operating System:** Windows 10

**Programming language used:** Python 3.12

**Tools:** PyCharm 2024.2.4/ onlineGDB


# ALGORITHM#1 String Generation According to Grammar S -> aSb | ε
## Description:
This code implements a Python algorithm that generates valid and invalid strings according to the grammar:
```
S -> aSb | ε
```

The generated strings can follow the correct structure of the grammar (valid) or be altered so that they do not belong to the language (invalid).

## Code structure
The source code is located in the `Scripts` folder and the main file is:
```
Scripts/ALGORITHM_1_LFCO_2025_DG_KM.py
```


## Execution Instructions

To run the algorithm, follow these steps:

1. Clone the repository from GitHub:
   ```sh
   git clone < URL_OF_REPOSITORY >
   ```

2. Access the project folder:
   ```sh
   cd < PROJECT_NAME >/Scripts
   ```

3. Make sure you have Python installed. You can check it with:
   ```sh
   python --version
   ```

4. Execute the script:
   ```sh
   python ALGORITHM_1_LFCO_2025_DG_KM.py
   ```

## Explanation of the Algorithm

The algorithm has the following main functions:
- **`generate_valid_string(existing_strings)`**: Generates a valid string that follows the form `a^n b^n`.
- **`mutate_invalid_string(string)`**: Modifies a valid string to make it invalid by altering its structure.
- **`generate_invalid_string(existing_strings, used_patterns)`**: Creates invalid strings using different strategies (messing up characters, incorrect patterns, etc.).
- **`get_shuffled_strings()`**: Generates and mixes valid and invalid strings without printing them.
- **`main()`**: It generates 4 valid and 4 invalid strings, and prints them on the console.

## Output Example
Running the script, you could get a result similar to:
```
Valid chains:
String: 'aabb'
String: 'aaaabbbb'
String: 'ab'
String: ''

Invalid chains:
String: 'abab'
String: 'bbaa'
String: 'aaaabb'
String: 'bbbbaaaa'
```

# ALGORITHM#2 PDA: Deterministic Stack Automata

This code implements a Deterministic Stack Automaton (DSA) that checks if a string follows the pattern of 'a's followed by the same amount of 'b's.
## Requirements
This code is developed in Python and does not require external libraries.
## Installation
Clone the repository on your local machine:
```bash
git clone < URL_OF_REPOSITORY >
cd Project
```

## Use
Run the `ALGORITHM_2_LFCO_2025_DG_KM.py` script to parse the strings generated by ` ALGORITHM_1_LFCO_2025_DG_KM.py`:
```bash
python Scripts/ALGORITHM_2_LFCO_2025_DG_KM.py
```
The program will show whether each string is accepted or rejected by the PDA.

## PDA Description
The PDA operates with the following states and transitions:
- State `q0`:
- If it reads `a`, it stacks it and remains at `q0`.
- If it reads `b`, it switches to `q1` and unstacks.

- State `q1`:
- If it reads `b`, it continues unstacking.
- If the stack is empty at the end, the string is accepted.

## Operation of the Program
1. The `ALGORITHM_1_LFCO_2025_DG_KM.py` script generates strings with combinations of 'a' and 'b'.
2. `ALGORITHM_2_LFCO_2025_DG_KM.py` processes each string and determines if it meets the expected grammar.
## Output Example
```bash
Results of the analysis by the PDA
String: 'aabb' is accepted by the PDA.
String: 'abab' is rejected by the PDA.
String: 'aaabb' is rejected by the PDA.
```

# ALGORITMO#3 PDA Tracer

## Description
This code implements a Deterministic Stack Automaton (DSA) that processes strings generated by `ALGORITHM_1_LFCO_2025_DG_KM.py ` and filtered by `ALGORITHM_2_LFCO_2025_DG_KM.py`. In addition, it records the execution step by step, showing the applied rules, stack changes and automaton configurations.

## Requirements
To execute the code, it is necessary to install the following libraries:
```sh
pip install tabulate
```

## Archives
- `ALGORITHM_1_LFCO_2025_DG_KM.py`: Generates random strings based on a specified grammar.
- `ALGORITHM_2_LFCO_2025_DG_KM.py`: Filters the strings generated by `Algorithm_1`.
- `ALGORITHM_3_LFCO_2025_DG_KM.py`: Implements the PDA with traceability and visualization of applied rules.

## Use
Run `ALGORITHM_3_LFCO_2025_DG_KM.py` to process the strings and display the transition history:
```sh
python ALGORITHM_3_LFCO_2025_DG_KM.py
```

The program will display:
1. The PDA rules.
2. The accepted strings.
3. A detailed record of the step-by-step process in table format.

## Expected output
Example of program output:
```
PDA Rules:
1: (q0, a) -> push
2: (q0, b) -> pop
3: (q1, b) -> pop

Accepted string: aabb
+--------+-------+--------------+
| Tree   | Stack | Rules        |
+--------+-------+--------------+
| aabb   | a     | (q0, a) -> push |
| abb    | aa    | (q0, a) -> push |
| bb     | a     | (q0, b) -> pop  |
| b      |       | (q1, b) -> pop  |
|        |       | end        |
+--------+-------+--------------+
```
	
	
	

