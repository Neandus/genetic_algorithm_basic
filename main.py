import random

code_tab = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', '+': '1010', '-': '1011', '*': '1100', '/': '1101',
            '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': '+', '1011': '-', '1100': '*', '1101': '/'}

def generate_member(length, binary):
    member = ''
    if(binary == True):
        for i in range(length):
            member += random.choice('01')
    else:
        for i in range(length):
            member += random.choice('0123456789+-*/')
    return member

def generate_population(generation_size, member_size, binary):
    population = []
    for i in range(generation_size):
        population.insert(i, generate_member(member_size, binary))
    return population

def encode(equation):
    chromosome = ''
    for char in equation:
        for code in code_tab:
            if(char == code):
                chromosome += code_tab[char]
                break
    return chromosome

def decode(chromosome):
    equation = ''
    gene= ''
    counter = 1
    #decode chromosome
    for char in chromosome:
        gene += char
        if(counter % 4 == 0):
            equation += code_tab[gene]
            gene=''
        counter += 1
    return equation

def calculate(equation):
    sanitized_equation = ''
    number = True
    counter = 0
    print('equation' + str(equation))

    #step 1: check order
    for char in equation:
        print(char)
        if(number == True):
            if (ord(char) >= ord('0') and ord(char) <= ord('9')):
                sanitized_equation += char
                number = False
        else:
            if ord(char) == ord('+') or ord(char) == ord('-') \
            or ord(char) == ord('*') or ord(char) == ord('/'):
                sanitized_equation += char
                number = True

    #step 2: remove operation as last character
    check_ok = False
    while(check_ok == False):
        last_character = sanitized_equation[len(sanitized_equation) - 1]
        if(ord(last_character) >= ord('0') and ord(last_character) <= ord('9')):
            check_ok = True
        else:
            new_equation = sanitized_equation[:(len(sanitized_equation) - 1)]
            sanitized_equation = new_equation

    #step 3: remove divide by zero

    print('sanitized_equation' + str(sanitized_equation))
    equation_result = eval(sanitized_equation)
    print('equation_result' + str(equation_result))
    return equation_result

population_size = 3
member_size = 7
binary = False
population = []
population = generate_population(population_size, member_size, binary)
for i in range(population_size):
    result = calculate(population[i])
    print(encode(population[i]) + ' <-> ' + population[i] + ' = ' + str(result))
