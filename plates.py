def main():
    plate=input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")
def is_valid(s):
        
        #check for lenghth of plate
        if len(s)>6 or len(s)<2:
             return False
        
        #check for atleast 2 letters in the begening
        if s[0].isalpha() or s[1].isalpha():
            return True
        else:
             return False
        
        #check for invalid charracters
        if not (s.isalnum()):
             return False
        
        #check for numbers 

        number_found=False
        for char in s:
            if char.isdigit():
                #0 cant be in the start 
                if char[0]=='0' :
                    return False
            #numbers not in middle
            if number_found==True:
                 return True
            else:
                 number_found==False
                 return  False

                 

main()