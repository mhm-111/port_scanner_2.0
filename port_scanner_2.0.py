import socket



logo="""  
░█▀▀█ ░█▀▀▀█ ░█▀▀█ ▀▀█▀▀ 　 ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ░█▄─░█ ░█▄─░█ ░█▀▀▀ ░█▀▀█ 
░█▄▄█ ░█──░█ ░█▄▄▀ ─░█── 　 ─▀▀▀▄▄ ░█─── ░█▄▄█ ░█░█░█ ░█░█░█ ░█▀▀▀ ░█▄▄▀ 
░█─── ░█▄▄▄█ ░█─░█ ─░█── 　 ░█▄▄▄█ ░█▄▄█ ░█─░█ ░█──▀█ ░█──▀█ ░█▄▄▄ ░█─░█  2.0   - 𝔹𝕐 𝕄ℍ𝕄
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------    
    """

print(logo)


print("\n-------------------------  To scan multiple targets separate targets by comma ',' ---------------------------------")
first_ip=input("Enter an Ip/Domain to scan : ")
split_ip=first_ip.split(",")

option="""\n Port scan option
 -------------------------
 1. Single Port Scan
 2. Multiple Ports Scan"""

print(option)
port_optn=int(input("\n Select a port scan option(1/2) : "))

open_port=0
close_port=0

def get_banner(s):
    return s.recv(1024)


def scan_ip(ip,prt):
    global open_port
    global close_port

    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip,prt))
        open_port += 1
        try:
            banner = get_banner(sock)
            print(f" [+] Open Port : {prt}  :::  "+ str(banner.decode().strip("\n")))

        except:
            print(f" [+] Open Port : {prt}")
    except:

        close_port += 1



if port_optn==1:
    port_single =int(input(" Enter a single port : "))
    for fin_ip in split_ip:
        fin_ip=fin_ip.strip()
        print(f"\n--------------- {fin_ip} scanning programme has been launched! :) ---------------")

        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\ Please wait /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\\n")
        scan_ip(fin_ip,port_single)
        print(f"\n ' {fin_ip} ' scanning has been completed :) ")
        print(f" Open Port : {open_port} ")
        print(f" Close Port : {close_port}")


elif port_optn==2:
    port_strt=int(input(" Enter the first port : "))
    port_end=int(input(" Enter the last port : "))
    for fin_ip in split_ip:
        fin_ip=fin_ip.strip()
        print(f"\n--------------- {fin_ip} scanning programme has been launched! :) --------------- ")
        print("/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\ Please wait /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\\n")
        for prt in range(port_strt,port_end+1):
            scan_ip(fin_ip,prt)
        print(f"\n ' {fin_ip} ' scanning has been completed :) ")
        print(f" Open Port : {open_port} ")
        print(f" Close Port : {close_port}")