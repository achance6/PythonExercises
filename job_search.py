def add_companies(*companies: str):
    with open('companies.txt', 'a', encoding = 'utf-8') as f:
        for company in companies:
            f.write(f'{company}\n')

def print_companies():
    with open('companies.txt', 'r', encoding = 'utf-8') as f:
        line = f.readline()
        while line:
            print(line, end = '')
            line = f.readline()


print('Q to quit, A to add companies, R to print companies', end = ' ')

inp = input().upper()
while inp != 'Q':

    if inp == 'A':
        add_companies(input())

    if inp == 'R':
        print_companies()

    print('Q to quit, A to add companies, R to print companies', end = ' ')
    inp = input().upper()

