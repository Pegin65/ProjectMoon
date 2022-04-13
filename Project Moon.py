import os
import requests
import sys
from dhooks import Webhook
from pystyle import * 
import socket
import re
import json
from threading import Thread
from urllib.request import Request, urlopen
#module de billythegoat356
#created by Pegin56 in github.

sys.stdout.write("\x1b]2;Project moon by 667_lucass in ig or Pegin65 in github...\x07")


def banner():
    print(Colorate.Horizontal(Colors.white_to_black, """                                     
            §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
            §§§§§§§§§§§§§§/#&@@@@&##/§§§§§§§§§§§§§§§
            §§§§§§§§§§/&$%*%%%%%%%$$$@@#§§§§§§§§§§§§
            §§§§§§§§/@$%%%%$$$$%%$$$$$$$@&/§§§§§§§§§
            §§§§§§/@$$$%$@@@@$$$$%%$$$$@@@@#§§§§§§§§
            §§§§§#$$$$$$@@@@@@$$$$$@@@@@$$$@&/§§§§§§                                  
            §§§§#$@$%$$$$@@@@$$$$$@@@@@&$$$@@#/§§§§§
            §§§/$@@$$$$$$$$$$$$$$@@@@@&&@@&@@&/§§§§§
            §§§@%@@@$%$$%%*%$$@$$@@$$@&&&&&&@@&/§§§§
            §§§%*@@@$%%$%%%$$@@$$%%%%$@&&@@&&&#/§§§§
            §§§%*$@@@@$$$$$$$$%%%%*%%%%$@$$@&##/§§§§
            §§§@!%$$@$$$$@$%$$%%%%*%%**%$$$$@&#/§§§§
            §§§/*!*%%%$$$$$$$$$%%%%%%%%*%@@$@&#§§§§§
            §§§§#!!**%$$%$$$@@%***%*%%%%%$$$@&#§§§§§
            §§§§§#*!!*%%%$%%%%*!!***%%%%%$$$@#§§§§§§
            §§§§§§/$!!******!!!!!****%%%%$$&/§§§§§§§
            §§§§§§§§/$******!!!!!**%%%%%$@#§§§§§§§§§
            §§§§§§§§§§§#$%*!!!!!!***%$@&/§§§§§§§§§§§-
            §§§§§§§§§§§§§§/#&&@@@@&#/§§§§§§§§§§§§§§§
            §§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§  """, 1))

    print(Colorate.Horizontal(Colors.black_to_white,  """                           
     ______________________________________________  
    |                                             |
    |     [1] webhook deleter                     |
    |     [2] webhook sender                      |
    |     [3] webhook spam                        |
    |     https://discord.gg/AQJb2syW             |
    |                                             |
    |     By 667_lucass in ig...                  |
    |_____________________________________________|
""", 1)) 


