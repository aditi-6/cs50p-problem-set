#CAMEL CASE TO SNAKE CASE
'''c=input("enter the word in camel case: ")
result=""
for i in c:
    if i.isupper():
      result+="_"
      result+=i.lower()
    else:
       result+=i
    
print(result)'''

#SNAKE CASE TO CAMEL CASE
a=input("enter in snake case: ")
result=""
capitalize_next= False #flag
for i in a:
  '''  if i=="_":
      capitalize_next=True
      result+=i.upper()

    else:
       capitalize_next= False
       result+=i'''
  if i == "_":
        capitalize_next = True
        
  else:
        if capitalize_next:
            result += i.upper()
            capitalize_next = False
        else:
            result += i
print (result)