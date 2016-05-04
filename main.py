import random
global goal_value

code_tab = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', '+': '1010', '-': '1011', '*': '1100', '/': '1101',
            '0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': '+', '1011': '-', '1100': '*', '1101': '/', '1110': ' ', '1111': ' '}


class Member:
    """ member of the population of equations :) """
    def __init__(self, equation):
        self.equation = equation
        self.chromosome = ''
        self.fitness_score = 0.0
        self.roulette_value = 0
        self.encode(self.equation)

    def encode(self, equation):
        for char in equation:
            for code in code_tab:
                if (char == code):
                    self.chromosome += code_tab[char]
                    break

def decode(chromosome):
    equation = ''
    gene = ''
    counter = 1
    # decode chromosome
    for char in chromosome:
        gene += char
        if (counter % 4 == 0):
            equation += code_tab[gene]
            gene = ''
        counter += 1
    return equation

def generate_equation(length, binary):
    equation = ''
    if(binary == True):
        for i in range(length):
            equation += random.choice('01')
    else:
        for i in range(length):
            equation += random.choice('0123456789+-*/')
    return equation

def generate_population(generation_size, member_size, binary):
    population = []
    for i in range(generation_size):
        equation = generate_equation(member_size, binary)
        population.insert(i, Member(equation))
    return population


def calculate(member):
    equation = member.equation
    sanitized_equation = ''
    number = True
    counter = 0

    print('calculate: ' + equation)
    #step 1: check order
    for char in equation:
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
    if len(sanitized_equation) > 1:
        check_ok = False
        while(check_ok == False):
            last_character = sanitized_equation[len(sanitized_equation) - 1]
            if(ord(last_character) >= ord('0') and ord(last_character) <= ord('9')):
                check_ok = True
            else:
                new_equation = sanitized_equation[:(len(sanitized_equation) - 1)]
                sanitized_equation = new_equation

    #step 3: remove divide by zero
    equation_helper = sanitized_equation
    if '/0' in equation_helper:
        sanitized_equation = equation_helper.replace('/0', '')

    #step 4: return equation string
    return sanitized_equation

def fitness_score(member):
    equation = calculate(member)
    equation_result = 0.0
    if len(equation) > 0:
        equation_result = eval(equation)
    else:
        equation_result = (goal_value + 9999) * 9999

    fitness_result = 0.0
    if equation_result == goal_value:
        fitness_result = 1
    else:
        fitness_result = 1 / (goal_value - equation_result)

    member.fitness_score = fitness_result
    return fitness_result

def roulette_wheel(population):
    print('roulette_wheel')
    fitness_score_sum = 0
    for member in population:
        member.roulette_value = int(member.fitness_score * 100000)
        fitness_score_sum += member.roulette_value
        print('member ' + str(member.roulette_value))
    print('fitness_score_sum ' + str(int(fitness_score_sum)))

    roulette_ball = random.randint(1, fitness_score_sum)
    print('roulette_ball ' + str(roulette_ball))

    output_member = Member('+++++++')
    counter = 0
    for member in population:
        counter += member.roulette_value
        if counter >= roulette_ball:
            output_member = member
            print(output_member.roulette_value)
            break

    return output_member

def mutation(chromosome):
    # mutation of single gene
    new_chromosome = ''
    for gene in chromosome:
        mutation_chance = random.randint(0, 1000)
        if mutation_chance == 1000:
            if gene == '0':
                new_chromosome += '1'
            else:
                new_chromosome += '0'
        else:
            new_chromosome += gene
    return new_chromosome

def fitness_score_population(population):
    for i in range(len(population)):
        fitness_score(population[i])

#-------------------------PROGRAM---------------------------
goal_value = 25
population_size = 3000
member_size = 7
binary = False
population = []
population = generate_population(population_size, member_size, binary)
fitness_score_population(population)

new_population = []
#for i in range(population_size):


# take 2 members and create new one from them
reproductor_1 = roulette_wheel(population).chromosome
reproductor_2 = roulette_wheel(population).chromosome

print('reproductor_1: ' + reproductor_1)
print('reproductor_2: ' + reproductor_2)

#crossover
crossover_random = random.randint(1, 28)
print('crossover_random' + str(crossover_random))
offspring_chrome = reproductor_1[0:crossover_random] + reproductor_2[crossover_random: 4 * member_size]

print('offspring: ' + offspring_chrome)

#mutation of single gene
new_chromosome = mutation(offspring_chrome)

print('mutation   ' + new_chromosome)

offspring_equation = decode(new_chromosome)

new_member = Member(offspring_equation)
fitness_score(new_member)

new_population.insert(0, new_member)





