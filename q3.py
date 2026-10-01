# marks 
marks =int(input("How many grades do you have? "))

if marks >=80:
    grades ="A"
elif marks >=70:
    grades ="B"
elif marks>=60:
    grades ="C"
    
else:
    grades ="F"
    
with open('answer3.csv','w') as file:
    file.write(f'THE marks {marks} Grade you as {grades}! ')