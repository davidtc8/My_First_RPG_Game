import codecs

logo = """
░           ░░▓▒▓░  ░░▓▒    ▓░░░▒░░▒                        
            ░▒▓▓█   ░ █░   ▒░░░▒░░▓                   ░     
░          ░▒▒▓█▓  ░▒░█  ▒▒░▒▒▒▒░█░                ░▓▓▒     
           ▒▓░▓█   ▓░░█▓▒▒░▒▒▒▒░▓▓ ░         ░░░ ░▒▓▒       
░         ▒▓░░▓▒  ▓▓▒▓█▒ ░▒▒▒▒ ▒█▓▓░░░░ ░  ░▒▒░░░▒▒         
         ░▒▒ ▒█░ ▓▓▓▓▓░ ░▒░▓▒ ▓██▒▒░▒▓▒▓▓▒▓▒░ ░▒▓░          
        ▒░█ ▒▒██▓▓▒▒▒▒ ░▒▒▒▓ ▒█▓▒▒▒░▒▒▒▓▓▓░░░░▒█░           
       ░░▓█░▒▓██▒▓░▒█░░▓▒▓▓▒░██▒▒▒▓▒▒▒░▓▓░ ▒▓░█▒            
       ░░▓▓▒ ▒▒▒▒▒▒██▒▒▓▒▓▓░██▓▒▓▓▓▓▓░▒▓▒▒░█▓▓█             
       ░▓▓▓▓▒▒▒░▒█▓▒░▒▓▓▓▓▒░██▒▒▒▒▒▒░ ▓▓▒░▒▓▒█▒             
░      ░▓▒▓▒▓▓▒░█▒▒░▒░▒▒▒▓▒▒██▒░▓▒▒  ▒▓▒▓▒▒▒ ▓▓░            
       ░▓▓▓▒░▒█▓░░▓▓▓▓▒▒▒▓░██▓ ▓█░  ▓█▒▒░▓▓  █▒▒▒▒▒▒▒▒▒▒░░  
░       ▓█▓▓▒░█▒▒█▓░▒█▓▒▓░▒█▓ ░█░  ▓█▒░▒▒░  ▒████▓▒▒░░░░░░░ 
       ░█▓ ▒▒ ▓▓▓▓░▒░▓░▓▓░▓█  ▓▓  ▓█▓▒▒░   ▒█▓░█▒░░░        
░      ░█░  ▓▒▓▒▒▒▓▓▓▒▒█▒▓█▒▒▒█░░░██▓░   ▒███▓░▒▓▒░░░░░░░░░ 
       ▒▓   ░█▓▒▒▓▓░▒██▒ ▓▓  ██▓░ █▓   ░▓█▓▒▓▓▒▒█▓▓▓▓█▓▓▓▓▓▒
░      ▓▒  ░▒█▓▒▓█▓▒▒▓▓░  ▓ ░█ ▒░░▓▒░░░▓█▒▒▒░▓▒░▒▓██▒░░     
       ▓█ ░▒▒▓▓▒██▓▒▒▒▓░  ▓ ▓▓  ▒░▓▒ ▒██▒░░░░█▒▒▓▓▓▓░       
        █▒▒░▒▓▓▓█▓▓░░▒▓░ ▓░ █▒  ░▒▒  ██▓▒░░▒ ▓▒▒▒▓▒░░░      
        ░█ ░▒▒▓█▓▓▒▒▒▓▒░░█ ▓▒░  ░░▒▒███▒▓░ ▒░█▒ ░▓▓▒▒▒▒▒    
        ░▓▒░ ▓▓█▓▒▒▒░░░░▒░▒▓▒░ ▒▒░▒░░░░▓▓ ░░░█▓░▒▓▓▓▓▓███▓  
        ░▒ ░▓▓██░░░  ▒▒░▒▓▒░   ▒▓▓▒▒░▒▓▓▒ ░░ █▓░ ▓▓▒░░ ░▒▓▓▒
░        ▒▒▒░▒█▓░  ▒░░▒▒▒░   ▒▓██▓████▓░░ ░░ █▒░░▒▒▓▒░░   ░░
         ░▒ ▒▓▒░ ▒▒░ ░░░░░▒▓██▓▒░ ░█▓▒░   ░░ █▒░░▓▒▓██▓▓▒░  
         ░░▒█▓▒▒▒▒░ ░░░░░▓█▓█▓▒░░░ ▒▓▒░  ░▒░▒█▒░░▓▓░ ▒▓▓▓█▓░
        ░▓▓▒▒▓▒▓▒░░░░▒░▒█▒   ▒░░░░░▓▓▒░░ ░▒ ▓▓▒▒ ▓░       ▒▓
░       ▓▓░ ▓▒░█▒░░░░▒░▓▒     ░ ░▒▒▓▒░ ░ ░▒ ▓▒▒▒▒▓▓▒▒       
        ▒▒ ▓▒░░▓▒▒░░░░▓░      ▓  ░▒▓░  ░ ▒ ▒█▒▓▒▒▓▓▒▓▓░     
░        ▒▓  ░░▒▒░░░░▓█      ░▓░ ░▓▒▒ ░ ░▒ ░▒▒▓░░▒▒▒▒▒▒░    
          ░  ░ ░░░░░░██     ░░▒░░▓▒░░ ░▒░░ ▓▒░▓▒░▓▓▒░░░     
░          ░░ ▒▒▒░  ▓▒░▒   ░░▒  ▒▓▒▒ ░░░▒ ░▓▒▒▒░▒▒▒░░░░     
             ░▒░░▒▒▓█      ░▒  ░▒▓▒░ ░ ░░ ▒▓░▒▓░░▒   ░░░    
░                ░▒▒▓▒  ░░░▒░ ░░▒░░   ░▒░░█▒░▒▒░▒░     ░    
                   ░░▒▒ ░░▒  ░░░░    ░▒  ▒▓▒▒   ▒▒          
░                     ░░░░  ░▒░      ░░ ▒▓▒ ░░░ ▓▒          
                                      ░▒░ ░░  ░▒▒▒                                                                                                                                                     
"""

