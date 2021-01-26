#open file path w/ cd Documents/CY300

# Day 1 Part 1

def decipher(code):
    with open(code, 'r') as file_:
        lines = file_.readlines()

        for line in lines:
            line = int(line)
            for other in lines:
                other = int(other)
                hope = other + line
                if hope == 2020:
                    print(other, line)
decipher('numbers.txt')

print(1402*618)


# Day 1 Part 2

def decipher2(code):
    with open(code, 'r') as file_:
        lines = file_.readlines()

        for line in lines:
            line = int(line)
            for other in lines:
                other = int(other)
                for last_one in lines:
                    last_one = int(last_one)
                    hope = other + line + last_one
                    if hope == 2020:
                        print(other, line, last_one)  
decipher2('numbers.txt')

print(547*545*928)





# Day 2 Part 1

def password_puzz(name):
    legit_passwords = 0
    appearance = 0
    with open(name, 'r') as file_:
        file_1 = file_.readlines()
        for line in file_1:
            break_line = line.split()
            policy = break_line[0]
            letter = break_line[1][0]
            password = break_line[2]
            policy = policy.split('-')
            least = int(policy[0])
            most = int(policy[1])

            for char in password:
                if char == letter:
                    appearance += 1
            if appearance >= least and appearance <= most:
                legit_passwords += 1
            appearance = 0
    return legit_passwords

print(password_puzz('day2input.txt'))


# Day 2 Part 2

def password_puzzle(name):
    appearance = 0
    with open(name, 'r') as file_:
        file_1 = file_.readlines()
        for line in file_1:
            break_line = line.split()
            policy = break_line[0]
            letter = break_line[1][0]
            password = break_line[2]
            policy = policy.split('-')
            position1 = int(policy[0]) - 1
            position2 = int(policy[1]) - 1

            print(password[position1], 'and', letter)

            if password[position1] == letter and password[position2] == letter:
                print('worthless')
            elif password[position1] == letter:
                appearance += 1
            elif password[position2] == letter:
                appearance += 1
    return appearance

print(password_puzzle('day2input.txt'))





# Day 3 Parts 1 and 2

answer = 1
pattern = [(1,1), (3,1), (5,1), (7,1), (1,2)]

list_ = []
with open('trees.txt', 'r') as file_:
    file_ = file_.readlines()

    for line in file_:
        list_.append(line.strip())

    for values in pattern:
        first = 0
        second = 0
        score_count = 0

        while len(list_) > second :
            first += values[0]
            second += values[1]
            if second < len(list_) and list_[second][first%len(list_[second])] == '#':
                score_count += 1
        answer = answer * score_count

        if values[0] == 3 and values[1] == 1:
            print(score_count)

    print(answer)





# Day 5 Parts 1 and 2

# Variables
first = None
second = None

verif = set()

# Solve
with open('puzzle5.txt', 'r') as file_:
    file_ = file_.readlines()

    for line in file_:
        line = line.strip()

        row = 0
        f = 64
        column = 0
        c = 4

        for letter in line:
            if letter == 'B':
                row = row + f
                f = f / 2
            elif letter == 'F':
                f = f / 2

            if letter == 'R':
                column = column + c
                c = c / 2
            elif letter == 'L':
                c = c / 2

        seat = column + row * 8 
        verif.add(seat)

        if first:
            first = max(first, seat)
        else: 
            first = seat

    for face in sorted(verif):

        if face + 1 not in verif and face + 2 in verif:
            second = face + 1

    print(int(first), 'and', int(second))





# Day 6 part 1

total = 0       
def distinct(resp):
    quest = []

    for char in resp:
        if char not in quest:
            quest.append(char)

    return len(quest)


with open('puzzle6.txt', 'r') as file_:
    file_ = file_.readlines()
    file_ = [line.strip() for line in file_]

g = ''
for line in file_:
    if line != '':
        g = g + line

    else:
        total = total + distinct(g)
        g = ''

total += distinct(g)

print(total)


# Day 6 Part 2

def distinct(rep):
    quest = []

    for char in rep[0]:
        included = True 
        for line in rep:
            if char not in line:
                included = False
        
        if included and char not in quest:
            quest.append(char)

    return len(quest)

total = 0 
list_ = []

with open('puzzle6.txt', 'r') as file_:
    file_ = file_.readlines()
    file_ = [line.strip() for line in file_]
   
    for line in file_:
        if line != '':    
            list_.append(line)
        
        else:
            total = total + distinct(list_)
            list_ = []
    total = total + distinct(list_)

    print(total)