
#Implement bidirectional dictionary?
code_tab = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', '+': '1010', '-': '1011', '*': '1100', '/': '1101',
            '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': '+', '1011': '-', '1100': '*', '1101': '/'}

def encode(equation):
    chromosome = ''
    for char in equation:
        for code in code_tab:
            if(char == code):
                chromosome += ' ' + code_tab[char]
                break
    return chromosome

def decode(chromosome):
    print('decode')
    #decode the chromosome, but keep equation sense...

equ = "6-7+9"
chro = encode(equ)
print(equ)
print(chro)

decode(chro)