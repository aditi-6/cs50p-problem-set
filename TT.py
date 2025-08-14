def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    # Check for invalid characters
    if not s.isalnum():
        return False
    
    # Check number rules
    number_found = False
    for char in s:
        if char.isdigit():
            # First number can't be 0
            if char == '0' and not number_found:
                return False
            number_found = True
        elif number_found:
            # Letter after number is invalid
            return False
    
    return True

main()