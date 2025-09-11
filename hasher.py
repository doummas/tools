import hashlib

def hasherr(password,type):
    try:
        if type == "md5":
            return hashlib.md5(password.encode()).hexdigest()
        elif type == "sha1":
            return hashlib.sha1(password.encode()).hexdigest()
        elif type == "sha512":
            return hashlib.sha512(password.encode()).hexdigest()
        elif type == "sha256":
            return hashlib.sha256(password.encode()).hexdigest()
        elif type == "sha224":
            return hashlib.sha224(password.encode()).hexdigest()
    except KeyboardInterrupt:
        exit()


    
    

