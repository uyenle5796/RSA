# -*- coding: utf-8 -*-#

import os
import re
from rsa_functions import *

def menu():

    os.system('python3 rsa_functions.py')

    regexStr = re.compile("^[a-zA-Z0-9_,.].*$")

    print("==========================================================================")
    print("Computer Security Coursework \nPart 1: RSA Algorithm \nby Uyen Le (tle004)")
    print("==========================================================================\n")

    print("Hello Alice! \n\nSuppose you want to send a private message to Bob...\n")
    print("What would you like to say? \n(Note: you can only use alphanumeric characters in your message)\n")
    inputMessage = str(input("Your plaintext message: "))

    #Input message cannot be empty
    if not inputMessage:
        print("ERROR: Please enter a message.")
        return

    # Validate input using regular expression
    # only alphanumeric characters are allowed
    elif not(regexStr.match(inputMessage)):
        print("\nSorry, only alphanumeric characters allowed. Please try again.")
        return

    #If all above is passed, start the crytosystem
    else:
        print("\nStarting RSA encryption...\n")
        key_p = generateRandKey()
        key_q = generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        print("\nn is:", str(key_p), "*", str(key_q), "=", calculateN(key_q, key_p))

        phiN = totient(key_q, key_p)
        print("\nphi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # TO DO
        for e in range(1, phiN):
            result = generateE(e, phiN)
        print("\ne (coprime to phi(n)) is: ", result)

        # print("\n d is: ")

        # print ("\n\n Your public key (e,n) is: (", ....)
        # print ("\n\n Your private key (d,n) is: (", ....)

        # print("\n-------------------------------------------------")
        # print("Your Public key can be published anywhere! However your Private Key is be confidential!")
        # print("So that Charlie cannot intercept your private message!\n")
        # print("Your Communication diagram now looks like this:")
menu()
