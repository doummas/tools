import sys
import hashlib



if sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv)<3:
    print("" \
    "[+] Usage python3 hash.cracker.py  <wordlist>  <The hashs file> <algorithm>\n" \
    "[+] if you want to enable verbose mode just add -v ( Not recomended it cause lower speed )\n"\
    "[+] the algorithm must be lower chase letter\n" \
    "[+] supported algorithm:\n" \
    "[+] md5\n" \
    "[+] sha1\n" \
    "[+] sha512\n" \
    "[+] sha256\n" \
    "[+] sha224\n")
    exit()

algorithm=sys.argv[3]

algorithm=sys.argv[3]
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


def hash_file_reader():
    hash_file=sys.argv[2]
    hash_list=[]
    with open(hash_file, "r") as f:
        for line in f:
            line=line.strip()
            hash_list.append(line)
    return hash_list

def hashing_wordlist(hash):
    wordlist = sys.argv[1]
    line_count = 0
    i=0
    with open(wordlist , "r",encoding='latin-1') as file:
        try:
            while i < len(hash):
                for line in file:
                    line_count += 1
                    words=line.strip()
                    hashed_pass=hasherr(words,algorithm)
                    if hashed_pass in hash:
                            i+=1
                            with open("output.txt",'a') as f: 
                                f.writelines(f"{words}\n")
                    if "-v" in sys.argv:
                        if hashed_pass not in hash:
                            print(f'Searching({line_count })')
                    if i == len(hash):
                        sys.exit()
        except UnicodeDecodeError:
            print("Invalid charactere")
        except KeyboardInterrupt:
                exit()        
list=hash_file_reader()
print(list)
print(f"Password to crack {len(list)}")
hashing_wordlist(list)
