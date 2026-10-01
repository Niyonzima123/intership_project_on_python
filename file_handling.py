with open('students.csv','w') as file:
    file.write("1" ':' 'isaac\n')
    file.write('2' ':' 'Lucie\n')
    file.write('3' ':' "Cynthia\n")
    
with open('students.csv', 'a') as file:
    file.write("4" ':' "Phoibe\n")
    file.write("5" ":" "Francine")
    
with open('students.csv', "r") as file:
    for line in file:
        print(line.strip())