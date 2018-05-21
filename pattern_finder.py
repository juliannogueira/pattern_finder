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




#This next block of code adds more functionality to pattern_finder. It actually looks through
#entire strings of data, and it reports if there are any phone numbers found in it - based on 
#what qualifies as a phone number per the is_phone_number function. 

test_string = 'Please call me on my cellphone: 619-782-6610, or you can reach me from 0900-1700 on my work line: 619-454-0189.'    #This string will be tested.

def pattern_finder(a_string):
    for y in range(len(a_string)):
        data_chunk = a_string[y: y + 12]    #This slices a string at each index, (12) char. long. 

        if is_phone_number(data_chunk) == True:    #Here we run our test function on the string.
            print('Phone number found: ' + data_chunk)

pattern_finder(test_string)