def main():
    banner()
    choice = input(Colorate.Horizontal(Colors.white_to_black, "    Choice : ", 1))




    if choice == "1":
        os.system('cls' if os.name=='nt' else 'clear')
        print(Colorate.Horizontal(Colors.white_to_black, """
                                                                    
                                                        ::!*%*!!*%
                                                    :!*$$@@@&&$%*!                                                                       
                                                 !*%%%$@&&&&&&&&$:
                                              :*$$$$$$$$@&&&&&&@! 
                                           :*%$$$%$$$@@$$@@&&&@%  
                                         :%$$$$**%%%%%$$$$$@@@%   
                                       !%@$$$@%!%%%%$%%@$$$$$*    
                                     :%$$$@$$@%!*%%%$%%@$$$$*                                                                                                                                                                                        
                                   :*$$$$$$@@@@$**%%%$$$$$%:      
                                  !$$$$%%%%%$$$@@$$$$@$$$*        
                           :*****%@$$@$!*%%$%%@$@@@$$$$%:         
                        !!!*%%%$&&@@$@@**%%%%$$$@@@@$%!           
                       !*!!***%%&&@@@@$@$%%$$@$$$@$%!             
                      !****%%%%@&&&@&@@$@@@@$$@@$*:               
                     !*******%$$@$%@&&&@@@$@@@%!:                 
                    !*!:::!*****%$@&&&&&&&@$*:                    
                   !*: :!*******%$$$@@$%@@$!                      
                   : :!%$%***!!!***%%%**%%%*                      
                    :*$@$%*!!!*%%:!%%*****!:                      
                   :*@@%***%%$%*::*******:                        
                 ::!%@$$$@@$%!:::****!!::                         
                ::!$&@@&@%*:::!!*!!::                             
               ::!$$%%%*::   :!::                                 
             ::!!**!!!::                                          
            :!!!!:::::                                            
         ::!!!::                                                  
       ::!!!:                                                     
     :::!::                                                       
  ::::::                                                          
::::                                                              
                 :**:!!!!!!!!!::!!**!:!!!:::::!:                  
                 :**:!!**!*********!!****!!****!                  """,1))


        try:
            Webhookdeleter = input(Colorate.Horizontal(Colors.white_to_black, "   Veuillez entrez le lien du webhook a détruire. : ", 1))
            webhookchecker = requests.get(Webhookdeleter)
            if webhookchecker.status_code == 404:
                print("le webhook n'a pas était trouvé ou a était détruit. ")
                time.sleep(2)
                os.system('cls' if os.name=='nt' else 'clear')
                main()
            if webhookchecker.status_code == 10015:
                print("le webhook n'a pas était trouvé ou a était détruit.")
                time.sleep(2)
                os.system('cls' if os.name=='nt' else 'clear')
                main()
            if webhookchecker.status_code == 401:
                print("le webhook n'a pas était trouvé ou a était détruit.")
                time.sleep(2)
                os.system('cls' if os.name=='nt' else 'clear')
                main()
            else:
                hook = Webhook(Webhookdeleter)
                print("   Destruction . . . ")
                x = requests.delete(Webhookdeleter)
                print("    Webhook détruit avec succes.")
                time.sleep(3)
                os.system('cls' if os.name=='nt' else 'clear')
                main()
        except:
            print("[!] format de webhook incorrect, retour au menu !")
            main()


    if choice =="2":
        os.system('cls' if os.name=='nt' else 'clear')
        print(Colorate.Horizontal(Colors.white_to_black, """""                                                  :!::!!:                             :!:      
                            :*%%%%%%%%%%%%%*******$&@@@&@$%%%%%%%*********!!!         %&*      
            :::::::     ::!$@&&&&&&&######@$%%%%%$@&&&&&&&@$$@@$$$$@&@%%$$%@@*!::::::!%%%::    
   !%%%%%%%%%%%$$$%%%%$$@@&&&&##&###########&###########&&&&&&@@$$$$@$%%%%%$@@@$%%%%%$@@$%*:   
   $&@@@@@$$$$$@@@@@&&#&&&&@&#######@@@##/#####&%%%*%$$%***!!!!!!!!!:::::::::::::::::::::      
   %#&&&&&&&&&&&&&@@@$%*!:::$&&&&@!*   @&$////##*                                              
   !@&&&&&&&@@$$%*!:        %&&&$!::::::! $/#/#&&:                                             
   :@&&@@$%*!:             !&&&$:         :&//###@:                                            
    !!!:                  !@&&@:           !&///##@!                                           
                          *@&@*             :&///##&%:                                         
                           :::               :$///###@$!                                       
                                               !@////#&!                                       
                                                 !@#/@:                                        
                                                   !%:                                         """, 1))
        try:
            Webhooklien = input(Colorate.Horizontal(Colors.white_to_black, "Lien du webhook pour envoyer un messages. : ", 1))
            Webhookmsg = input(Colorate.Horizontal(Colors.white_to_black, "Message a envoyez. : ", 1))
            data = {
                "content" : "",
                "username" : "Project moon"
            }
            data["embeds"] = [
            {
            "description" : f"{Webhookmsg}",
            "title" : "Project moon"
            }
    ]
            result = requests.post(Webhooklien, json = data)
            print("\n\nMessage envoyé.")
            time.sleep(3)
            os.system('cls' if os.name=='nt' else 'clear')
            main()
        except:
            print("[!] format de webhook incorrect, retour au menu !")
            main()

    if choice == "3":
        os.system('cls' if os.name=='nt' else 'clear')
        print(Colorate.Horizontal(Colors.white_to_black, """ 
        
                                         ::!!*%%* 
             : :!:      :::!!***%$$$%%*!: 
        *%*$@@$@%!*%$$$***!!!:::         
        : !%@#@&&&@@@$$@$*                 
    :%$@&&@$##&@$%!:    %!*!                
    !#//&&&$/%:         %: *!               
    $@%:::!!:         :%   %:              
     !!!:::::          :!   :              """, 1))

        try:
            Webhooklien = input(Colorate.Horizontal(Colors.white_to_black, "lien du webhook à spam. : ", 1))
            Webhookmsg = input(Colorate.Horizontal(Colors.white_to_black, "Message à spam : ", 1))
            data = {
                "content" : "",
                "username" : "Project moon"
             }
            data["embeds"] = [
            {
            "description" : f"{Webhookmsg}",
            "title" : "Project moon"
            }
    ]

            count = 0
            while (count < 50):   
                count = count + 1
                print(Colorate.Horizontal(Colors.white_to_black,"Messages Envoyé" ,1)) 
                result = requests.post(Webhooklien, json = data)
            print("\n\nSpam finis...")
            time.sleep(2)
            os.system('cls' if os.name=='nt' else 'clear')
            main()   
        except:
            print(Colorate.Horizontal(Colors.white_to_black,"Webhook non valide" ,1))
            main() 


    if choice == "4":
        os.system('cls' if os.name=='nt' else 'clear')
        print(Colorate.Horizontal(Colors.white_to_black, """ 
        
                                         ::!!*%%* 
             : :!:      :::!!***%$$$%%*!: 
        *%*$@@$@%!*%$$$***!!!:::         
        : !%@#@&&&@@@$$@$*                 
    :%$@&&@$##&@$%!:    %!*!                
    !#//&&&$/%:         %: *!               
    $@%:::!!:         :%   %:              
     !!!:::::          :!   :              """, 1))


      




if __name__ == '__main__':
    main()

