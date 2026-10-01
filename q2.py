# numbers calculations

num1 = int(input("First number: "))
operator =input("choose the operator in(+,-,*,/): ")
num2 = int(input("Second number: "))


if operator == '+':
    result = num1 +num2
elif operator == '-':
    result = num1-num2
elif operator =="*":
    result = num1*num2
    
else:
    num1/num2
    

with open('answer2.csv','w') as file:
    file.write(f'The real Answer for {num1}  by {operator}  and {num2} is {result}')
    
with open('answer2.csv','r') as file:
    for line in file:
        print(line.strip())