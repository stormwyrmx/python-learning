import gate

def _gate(gate_type):
    if gate_type == 'and':
        print("and:--------------")
        print(gate.and_gate(0, 0))
        print(gate.and_gate(1, 0))
        print(gate.and_gate(0, 1))
        print(gate.and_gate(1, 1))
    elif gate_type == 'or':
        print("or:--------------")
        print(gate.or_gate(0, 0))
        print(gate.or_gate(1, 0))
        print(gate.or_gate(0, 1))
        print(gate.or_gate(1, 1))
    elif gate_type == 'nand':
        print("nand:--------------")
        print(gate.nand_gate(0, 0))
        print(gate.nand_gate(1, 0))
        print(gate.nand_gate(0, 1))
        print(gate.nand_gate(1, 1))
    elif gate_type == 'xor':
        print("xor:--------------")
        print(gate.xor_gate(0, 0))
        print(gate.xor_gate(1, 0))
        print(gate.xor_gate(0, 1))
        print(gate.xor_gate(1, 1))
    else:
        print('Invalid gate type')

_gate('and')
_gate('or')
_gate("nand")
_gate("xor")
