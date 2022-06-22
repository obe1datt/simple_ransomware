import os
from cryptography.fernet import Fernet 
import hashlib


      
     

files_to_decrypt = []
key_file = []
# home dirctory for system 
home = os.path.expanduser('~/Desktop/ran')
# bring all files in home dirctory 
for root,dirs,files in os.walk(home):
    for filex in files:
       if filex == "keyfile" :
         key_file.append(root+'/'+filex)
       if filex == "encryption_file.py" or filex=="keyfile" or filex=="decryption_file.py" :
          continue 
       files_to_decrypt.append(root+'/'+filex)          
print(files_to_decrypt)          
print(key_file)

passwd = str(input("Enter password to dycrypt your file:"))

if passwd == '0be1dat':  
  for keyfi in key_file:
      with open(keyfi,'rb') as fff: 
         keyr = fff.read()

  for FILE in files_to_decrypt :
    with open(FILE,'rb') as f :
        content = f.read()
    con_decrypt=Fernet(keyr).decrypt(content)
    
    with open(FILE,'wb') as ff :
        ff.write(con_decrypt)
        
        
           
    


