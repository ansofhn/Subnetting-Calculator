# Import
from time import sleep as wait
try: 
	from playsound import playsound
except: pass
# Function for called file mp3 with playsound module
def voice (mp3):
	try: playsound(mp3)
	except: pass
# Function for IP Counter
def CountIP(classes,enter):
    if classes==1:
        prev = 32-((int(enter[-1]))+16)
    elif classes==2:
        prev = 32-((int(enter[-1]))+8)
    elif classes==3:
        prev = 32-(int(enter[-1]))
    mask = 2**prev
    host = (2**(32-(int(enter[-1]))))-2
    if mask > int(enter[classes]):
        mask-=1
        if classes==1:
            enter[1],enter[2],enter[3]='0','0','0'
            net = ".".join(enter)
            enter[1],enter[2],enter[3]=str(mask),'255','255'
            bc = ".".join(enter)
            enter[0],enter[1],enter[2],enter[3]='255',str(256-(2**prev)),'0','0'
            netmask = ".".join(enter)
        elif classes==2:
            enter[2],enter[3]='0','0'
            net = ".".join(enter)
            enter[2],enter[3]=str(mask),'255'
            bc = ".".join(enter)
            enter[0],enter[1],enter[2],enter[3]='255','255',str(256-(2**prev)),'0'
            netmask = ".".join(enter)
        elif classes==3:
            enter[3]='0'
            net = ".".join(enter)
            enter[3]=str(mask)
            bc = ".".join(enter)
            enter[0],enter[1],enter[2],enter[3]='255','255','255',str(256-(2**prev))
            netmask = ".".join(enter)
    else:
        while mask < int(enter[classes]):
            mask+=mask
        if mask == int(enter[classes]):
            if classes==1:
                enter[1],enter[2],enter[3]=str(mask),'0','0'
                net = ".".join(enter)
                enter[1],enter[2],enter[3]=str((mask*2)-1),'255','225'
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255',str(256-(2**prev)),'0','0'
                netmask = ".".join(enter)
            elif classes==2:
                enter[2],enter[3]=str(mask),'0'
                net = ".".join(enter)
                enter[2],enter[3]=str((mask*2)-1),'255'
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255','255',str(256-(2**prev)),'0'
                netmask = ".".join(enter)
            elif classes==3:
                enter[3]=str(mask)
                net = ".".join(enter)
                enter[3]=str((mask*2)-1)
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255','255','255',str(256-(2**prev))
                netmask = ".".join(enter)
        elif mask > int(enter[classes]):
            if classes==1:
                enter[1],enter[2],enter[3]=str(mask-2**prev),'0','0'
                net = ".".join(enter)
                enter[1],enter[2],enter[3]=str(mask-1),'255','255'
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255',str(256-(2**prev)),'0','0'
                netmask = ".".join(enter)
            elif classes==2:
                enter[2],enter[3]=str(mask-2**prev),'0'
                net = ".".join(enter)
                enter[2],enter[3]=str(mask-1),'255'
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255','255',str(256-(2**prev)),'0'
                netmask = ".".join(enter)
            elif classes==3:
                enter[3]=str(mask-2**prev)
                net = ".".join(enter)
                enter[3]=str(mask-1)
                bc = ".".join(enter)
                enter[0],enter[1],enter[2],enter[3]='255','255','255',str(256-(2**prev))
                netmask = ".".join(enter)
    ranf=net.split(".")
    ranf[-2]=str(int(ranf[-2])+1)
    first=".".join(ranf)
    ranl=bc.split(".")
    ranl[-2]=str(int(ranl[-2])-1)
    last=".".join(ranl)
    print('\n'+'='*50);print('Network\t\t:',net[:-2],'\nBroadcast\t:',bc[:-2],'\nNetmask\t\t:',netmask[:-2],'\nRange IP\t:',first[:-2],'~',last[:-2],'\nUsable IP\t:',host,'Host');print('='*50)

opening=("\n"+"<"+"="*28+">"+"\n| SUBNETTING CALCULATOR IPV4 |\n"+"<"+"="*28+">")
print(opening),voice('open.mp3')

# Central Programm
while True:
    voice('enter.mp3')
    ip = input("\nEnter IP Address : ")
    ip = "/".join(ip.split("."))
    ip = ip.split("/")
    prev = int(ip[-1])
        
    if prev > 7 and prev < 16:
        print('\n'+'<'+'='*17+'>'+'\n| CLASS A NETWORK |\n'+'<'+'='*17+'>'),voice('a.mp3')
        CountIP(1,ip)
        wait(2)
    elif prev > 15 and prev < 24:
        print('\n'+'<'+'='*17+'>'+'\n| CLASS B NETWORK |\n'+'<'+'='*17+'>'),voice('b.mp3')
        CountIP(2,ip)
        wait(2)
    elif prev > 23 and prev < 33:
        print('\n'+'<'+'='*17+'>'+'\n| CLASS C NETWORK |\n'+'<'+'='*17+'>'),voice('c.mp3')
        CountIP(3,ip)
        wait(2)
    else :
        print('\nINPUT ERROR !!')
        voice('error.mp3')
        print('\n-----< Retype IP Address >-----\n')
        continue
    voice('repeat.mp3')
    repeat = input("\n>> Do you want to repeat? [y/n]    : ")
    if repeat == 'n' or repeat == 'N' or repeat == 'no' or repeat=='NO':
        print('\n-----< Thanks for Use this programm >-----\n'),voice('end.mp3') 
        break
    else:
        print('\n-----< Programm Reapeted >-----\n'),voice('restart.mp3')
        print(opening),wait(1)