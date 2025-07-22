import hashlib


    

def hasherr(password,type):
    if type == "md5":
         return hashlib.md5(password.encode()).hexdigest()
    if type == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    if type == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    
    
    

