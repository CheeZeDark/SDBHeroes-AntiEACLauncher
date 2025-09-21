import shutil
import os.path as p
import os as n
import pefile
from os import _exit as exit
from Mus_Force import PlayMusic_AlanWalkerForce

def Main():
    PlayMusic_AlanWalkerForce()
    dragonballheroes_realfile = "Launch_Game.exe"
    if(p.exists(dragonballheroes_realfile)):
        PE_DragonBallHeroes = pefile.PE(dragonballheroes_realfile)
        print("Real Size of Fake Launcher of EAC(EasyAntiCheat): {}".format(PE_DragonBallHeroes.OPTIONAL_HEADER.SizeOfImage))
        input_yes = input("Do you Want to Copy This Fake EAC Launcher(Super Dragon Ball Heroes)?")
        if(input_yes == "y"):
            shutil.copy2("C:\\Program Files (x86)\\Steam\\steamapps\\common\\SUPER DRAGON BALL HEROES WORLD MISSION\\Launch_Game.exe", n.getcwd() + "Launch_Game_TMP.exe")
            print("PLS DO NOT TOUCH Launch_Game_TMP.exe(IN TEMP FOLDER) \nIF YOU WANTED, YOU CAN RENAME THIS TO LAUNCH_GAME.EXE AND COPY TO LICENSE FOLDER OF SUPER DRAGON BALL HEROES TO RETURN ONLINE MULTIPLAYER!!!")
            shutil.copy2(dragonballheroes_realfile, "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SUPER DRAGON BALL HEROES WORLD MISSION\\Launch_Game.exe")
            print("Successfully Copied!!!")
            tmp_reallauncher_superdragonballheroes = n.getenv['TEMP'] + "\\Launch_Game.exe"
            shutil.copy2("Launch_Game_TMP.exe", tmp_reallauncher_superdragonballheroes)
            n.remove("Launch_Game_TMP.exe")
            print("Successfully Bypassed EAC Protected Game Super Dragon Ball Heroes!!! \nCreated By Rikko Matsumato!!!")
            exit(3112)
        else:
            exit(4321)

if __name__ == "__main__":
    Main()