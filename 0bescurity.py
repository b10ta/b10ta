encrypted = '¦ÚÈêÚÞØÛÝÝ  '


decrypted = 'Encrypting this file with your key should result in out.txt, make sure your key is correct!'

key=''
for i in range(len(encrypted)-1):
    keyChr =  chr(ord(encrypted[i]) - ord(decrypted[i]) % 255)
    key = key+keyChr

print(key)
