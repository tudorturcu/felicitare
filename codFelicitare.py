#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import numpy as np

turcu = 1
tudor = 0

mesaj = [turcu, tudor, tudor, tudor, tudor,
         tudor, turcu, turcu, tudor, tudor,
         tudor, tudor, turcu, tudor, turcu,
         turcu, turcu, tudor, turcu, turcu,
         tudor, tudor, turcu, turcu, tudor,
         tudor, tudor, turcu, turcu, turcu,
         tudor, turcu, tudor, turcu, tudor,
         turcu, turcu, tudor, tudor, turcu,
         tudor, turcu, turcu, turcu, turcu,
         turcu, tudor, turcu, turcu, turcu,
         tudor, tudor, tudor, turcu, tudor,
         turcu, turcu, turcu, tudor, turcu,
         tudor, turcu, tudor, turcu, tudor,
         tudor, turcu, tudor, tudor, tudor,
         tudor, tudor, turcu, turcu, tudor,
         turcu, tudor, tudor, tudor, turcu,
         tudor, turcu, tudor, turcu, tudor,
         turcu, turcu, turcu, turcu, turcu,
         tudor, tudor, turcu, tudor, turcu,
         turcu, tudor, turcu, turcu, tudor,
         turcu, tudor, tudor, tudor, turcu,
         tudor, turcu, turcu, turcu, tudor,
         tudor, tudor, turcu, tudor, tudor,
         tudor, turcu, turcu, tudor, tudor,
         turcu, tudor, turcu, turcu, tudor,
         tudor, turcu, turcu, turcu, turcu,
         turcu, turcu, tudor, turcu, turcu,
         turcu, tudor, tudor, turcu, turcu,
         tudor, turcu, turcu, turcu, tudor,
         tudor, tudor, turcu, turcu, turcu,
         turcu, tudor, turcu, turcu, tudor,
         tudor, tudor, tudor, turcu, turcu]

nrBitiCaracter = 5
nrCaractere = len(mesaj) / nrBitiCaracter

mesaj = np.reshape(mesaj, (nrCaractere, nrBitiCaracter))
#print mesaj

alfabetEngleza = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# print alfabetEngleza

cipherText = ""
frecventa = [0] * 32
coduriCaractere = []

for caracter in mesaj:
    codCaracter = 0
    for bit in caracter:
        codCaracter = (codCaracter << 1) | bit
    # print codCaracter
    coduriCaractere.append(codCaracter)

print coduriCaractere

for codCaracter in coduriCaractere:
    #litera = (codCaracter - 1) % 26
    if codCaracter > len(alfabetEngleza):
        cipherText += chr(ord('0') + codCaracter - len(alfabetEngleza))
        #cipherText += '-'
    else:
        cipherText += alfabetEngleza[codCaracter - 1]
    frecventa[codCaracter] += 1

print '_' + alfabetEngleza + "12345"

def to_string(lista):
    return ''.join(str(element) for element in lista)

print to_string(frecventa)

print cipherText

#caesar - simple shift - 26 possibilities


# for shiftAmount in range (0, len(alfabetEngleza)):
#     #print shiftAmount
#     mesaj = ""
#     for litera in cipherText:
#         mesaj += alfabetEngleza[(ord(litera) + shiftAmount - ord('A') ) % len(alfabetEngleza)]
#     print mesaj

# substitution - each letter replaced with another
# TRY grupuri de litere


#                   1010201013001021221203012211110
#                     _ABCDEFGHIJKLMNOPQRSTUVWXYZ12345
substitutionString = "_JBCDVFGHIAKLMNOPQRSTUEWXYZ12345"
base32_substitionString = "_123456789abcdefghijklmnopqrstuv"



def toTextString (array):
    return ''.join(chr(ord('A') + element - 1) for element in array)


def isArrayOk (array):
    ok = 1
    for element in array:
        if element > 26 or element < 1:
            ok = 0
    if ok == 1:
        print toTextString(array)
    else:
        print "not ok"

mesaj = []


isArrayOk(mesaj)


possibleKeys = ["PENIS", "QWERTYUIOPASDFGHJKLZXCVBNM", "ABCDEFGHIJKLMNOPQQRSTUVWXYZ", "RANDOM", "PULA", "PIZDA", "SUGIPULA", "FUCK",  "TUDOR", "TURCU", "TUDORTURCU", "TURCUTUDOR", "CRISTI", "CRISTIAN",
"TREE", "COPAC", "LAMULTIANI", "PADURE", "HAPPYBIRTHDAY"]

len_alf = len(alfabetEngleza)

for key in possibleKeys:
    mesaj = ""
    len_key = len(key)
    for i in range(0, len(coduriCaractere)):
        cod = coduriCaractere[i]

        # ADUNARE
        mesaj += chr (ord('A') + ((cod - ord(key[i % len_key]) + ord('A') - 1 - 1) % 32 ))

    print mesaj


for key in possibleKeys:
    mesaj = ""
    len_key = len(key)
    for i in range(0, len(coduriCaractere)):
        cod = coduriCaractere[i]

        # SCADERE
        mesaj += chr (ord('A') + ((cod + ord(key[i % len_key]) - ord('A') + 1 - 1) % 32 ))

    print mesaj


for key in possibleKeys:
    mesaj = ""
    len_key = len(key)
    for i in range(0, len(coduriCaractere)):
        cod = coduriCaractere[i]

        # XOR
        mesaj += chr (ord('A') + (cod ^ (ord(key[i % len_key]) - ord('A') + 1)) - 1)
    print mesaj

    # for shiftAmount in range (0, len(alfabetEngleza)):
    #     #print shiftAmount
    #     mesajCaesar = ""
    #     for litera in mesaj:
    #         mesajCaesar += chr(ord('A') + ((ord(litera) + shiftAmount - ord('A') ) % 32))
    #     print mesajCaesar



