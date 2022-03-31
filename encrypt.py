# Binary and Hexadecimal
def binary(num, length=8):
  bina = bin(num).lstrip("0b")
  bina = "0" *(length-len(bina)) + bina
  return bina
def hexadecimal(num, length=2):
  hexa = hex(num).lstrip("0x").upper()
  hexa = "0" *(length-len(hexa)) + hexa
  return hexa
  
# Text and Key
text = input("Enter the text that you want to decrypt : \n")
key = "QAZ1308"
keylength = len(key)
  
# Cipher List
cipherAscii = ""
cipherBin = ""
cipherDen = ""
cipherHex = ""
  
# Calculation
for i in range (0, len(text)):
    j = i % keylength
      
    xor = ord(text[i]) ^ ord(keyopen[j])
    cipherAscii = cipherAscii + chr(xor)
    cipherBin = cipherBin + binary(xor) + " "
    cipherDen = cipherDen + str(xor) + " "
    cipherHex = cipherHex + hexadecimal(xor) + " "
     
# Output
print ("\n Cipher Ascii : \n" + cipherAscii)
print ("\n Cipher Binary : \n" + cipherBin)
print ("\n Cipher Denary : \n" + cipherDen)
print ("\n Cipher Hexadecimal : \n" + cipherHex)
 
