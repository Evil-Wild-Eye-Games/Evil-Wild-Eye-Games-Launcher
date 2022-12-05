import os, urllib.request, time

groupname = "Evil Wild Eye Games"
launcher_version = "A-0.0.42"
launcher_directory = "C:/Evil Wild Eye Games"
launcher_directory_file = "C:/Evil Wild Eye Games/Evil-Wild-Eye-Games-Launcher.py"
game_1 = "Dungeon Escape Survival"
games_directory = "C:/Evil Wild Eye Games/Games"
game_1_directory = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival"
game_1_sound_directory = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Sound"
game_1_directory_file = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Dungeon-Escape-Survival-Alpha.py"
game_1_file = "Dungeon-Escape-Survival-Alpha.py"
game_1_download_url = "https://raw.githubusercontent.com/WLHQ/Test-Python-Code/main/Dungeon-Escape-Survival-Alpha.py"
game_1_launch = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Dungeon-Escape-Survival-Alpha.py"

#Checking if Evil Wild Eye Games directory exists
if os.path.exists(launcher_directory):
    print("The directory " + groupname + " exists and is located at " + launcher_directory)
else:
    print("The directory " + groupname + " will be created at the root of the drive.")
    os.mkdir(launcher_directory)

#Checking if Games directory exists
if os.path.exists(games_directory):
    print("The directory Games exists and is located at " + games_directory)
else:
    print("The directory Games will be created inside of the " + groupname + " directory.")
    os.mkdir(games_directory)

while True:
    user_input_launcher_menu = int(input("\nWelcome to the " + groupname + " Launcher!\nYou can view the library of games or take a look at the launchers settings.\n\n1: Game Library\n2: Launcher Settings\n\nInsert a number: "))
    if user_input_launcher_menu == 1:
        print("\nLoading Library of Games...")
        time.sleep(0.5)
        user_input_library = int(input("\nFrom here you can launch our games and download game assets as needed.\nWhich game do you want to play?\n\n1: " + game_1 + "\n2: Placeholder\n\nInput the number that corresponds with its game here: "))
        if user_input_library == 1:
            print("\nNow starting " + game_1)
        
            #Checking if Dungeon Escape Survival directory exists
            if os.path.exists(game_1_directory):
                print("The directory " + game_1 + " exists and is located at " + game_1_directory)
            else:
                print("The directory " + game_1 + " will be created inside of the " + groupname + " directory.")
                os.mkdir(game_1_directory)

            #Checking if Dungeon-Escape-Survival-Alpha.py file exists
            if os.path.exists(game_1_directory_file):
                print(game_1_file + " exists and is located at " + game_1_directory_file)
            else:
                print("The file " + game_1_file + " will be downloaded from " + game_1_download_url + " and put inside of the " + game_1 + " directory.")
                urllib.request.urlretrieve(game_1_download_url, game_1_directory_file)

            #Checking if Sound directory exists
            if os.path.exists(game_1_sound_directory):
                print("The directory Sound exists and is located at " + game_1_sound_directory)
            else:
                print("The directory Sound will be created inside of the " + game_1 + " directory.")
                os.mkdir(game_1_sound_directory)
            time.sleep(6)
            exec(open(game_1_launch).read())
            break
        elif user_input_library == 2:
            print("Placeholder")
        else:
            print("That number of input doesn't exist at this time!")
    elif user_input_launcher_menu == 2:
        print("\nLoading settings...")
        time.sleep(0.5)
        while True:
            user_settings_input = int(input("\nYou can Refresh Installed game files or Update the Launcher.\n\n1: Check the Launcher Version\n2: Refresh Game Library Files\n3: Exit Settings\n\nInsert a number: "))
            if user_settings_input == 1:
                print(launcher_version)
                time.sleep(2)
            elif user_settings_input == 2:
                if os.path.exists(games_directory): 
                    os.rmdir(games_directory)
                    print(games_directory + " has been removed from this computer. Run the launcher again to redownload the files.")
                    time.sleep(2)
            elif user_settings_input == 3:
                print("Leaving settings...")
                break
            else:
                print("That option doesn't exist! Try Again!")
                time.sleep(2)
    else:
        print("That option doesn't exist!")
        time.sleep(2)