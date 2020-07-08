import  sys
def gcd(a, b):
    if a > b:
        for i in range(b, 0, -1):
            if a % i == 0 and b % i == 0:
                return i
    else:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return i


# Function to find x
def findx(k):
    for i in range(1, 26):
        if (k * i) % 26 == 1:
            return i


# Implementation of Affine Cipher
c = 1
while c == 1:
    it = input("Enter the text to cipher: ")
    if it != it.lower():
        print("Please input lower case values")
        sys.exit(1)
    for i in it:
        if i != " ":
            if (ord(i) < ord('a') or ord(i) > ord('z')):
                print("XXX Enter the correct text XXX")
                c = 1
                break
            else:
                c = 0

# Encryption
ct = ""
c1 = 0
c2 = 0
while c1 == 0:
    k1 = int(input("Enter the value of 1st Key: "))
    if isinstance(k1, int) != True or k1 > 26 or gcd(k1, 26) != 1:
        print("XXX Enter the correct value of key 1 XXX")
        c1 = 0
    else:
        c1 = 1

while c2 == 0:
    k2 = int(input("Enter the value of 2nd Key: "))
    if isinstance(k2, int) != True:
        print("XXX Enter the correct value of key 2 XXX")
        c2 = 0
    else:
        c2 = 1
if k2 > 26:
    k2 = k2 % 26

for i in it:
    if i == " ":
        ct += " "
    else:
        a = chr((((ord(i) - 96) * k1) % 26) + 96 - 32)
        t = chr((((ord(a) - 96) + k2) % 26) + 96 - 32)
        ct += t
print("Ciphered Text: ", ct)

# Decryption
pt = ""
for i in ct:
    if i == " ":
        pt += " "
    else:
        x = findx(k1)
        a = chr(((ord(i) - 64 - k2) % 26) + 64 + 32)
        t = chr((((ord(a) - 64) * x) % 26) + 64 + 32)
        pt += t
print("Plain Text: ", pt)

# Bruteforce
for k1 in range(1, 26):
    if gcd(k1, 26) == 1:
        x = findx(k1)
        for k2 in range(1, 26):
            mt = ""
            for i in ct:
                if i == " ":
                    mt += " "
                else:
                    a = chr(((ord(i) - 64 - k2) % 26) + 64 + 32)
                    t = chr((((ord(a) - 64) * x) % 26) + 64 + 32)
                    mt += t
            if mt == pt:
                print("The Keys are: ", k1, k2)
                break