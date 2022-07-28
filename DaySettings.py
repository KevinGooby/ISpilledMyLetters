from calendar import week
from datetime import datetime

import string

# These three dictionaries show unique settings to ENCRYPT words
# The first batch of settings to scramble words
firstSettings = {
        'A': 7, 'B': 10,
        'C': -1, 'D': 10,
        'E': 14, 'F': -3,
        'G': 10, 'H': 1,
        'I': 7, 'J': -3,
        'K': -10, 'L': 10,
        'M': -3, 'N': -10,
        'O': 10, 'P': -3,
        'Q': 7, 'R': -3,
        'S': 7, 'T': -14,
        'U': -3, 'V': -17,
        'W': -3, 'X': -3,
        'Y': -14, 'Z': -3
    }

# The second batch of settings to scramble words
secondSettings = {
        'A': 5, 'B': 16,
        'C': 5, 'D': 21,
        'E': 5, 'F': 16,
        'G': 16, 'H': 16,
        'I': 5, 'J': -9,
        'K': 5, 'L': 0,
        'M': -9, 'N': -9,
        'O': 5, 'P': 5,
        'Q': 2, 'R': -16,
        'S': -16, 'T': -9,
        'U': 5, 'V': -9,
        'W': -16, 'X': -9,
        'Y': -16, 'Z': -9
    }

# The third batch of settings to scramble words
thirdSettings = {
    'A': 3, 'B': 5,
    'C': 5, 'D': 1,
    'E': 1, 'F': 3,
    'G': 5, 'H': 5,
    'I': 1, 'J': 1,
    'K': 3, 'L': 5,
    'M': 5, 'N': 1,
    'O': 1, 'P': 3,
    'Q': 5, 'R': 5,
    'S': 1, 'T': 1,
    'U': 3, 'V': 3,
    'W': 3, 'X': -23,
    'Y': -23, 'Z': -23
}

#
SUNDAY_CODE = "ZS"
MONDAY_CODE = "AM"
TUESDAY_CODE = "ET"
WEDNESDAY_CODE = "IW"
THURSDAY_CODE = "MT"
FRIDAY_CODE = "QF"
SATURDAY_CODE = "XS"

# Dictionary for each weekday's CODE (0 = Monday, 1 = Tuesday, etc..)
dayCodes = {
    0: MONDAY_CODE,
    1: TUESDAY_CODE,
    2: WEDNESDAY_CODE,
    3: THURSDAY_CODE,
    4: FRIDAY_CODE,
    5: SATURDAY_CODE,
    6: SUNDAY_CODE
}

# Encrypts the given string with the given setting, then returns the string
def encrypt(string, setting) -> string:

        message = string.upper() # Make all characters uppercase to ensure it it consistent with settings
        result = ""

        for char in message:
            if char.isspace() is True:
                result += " "
            elif char.isalpha() is True:
                result += chr(ord(char) + setting[char])

                # ord() is used to find the unicode value of a character
                # chr() is used to get the unicode character that corresponds with a numerical value

            else:
                result += char
        
        return result
    
# Reverses a given string, then returns it
def reverse(string) -> string:
    result = ""
    for i in range(len(string)):
        result += string[len(string) - 1 - i]
        
    return result

# Encrypts given string based on current weekday, reverses it, then adds its respective code
def completeEncryption(string, weekday) -> string:
    result = "" 
    if weekday == 0:
        result += encrypt(string, secondSettings)
    elif weekday == 1:
        result += encrypt(string, thirdSettings)
    elif weekday == 2:
        answer = encrypt(string, firstSettings)
        result += encrypt(answer, secondSettings)
    elif weekday == 3:
        answer = encrypt(string, secondSettings)
        result += encrypt(answer, thirdSettings)
    elif weekday == 4:
        answer = encrypt(string, thirdSettings)
        result += encrypt(answer, firstSettings)
    elif weekday == 5:
        answer = encrypt(string, firstSettings)
        secondAnswer = encrypt(answer, secondSettings)
        result += encrypt(secondAnswer, thirdSettings)
    elif weekday == 6:
        result += encrypt(string, firstSettings)
    
    reversedResult = reverse(result)
    return reversedResult + dayCodes[weekday]

# The dictionary settings used to decrypt words

# Settings to decrypt firstSettings
firstDecrypt = {

}

# Settings to decrypt secondSettings
secondDecrypt = {

}

# Setteings to decrypt thirdSettings
thirdDecrypt = {

}

# Generates the settings for the given ENCRYPTION settings dictionary
# settings must be either firstSettings, secondSettings or thirdSettings
def generateDecryptions(settings) -> None:
    keylist = settings.keys()
    for key in keylist:
        newletter = chr(ord(key) + settings[key])
        number = settings[key]

        if (settings == firstSettings):
            firstDecrypt.update({newletter: number})
        elif (settings == secondSettings):
            secondDecrypt.update({newletter: number})
        elif (settings == thirdSettings):
            thirdDecrypt.update({newletter: number})


# Decrypts the given string with the given settings, then returns the string
def decrypt(string, setting) -> string:

        message = string.upper() # Make all characters uppercase to ensure it it consistent with settings
        result = ""

        for char in message:
            if char.isspace() is True:
                result += " "
            elif char.isalpha() is True:
                result += chr(ord(char) - setting[char])
            else:
                result += char
        
        return result


# TODO: Use a higher order function in order to abstract encrypt + decrypt

# Decrypts a given string based on the day.
def completeDecryption(message) -> string:
    result = ""
    stringCode = message[len(message) - 2: len(message)]
    string = message[0: len(message) - 2]

    if stringCode == SUNDAY_CODE:
        result += decrypt(string, firstDecrypt)
    elif stringCode == MONDAY_CODE:
        result += decrypt(string, secondDecrypt)
    elif stringCode == TUESDAY_CODE:
        result += decrypt(string, thirdDecrypt)
    elif stringCode == WEDNESDAY_CODE:
        answer = decrypt(string, secondDecrypt)
        result += decrypt(answer, firstDecrypt)
    elif stringCode == THURSDAY_CODE:
        answer = decrypt(string, thirdDecrypt)
        result += decrypt(answer, secondDecrypt)
    elif stringCode == FRIDAY_CODE:
        answer = decrypt(string, firstDecrypt)
        result += decrypt(answer, thirdDecrypt)
    elif stringCode == SATURDAY_CODE:
        answer = decrypt(string, thirdDecrypt)
        secondAnswer = decrypt(answer, secondDecrypt)
        result += decrypt(secondAnswer, firstDecrypt)
    
    reversedResult = reverse(result)
    return reversedResult
    

    


        

