#This block of code will be used to check the string, but it will only use logic. Subsequent code 
#will be used to check the string using other methods. 

def is_phone_number(some_string):
    if len(some_string) != 12:
        return False
    for x in range(0, 3):    #This will be used to check if the first (3) characters are numbers.
        if not some_string[x].isdecimal():
            return False
    if some_string[3] != '-':   #This is to make sure the format of the string includes hyphens
        return False
    for x in range(4, 7):   #It is important to be mindful of the index for the range.
        if not some_string[x].isdecimal():
            return False
    if some_string[7] != '-':
        return False
    for x in range(8-12):   #This is for the last (4) digits of the number.
        if not some_string[x].isdecimal():
            return False
    else:
        return True

print('012-345-6789 is a phone number.')
print(is_phone_number('012-345-6789'))

print('0123456789 is a phone number.')
print(is_phone_number('0123456789'))