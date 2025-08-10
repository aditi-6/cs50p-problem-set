a=input("enter the word: ")
output=""
a=a.upper()
#vowel=False
for i in a:
    if i=="A" or i=="E" or i== "I" or i=="O" or i=="U":
        continue
    else:
        output+=i
           
print(output)

       
