# Ask user inputs 

name =input('Enter your name: ')
ages = int(input('Enter your  ages: '))



with open('answer1.csv','w') as file:
    file.write(f'Hello {name}! You are {ages} Years old')
    
with open('answer1.csv','r') as file:
    for line in file:
        print(line.strip())