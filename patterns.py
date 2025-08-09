n = int(input("no of rows in pyramid? "))
for i in range(1,n+1):
    print(("* "*i).rstrip())

print("_______________",end="\n\n")


for i in range(n):
    for j in range(n):
        print("*",end="  ")
    print()

print("_____________________")

for i in range(n-1):
    print(("* "*(n-i-1)).rstrip())

print("_____________________")
for i in range(1,n+1):
    space=" "*(n-i)
    star="* "*i
    print((space+star).rstrip())

print("_______________",end="\n\n")
for i in range (n):
    space=" "*(n-i)
    no=(str(i)+" ")*i
    i+=i
    print((space+no).rstrip())

    
print("_______________",end="\n\n")
