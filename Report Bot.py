
                                                     
# Made By Kurdo#7053 $        
                                                     



import requests
import colorama
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')

ctypes.windll.kernel32.SetConsoleTitleW(f"[MASS REPORT] By Kurdo ")

print(f"""
{b+Fore.RED}   
  in cp with kurdo and deployd
                                        ;                                    ;           
                                        ED.                                  ED.         
                      .,       .,       E#Wi                 ,;              E#Wi        
                     ,Wt      ,Wt       E###G.             f#i               E###G.      
             ..     i#D.     i#D.       E#fD#W;          .E#t             .. E#fD#W;     
            ;W,    f#f      f#f         E#t t##L        i#W,             ;W, E#t t##L    
           j##,  .D#i     .D#i          E#t  .E#K,     L#D.             j##, E#t  .E#K,  
          G###, :KW,     :KW,           E#t    j##f  :K#Wfff;          G###, E#t    j##f 
        :E####, t#f      t#f            E#t    :E#K: i##WLLLLt       :E####, E#t    :E#K:
       ;W#DG##,  ;#G      ;#G           E#t   t##L    .E#L          ;W#DG##, E#t   t##L  
      j###DW##,   :KE.     :KE.         E#t .D#W;       f#E:       j###DW##, E#t .D#W;   
     G##i,,G##,    .DW:     .DW:        E#tiW#G.         ,WW;     G##i,,G##, E#tiW#G.    
   :K#K:   L##,      L#,      L#,       E#K##i            .D#;  :K#K:   L##, E#K##i      
  ;##D.    L##,       jt       jt       E##D.               tt ;##D.    L##, E##D.       
  ,,,      .,,                          E#t                    ,,,      .,,  E#t         
                                        L:                                   L:                
 loading....

{b+Fore.RED} | {Fore.RESET}selections....?
{b+Fore.RED} | {Fore.RESET}illegal material {b+Fore.RED}:>{Fore.RESET} 1
{b+Fore.RED} | {Fore.RESET}harrassment {b+Fore.RED}:>{Fore.RESET} 2
{b+Fore.RED} | {Fore.RESET}spam or harmful links {b+Fore.RED}:>{Fore.RESET} 3
{b+Fore.RED} | {Fore.RESET}self inflected harm {b+Fore.RED}:>{Fore.RESET} 4
{b+Fore.RED} | {Fore.RESET}nsfw material {b+Fore.RED}:>{Fore.RESET} 5
""")

token = input(f"{b+Fore.RED} >> token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
if r.status_code == 200:
        pass
else:
        print(f"{b+Fore.RED} > INCORRECT TOKEN")
        input()
guild_id1 = input(f"{b+Fore.RED} > Server ID{Fore.RESET}: ")
channel_id1 = input(f"{b+Fore.RED} > Channel ID{Fore.RESET}: ")
message_id1 = input(f"{b+Fore.RED} > Message ID{Fore.RESET}: ")
reason1 = input(f"{b+Fore.RED} > Option{Fore.RESET}: ")


def Main():
  global sent
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
      }

  payload = {
    'channel_id': channel_id1,
    'guild_id': guild_id1,
    'message_id': message_id1,
    'reason': reason1
  }

  while True:
    r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
    if r.status_code == 201:
      print(f"{Fore.RED} | Sent Report {b+Fore.RED} {Fore.RED} ID {message_id1}")
      ctypes.windll.kernel32.SetConsoleTitleW(f"[ACC DEAD] By KURDO | Sent: %s" % sent)
      sent += 1
      
    elif r.status_code == 401:
      print(f"{Fore.RED} | INCORRECT TOKEN")
      input()
      exit()
    else:
      print(f"{Fore.RED} | Error")


print()
for i in range(500, 1000):
    Thread(target=Main).start()