logo2 ="""
   *               (                               (      (              
 (  `              )\ )                      )     )\ )   )\ )   (       
 )\))(    (       (()/(   (    (          ( /(    (()/(  (()/(   )\ )    
((_)()\   )\ )     /(_))  )\   )(    (    )\())    /(_))  /(_)) (()/(    
(_()((_) (()/(    (_))_| ((_) (()\   )\  (_))/    (_))   (_))    /(_))_  
|  \/  |  )(_))   | |_    (_)  ((_) ((_) | |_     | _ \  | _ \  (_)) __| 
| |\/| | | || |   | __|   | | | '_| (_-< |  _|    |   /  |  _/    | (_ | 
|_|  |_|  \_, |   |_|     |_| |_|   /__/  \__|    |_|_\  |_|       \___| 
          |__/                                                                                                     
"""

enemy_list =  {"skelleton":
"""
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \
               f'. _,,-'                   \ \
              ()--  |                       \ \
                \.  |                       /  \
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \
                                             |lllj
                                             |||||
""",
    "dragon":
"""
                                             ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`
""",
"woods":
"""
▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▒▒▒▒▒▒▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒█▒░░▓▒█ ░█▓░ ▒█▒░▓▓█▓▒▒▒▒▒▓░▒▒▓▓▓█░░▓▓▓▒▓▓▒▓▓▒▓▓▓░░▓█▓▒██▒
▒░ ▒▒▓▓▓▓   ░▓▓ ░░░▒▓▓▒▒▒▓█▓▓████▓▓▓▓▒▒▒▒▓█░░▒▓▓▓ ░▓░ ░▒█░░▓▓█▒░░░░░ ░░░▓███░░░░▒▒▓▓▒▒▒▒▓▓▓▓▒▓▓▓▓▓▓▓
▓░ ▒▒▒▓▓▓░░▒▒▓▓░▓░▒░▓▓▒▓▒▓▓▓▓▓▓█▓▓███▒▓▒▓▓▓░▒▒▓█▒ ░▒▒▒▒▒▓░▒▓▓█▒░▒░░░▒▒░▒▒▓▓█▒▒▓▒▓▒░ ▒▓▓▓▒░▒▓█▓░▒█▓▓▓
▓░ ▒▒▒▒▓▒░▒▒░▓▓▒▒░▒░▓▓░▓▒▓▒▓▓▒▓▓▒▒▓▓▓▒▓▒▓▒▒░▓▒▒█▒ ░██▒ ▓▓▒░▒▒█▒░▒▓▓▒░▒░▒▒▒▒██▒▒▓▓▒▒▓▓▓▓▒░▓▓▒▒██▓▒▓██
█░ ▒▒▒▓▓▒▒▒░▒▓▓░░░▒▒▓▒▒▒▓▓▒▒▓▒▓▓▓░▒▓▓▒▒▒▒▒▒░▒▒▓▓▓░▒▓░ ▒▓▓▓░░▓█▓░▒▓▒░▒░░░▒▒▓▓█▒▒░▒▒▓▒▒▒▒░▒▒▒▓▓▓██▓▒▒▓
█░░▒▒▒▓▓▒░░▒▒▓▓▒▒░▒▒▓▓▒▒▓▓▒▒▓▒▒█▓▒▒▓█▓▒▒▒░░░▒░▒▒▒ ░▒░▓▒░▓▒░▒▓█▓▒░▒▓▓░▒▒░▒▒░▓▓░▒▓▒▒▒▒░▓▒░▒▓▓▒▒▓▓▓██▓▓
█░░▒▒▒▓▓▒░▒░▒▓▓▒░░▒▒▒▒▒▒▒▓▒░▓▒▒▓█▒▒▓█▓▒▒▒░░░▒░▓▒▒░▒▒▒▒ ░▓░░▒▓█▒ ░▒▒░▓▒▒░▒▒▒▓▓░▒▒▒░▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓█▓
█░░▓▒▓▓▓▒▒▒░▒█▓░  ▒▒▓░▒▓░█▒░▒▓▒▒█▒▒██▓▒▒▒▒░ ▒░▓▓▓ ▒▓▒░░▒▒▒░▒▒█▒▒▓░▒▓▓░░▓▓▒░▓▓▒▒░▒▒▓▒▒▒▒▒▓▒▓▓▓▓▓▓▒▒▒▓
█░▓▒▒▓▓▓▒▒▒░▒█▓   ▒▒▓░▒▓▒▓▓▒▓▓▒▒█▒▒█▓▒▒▓▒▒░░ ░▒▓░░▓▓░▓▓▒▒▒░▒▒█▒▒▓▒▒▒▒▓▒▓█▒▒█▓▒▒▒▓▒░ ▒▓▒░▒▓▓▓▓▓▓▒▒▓▓░
▓▒▓░▒▒▒▓▒▒▒░▓█▒   ░▒░▒▒▓▒▓▓▒▓▒▒▓█▓▒▓▒░░▓▒░ ░ ░▒▒ ░▒▒▒▓▒░░▒▒▒▒█▓░▒▒▒▓▓▓▒░▒▒▓█▒░▒▒░▒▒▓▓▒▒▒▓▓▓▓▒▓▓▒▒▓▓░
▓▒▒░▒▒▒▓▒░  ▓█▒ ░ ░▒░▒▒▓▓▓▓▒▓▒▓▓█▓▒▓▒ ░▒█░   ░█▒  ▓▒░ ░▒░▒▓░▒█▒ ░▒▓▓▓▒░ ░▒▓▓  ░░▓▓▓░▒▓▓░▒▒▓░ ▒▓░▒▓▓░
▓░░▒▒▒▓▓░░ ░▒█▓   ░▒▒░▒▓▓▒▒▓▒▒▒▒█▓▒▓▒ ░░█▓░ ░▒█▒  ▒▒  ░░░▓▓░▓█▒░▒▒▓░░░░▒▒ ▓▓  ░▒▒▒░ ▒▓▒▒▓▓▓░ ▓▒▒▒██░
▓ ▒▓▒▓▓█▒  ░▓█▓ ░ ░▓█░▒▓▒▓▒█▓▒▓▒█▓▒▓▓  ▒▓█▓ ░▓▓▒  ▓▒     ▒▓░▒▓  ▒▒▓   ░▓▒░▓▓  ░ ▒▓░ ░░░ ░▒▓  ▓▒▒▓▓█░
▒ ▒▒▒▓▓█▒  ░▓▓▓   ░▓█▒▒█▒▓▒▓▓▒▒▓█▓▒▒▓░ ░▒█▓░ ▓█▓  ▓▓   ░▒▒▒▒▒█  ░░▓   ░░▒▒▒▓    ░▓   ▒░ ░▒▓  ▒▓░▒▓█▒
▒ ▒▒▒▒▓▓▒  ░▓▓▓   ▒▒█▒▒▓▓▒▓▒▓▓▒▓█▓▓▓▓▒ ░▓██░ ▒▓▒ ░▓▓   ░▒▒▒░▓█ ░░░▓   ░ ▒░▒▓    ▒▓  ░▒░ ░▒█░ ░▒▒▒▓█▒
▒ ▒▒▒▓▓▓▓░ ▒▓▓█░  ▒▒█▒▒▓▓▒▓▒▓▓▒█▓▒▒▓▓▒ ░▓█▓░ ▒▓▒ ░░▓   ░▒█▓▒▒▓ ░ ▒▒   ░░▒░▒▒    ▒▓  ░▒░  ▒█░ ░░▓▒▓▓▓
▒░▒▓▒▓▓▓▓░░▓▓▓█▒░░▒░▓▓▒▓█▒▓▒▓▒▒█▓▒▒▓▓▒▒▒██▓  ▒▓▒░▒▒▓▓▒░░▓▓█▒▓▓░░▒▒▓▒▒░ ░▒▓▒▒   ░▓▓░ ░▒▒  ▒█░ ░▒▒▒▓█▓
▒░▒▓▒▓▓▓▓▒░█▓▓██▒░▒░▓█▒▒█▒▒▓▓▓░██▒▒▓░▓▓▒██▒ ░▒▓░ ░░░▒▒░▒░░▓░▓▓   ░░▒▒▒ ░▒▒▒▒ ░░▒▒▓▒▒▒▓█░ ▒█▒░▒▒▒▒▓▓▓
▒░▒▒▒▓▓▒▓▓▒▒▒▒▓▓▓▓▓ ▓█▒▒█▒▒▓▓▓░▓█▓▒▓░▒▓░█▓░ ▒▒▓░ ░░░░ ░░░░▒▒▓▒░░░░░    ░▒░▓▒░░░░░░░░▒░▒░ ▒▓▒░░▓▒▓▓█▒
░ ▒▓▒▓▓▓▓▓▒▒▒▒░░░░▒░▓█░▓█▓▒▓▓▓▒▒█▓▒▓░░▓░█▒ ░▓▒▓░ ░░░░░░░░▒░░▓▒     ░░  ▒▒▒▓▒ ░░░░░ ░ ░░░░▓▒▒▒░▒▓▓██▒
░ ▒▓▓▓▓▓▓▓▒░░░░░░ ░▒█▓▒▓▓▓▒▓▒▓▓▒██▓▒▒ ▒░▓▒ ▒▒░▓░      ░░░▒▒▓▓░     ░░ ░▓░░█▓   ░░░░░░▒▒░▒▓▓▓▓░▓▓▒▓█▓
 ░▓▓▓░▓▓▒█▓░░░░░░░░▒█▒▒▓▒▓▒▓▒▓▓██▓▓░▒▓░ ▒░░░▒▓█▒       ▓░▒▓▓▓░ ▒▓▓▒░░▒▒▒▓░▒▓▓▒░            ░▒░▓▓▒▓▓▓
 ▓▓▓▒▒█▓▒▒█▓▒▒▒▒▒▒▒▒█▒▒▓▓▓▒▓▓▓▓██▓▓░▒▓▒ ▒▓ ░▓██░      ░▒░▒▓▒█▒ ░░░░░▒░░░▓▓▓▒▒▓▓▒▒▒▒░▒░░░    ░░█▓▓▓█▒
▓▓▓▓▒███▓░▓█▓▒▒▒▒▒░▒▓▒▒▓▓█▒▓▒█▓█▓▓▓▓▒▒▓░░█▒░▓██░ ░░░  ░▒ ░░░▓░             ░░▒▒▒▒▓▒▒▒▒▒▒▒▒░░▒▓▒▓▓▓▓▓
▓▒▓▓▓▓█▓▓▓▓▓█▓▓▓▓▒▒░▓▓▒▓▓▓▒▒▓█▓█▓▓▓▓▒░▓░ █▓░▒▓█░░░▒▒░░▒█▒ ░░▒▓                    ░░░░░░░░░▒▓▒░▒▓█▓▒
▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▓▒▒█▓▒█▓▓▓▒▓▓▓█▓▓▓█▒ ▓▓ ▒█░▓▓█░ ░░░ ▒ ▒░░▒▓▒█▓▒▒▒▒▒░░░░                ░▒▓▓▒▒▒▓▒▓█▓
▓▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒█▓░█▓▓▓▓▓▒▓█▓▓▓█▓░▓█░░█░▒██     ░▒ ░█▓ ▓▓▒▒░░░░▒▒▒▒▒▒▒░░░░░         ░▒▓▒▒▓▓██▒▓█
▒░▒▒▒▒▒▒▒▒░▒▒▒▒▓▒▒▒▒█▒░█▓▓▓▓▓▒▓█▓▓░▓█▓██░░█▒░▓█░ ░░▒▓░░█▓▓░░▓▓░░░     ░░░░░▒▒▒▒▒▒▒░░░▒▒▒▒▒░▒▒▓▓▓▓█▒▒
▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓█░▒█▓▓▓▓▓▒▒█▓▓▒░███▓▒░█▒░▓▓▓░▒▒▒▓▓▓▒▒▒▓▒▒▓▒░░▒▒░          ░░░░░░▒▓▓▒▓▓▓▓▓▒▒▒▒▓▓▒
▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▓▒ ▓█▓▓▓▓▓▒▓█▓▓▓░░███▒▒█░ ▓▒▓▒░░░▒▒▒░▒▒▒▒▒▒▒▒▒░▒▒▒▒░              ░ ░░▒▒▒▒▓▓█▓█▓▓
░░░░░░░░░▒▒▒▒▒▓▒▒▒▓▓░░▓█▓▓▓▓▓▒▓██▓▓▓░▓██░▒▓░░▓▒ ▓▒░░░░░  ░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░              ░░░▒▒▓▓▓▓
░ ░░░░░░░░░░░░▒▒░▓▓▒░░██▓▓▓▓▒▒██▓█░▒░▒███▓░░▓▒█▓░▓▒░ ░░░░░░   ░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒░░            ░░▒▓▓
░░░░░░░░░░░░░░░ ░▓▒▒ ▒█▓█▓▓▓░▓██▓██░ ░██▓▒▓ ░▒▒█▓░▓▓░  ░▒▒▒░░░░░      ░░░░░░░░▒▒▒▓▓▓▓▒▒░░░░ ░░░░░ ░▒
▒▒▒▒▒▒░░░░░░░░░ ▒█▓░░██▓▓▓▓▒░████▓▓▓░░██▒ ▓▒  ▒▓██▒▒▓▒       ░░░░▒░░░░░░            ░░░░░▒▒▒▓▓▓▓▒▒▒▒
▒▒▒▓▓▒▒▒▒▒▒░░░░ ▓█▓▒▓█▓▓▓▓▓░▒█████▒▒▒░██▓ ░█▓░░░███▓▒▓▓              ░▒░▒░░░░░░░░           ░░▒▒▒▓▓▓
▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▒▓▓▓▓█▓▓░░███████▒░▒▓██░░███▓ ░████▓▓▓                 ░░░▒▒▒▒▒▒▒▒▒▒░░░░░░   ░ ░░░
▓▒▒▒▒▒▒▒▒▒▒░▒▒▓▓▒▒▓▒▒▓██▒░ ▒███████▓░▒▒▒█▓░░▓███ ░▓███▓▓▒                      ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░
▒▓▓▓▒▒▒▒▓▓▓▓▓▒▓▓▒▓▓▒▓█▓░ ░▓██▓██████▓▒░░▓█▒  ▒███  ░▒██▓█                               ░░░▒▒▒▓▓▓▓▓▓
▓▒▓▒▓▓▓█▓▓▓▒▓▓▓▒▓▓▒▓██▒  ▒██▓████████▓▒░ ▓█▒░ ▒███░  ▒█▓█▒                                   ░░░▒▒▓▒
▓▓▓▓▓▓▒▒▒▓▓█▓▓░▒█▒▒██▓▒░▓██▓▓█▓███████▒░░░██▒  ████▒  ▒▓▓█▒░ ░ ░░    ░░░░░░    ░░░░░   ░ ░░  ░░░░░░░
▓▓▓▓▒▒▓███▓▒░░▒▓▒▒██▓▒▓███▓▒▓██████████▓▒░░▓█▓▒▒▒▒▓██░ ░▒▒▓█▓▓▒▒░░░░  ░░░░░ ░░░ ░░▒░░▒▒▒▒▒▒▒▒░░░▒▒▒▒
▓▓▓▓▓▓▓▓▒▒▒▒▓██▓▓█▓▒▒▓█▓▓▒░▓▓▒▒▒▓▓▓▓▓▓███▒░░▒███▒▒▒▒▓▓▒░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░ ░░░░░▒▒▒▒▒▒▒▒▒▒▒
""",
"chapter1":
"""
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░ ░░░░░ ░░░░░ ░ ░ ░   ░                                 ░░░░▒▒▒▒░░░         ░ 
░                                                                                                                          ░░░░░░░                    
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░ ░░░░░░░ ░░░ ░ ░ ░ ░ ░   ░               ░░░░░░▒▒▒▒░░░░░                         
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░ ░░░░░░░░░ ░ ░░░ ░ ░░░ ░ ░ ░ ░            ░░░░░▒▒▒▒▒░░░░░░                                  
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░ ░ ░ ░ ░             ░░░░▒▒▒▒▒▒▒▒▒░░░░                                           
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░ ░░░ ░ ░ ░ ░           ░░░░▒▒▒▒▒▒▒▒▒░░░░                                                    
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░ ░ ░ ░             ░░░░▒▒▒▒▓▒▒▒▒░░░░             ░ ░ ░       ░                                   
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░          ░░░▒▒▒▒▒▒▒▒▒▒▒░░░░             ░ ░ ░ ░     ░   ░ ░                                      
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░         ░░░░▒▒▒▒▒▒▒▒▒▒▒░░░            ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░   ░ ░                                         
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░        ░ ░░░ ░ ░ ░ ░░░ ░░░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░░░   ░                                    
░ ░░░░░░░░░░░░░░░░░░░░░░░ ░     ░░░░▒▒▒▒▒▒▓▒▒▒▒░░░░           ░ ░░░░░░░░░ ░░░ ░░░░░░░░░ ░ ░ ░░░░░░░ ░ ░ ░ ░ ░   ░     ░     ▒█▓                       
░░░░░░░░░░░░░░░░░░ ░ ░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░         ░ ░░░░░░░░░ ░ ░░░░░░░░░░░░░ ░ ░░░░░░░░░ ░░░░░░░ ░ ░ ░ ░ ░ ░ ░ ░ ░      ░████▒                      
░ ░░░░░░░░░ ░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░       ░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░   ░     ░░  ██▒                     
░ ░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░   ░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░ ░ ░ ░ ░     ░        ░██░                    
▒▒▒▒▒▒▒▒▒▒▒░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░ ░ ░ ░ ░ ░ ░ ░                  ▒██                    
▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░░░░░░          ░ ░▓▓░   ░        ▓█▓                   
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▓   ░ ░ ░   ░░░    ▒█░████▒ ░   ░ ░    ▓█▓                  
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░█▒        ▓█▓▓██▒ ░███▓ ▓█▒  ░░  ░ ░    ██▒                 
░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░  ▓██▒▒██░  ██░   ▒██▓▒██▓     ░░  ░ ░     ░██░                
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░█▒ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░             ▓█████▓▓░ ▒█▓    ▒███  ██▒   ░ ░ ░ ░ ░ ░   ▒██                
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░         ░▒▓███  ░░░░░░░░░░░░░░░░░░░   ░░░░  ▓   █████▓░ ░░▒██▒    ▓██▒▓██▓▒░░  ░██▒   ░ ░ ░ ░   ░   ▓█▓               
░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░▒▓▓▓▓▓▒░▒█████▒  ░░░░░░░░░░░░░░░           ▒█▒ ████████▓   ▓██░   ▒███░         ▓██░  ░░ ░░░ ░ ░     ███▒▒░           
░░░░░░░░░░░░░░░░░░░░░░░░░   ▒████▓▓▓████▒  ▓███░ ░░░░     ░░░░░  ▒▓████▒  ▓████▒    ▒████░  ███    ███░   ░ ░ ░  ███  ░ ░ ░ ░ ░ ░   ▒█▓▒▒▒░           
░░░░░░░░░░░░░░░░░░░░░░░░ ░▒██▓░      ░▒██▒ ░███▓  ░   ░░░   ░░ ░██▒░░███▓░█████       ▒███▒ ▒██▓   ▒███░   ░░░   ░██▓    ░ ░ ░ ░ ░  ░                 
░░░░░░░░░░░░░░░░░░░░░░░ ▒███▒  ░░░░░░   ▓█░ ▓███░  ░▓█████▒    ██▓    ███░  ███▓  ░░░  ░███░ ▓██▒   ▓███░   ░   ░ ░██▒ ░░ ░░░░░ ░░░         ░         
░░░░░░░░░░░░░░░░░░░░░░ ▒███▓  ░░░░░░░░░  ░░  ████ ░███▓█████░ ░███ ░  ▒███  ░███▒ ░░░░  ▒███  ███░   ▒███▓     ░█░ █████▒ ░░░░░░ ░ ░ ░░  ░   ░     ░  
░░░░░░░░░░░░░░░░░░░░░ ░████░ ░░░░░░░░░░░░░░░ ▒███▓█▒    ░████ ░██▒ ░░  ▓██▓  ▒███   ░░░  ▓██▒ ▒███    ░████▓▓▒▓█▓ ▓▓░░    ░░░░░░░ ░   ░ ░ ░ ░       ░ 
░░░░░░░░░░░░░░░░░░░░░░▓███▓  ░░░░░░░░░░░░░░░  ████▓  ░░  ░███▓ ░░  ░  ░████░  ▓██▓  ░░░░ ░██▓  ████  ░▓ ▒██████▓       ░ ░░░ ░░░ ░ ░ ░ ░       ░      
░░░░░░░░░░░░░░░░░░░░░░████▓ ░░░░░░░░░░░░░░░░░ ░███▓  ░░░░ ▒███▒  ░░  ▒█▒▒██▓  ░███▒ ░░░░  ██▓   ██████▓    ░░░    ░ ░░░░░░░░░░░░░░░ ░ ░░░ ░ ░         
░░░░░░░░░░░░░░░░░░░░ ▒████▓  ░░░░░░░░░░░░░░░░  ▓███░ ░░░░  ████  ░  ▓█░  ███▒  ▒███  ░░  ░██░    ▒▓██▒         ░░░░░░░░░░░░░░░░░ ░ ░ ░ ░ ░       ░░▒▒▒
░░░░░░░░░░░░░░░░░░░░░▒█████░ ░░░░░░░░░░░░░░░░░ ░███▓  ░░░░ ░███▓   ▓█▓   ░███   ▓███░    ██▓  ░░       ░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░      ░░▒▒▒▒░  
░░░░░░░░░░░░░░░░░░░░ ▒█████▒ ░░░░░░░░░░░░░░░░░░ ▒███▒ ░░░░  ▓███░ ░███    ████  ▓█████▓▓██▒  ░░░░░ ░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░▒▒▒▒▒░      
░░░░░░░░░░░░░░░░░░░░░░██████░ ░░░░░░░░░░░░░░░░░  ████░ ░░░░ ░████ ░███▓  ▒█▓████▓▒███▒▒▒░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░▒▒▒▒▒░      ░ ░ 
░░░░░░░░░░░░░░░░░░░░░░▒█████▒ ░░░░░░░░░░░░░░░░░░ ░███▓ ░░░░░ ▒███▒ ▓██████░ ░███  ▓██▓   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░▒▒▒▒░░     ░ ░ ░ ░  
░░░░░░░░░░░░░░░░░░░░░░░▓█████░  ░░░░░░░░░░░░░ ░█░ ▓███░ ░░░░  ▓███▒░█████░        ░███▒  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░   ░░▒▓▓▒▒░      ░ ░ ░ ░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░ ░▓█████░ ░░░░░░░░░░░░░ ▒█▓ ░███▓   ░░ ▒██████▒░▒▒   ░░░ ░░░ ▒███░   ░░░░░░░░░░░░░░░░░░░░░░░░░    ░▒▒▓▓▒░░   ░ ░░░░░░░░░ ░ ░ ░░ 
░░░░░░░░░░░░░░░░░░░░░░░ ░▓█████▒  ░░░░░░░░░░░ ▒██  ▓████▓▓▒ ▒██▒░        ░░░░░░░░░  ▓███░ ░░░░░░░░░░░░░░░░░░░░░░    ░▒▒▓▓▒░░    ░░░ ░░░░░ ░░░░░░░ ░ ░ 
░░░░░░░░░░░░░░░░░░░░░░░░ ░▒█████▒░ ░░░░░░░░░  ███▒░███████▒░░     ░░░░░░░░░░░░░░░░░ ░██████▒ ░░░░░░░░░░░░░░░   ░░▒▒▓▓▒░░   ░░░░░░░░░░░░░░░░░░░░░ ░ ░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░  ░▓█████▒   ░░░░░  ▓██▓░██▒░░   ░░░░░░░░░░░░░░░░░░░░░░░░░▓██▓▒▒░░░░░░░░░░░░░░░   ░░▒▓▓▓▒░░  ░ ░░░░░░░░░░░░░░░░░░░░░ ░░░ ░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▓█████▓▒░░░░░▒██▓░  ░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒      ░░░░░░░░░   ░▒▒▓▓▓▒░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░▒▓██████████▒░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░░░░░░░░   ░░▒▒▓▓▒▒░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░▒▒▒▒░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░▒▓▓▓▒▒░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   ░░▒▓▓▓▒░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░▒▒▓▓▒▒░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░▒▓▓▓▓▒░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
}