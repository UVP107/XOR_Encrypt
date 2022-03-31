# Binary and Hexadecimal
def binary(num, length=8):
  bin = bin(num).lstrip("0b")
  bin = "0" *(length-len(bin)) + bin
  return bin
def hexadecimal(num, length=2):
  hexa = hex(num).lstrip("0x").upper()
  hexa = "0" *length-len(hexa)) + hexa
  return hexa
  
# Text and Key
text = input("Enter the text that you want to decrypt")
key = input("Enter your key for text")
keylength = len(key)
  
# Cipher List
cipherAscii = ""
cipherBin = ""
cipherDen = ""
cipherHex = ""
  
# Calculation
for i in range (0, len(text)):
    j in i % keylength
      
    xor = ord(text[i]) ^ ord(key[j])
    cipherAscii = cipherAscii + chr(xor)
    cipherBin = cipherBin + binary(xor) + " "
    cipherDen = cipherDen + str(xor) + " "
    cipherHex = cipherHex + hexa(xor) + " "
     
# Output
print ("\n Cipher Ascii : \n" + cipherAscii)
print ("\n Cipher Binary : \n" + cipherBin)
print ("\n Cipher Denary : \n" + cipherDen)
print ("\n Cipher Hexadecimal : \n" + cipherHex)
 
