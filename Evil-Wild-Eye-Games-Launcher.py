import os, urllib.request, time
#----End Imports----
groupname = "Evil Wild Eye Games"
launcher_version = "A-0.0.55"
launcher_directory = "C:/Evil Wild Eye Games"
launcher_file = "Evil-Wild-Eye-Games-Launcher.py"
launcher_directory_file = "C:/Evil Wild Eye Games/Evil-Wild-Eye-Games-Launcher.py"
launcher_download_url = "https://raw.githubusercontent.com/Evil-Wild-Eye-Games/Evil-Wild-Eye-Games-Launcher/main/Evil-Wild-Eye-Games-Launcher.py"
game_1 = "Dungeon Escape Survival"
games_directory = "C:/Evil Wild Eye Games/Games"
game_1_directory = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival"
game_1_directory_file = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Dungeon-Escape-Survival-Alpha.py"
game_1_sound_directory = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Sound"
game_1_file = "Dungeon-Escape-Survival-Alpha.py"
game_1_download_url = "https://raw.githubusercontent.com/Evil-Wild-Eye-Games/Dungeon-Escape-Survival/main/Dungeon-Escape-Survival-Alpha.py"
game_1_launch = "C:/Evil Wild Eye Games/Games/Dungeon Escape Survival/Dungeon-Escape-Survival-Alpha.py"
#----End Variables----
def updater():
    # Get the updated file
    response = urllib.request.urlopen(launcher_download_url)
    updated_file = response.read()

    # Write the updated file
    with open(launcher_file, "wb") as f:
        time.sleep(1)
        f.write(updated_file)
        print("\nFile Updated!")

def sleep_p5():
    time.sleep(0.5)
def sleep_2():
    time.sleep(2)
def sleep_6():
    time.sleep(6)
#----End Functions----
updater()
#Checking if Evil Wild Eye Games directory exists
if os.path.exists(launcher_directory):
    print("\nThe directory " + groupname + " exists and is located at " + launcher_directory)
else:
    print("\nThe directory " + groupname + " will be created at the root of the drive.")
    os.mkdir(launcher_directory)
sleep_2()
#Checking if Games directory exists
if os.path.exists(games_directory):
    print("\nThe directory Games exists and is located at " + games_directory)
else:
    print("\nThe directory Games will be created inside of the " + groupname + " directory.")
    os.mkdir(games_directory)
sleep_2()
while True:
    user_input_launcher_menu = int(input("\nWelcome to the " + groupname + " Launcher!\nYou can view the library of games or take a look at the launchers settings.\n\n1: Game Library\n2: Launcher Settings\n\nInsert a number: "))
    if user_input_launcher_menu == 1:
        print("\nLoading Library of Games...")
        sleep_p5()
        user_input_library = int(input("\nFrom here you can launch our games and download game assets as needed.\nWhich game do you want to play?\n\n1: " + game_1 + "\n\nInput the number that corresponds with its game here: "))
        if user_input_library == 1:
            print("\nNow starting " + game_1)
            sleep_2()
            #Checking if Dungeon Escape Survival directory exists
            if os.path.exists(game_1_directory):
                print("\nThe directory " + game_1 + " exists and is located at " + game_1_directory)
            else:
                print("\nThe directory " + game_1 + " will be created inside of the " + groupname + " directory.")
                os.mkdir(game_1_directory)
            sleep_2()
            #Checking if Dungeon-Escape-Survival-Alpha.py file exists
            if os.path.exists(game_1_directory_file):
                print("\n" + game_1_file + " exists and is located at " + game_1_directory_file)
            else:
                print("\nThe file " + game_1_file + " will be downloaded from " + game_1_download_url + " and put inside of the " + game_1 + " directory.")
                urllib.request.urlretrieve(game_1_download_url, game_1_directory_file)
            sleep_2()
            #Checking if Sound directory exists
            if os.path.exists(game_1_sound_directory):
                print("\nThe directory Sound exists and is located at " + game_1_sound_directory)
            else:
                print("\nThe directory Sound will be created inside of the " + game_1 + " directory.")
                os.mkdir(game_1_sound_directory)
            sleep_6()
            exec(open(game_1_launch).read())
            break
        else:
            print("\nThat number of input doesn't exist at this time!")
            sleep_2()
    elif user_input_launcher_menu == 2:
        print("\nLoading settings...")
        sleep_p5()
        while True:
            user_settings_input = int(input("\nYou can Refresh Installed game files, check the launcher version, or update the launcher.\n\n1: Check the Launcher Version\n2: Update " + game_1 + " \n3: Update Launcher\n4: Exit Settings\n\nInsert a number: "))
            if user_settings_input == 1:
                print(launcher_version)
                sleep_2()
            elif user_settings_input == 2:
                # Get the updated file
                response = urllib.request.urlopen(game_1_download_url)
                updated_file = response.read()

                # Write the updated file
                with open(game_1_directory_file, "wb") as f:
                    time.sleep(1)
                    f.write(updated_file)
                    print("\nFile Updated!")
            elif user_settings_input == 3:
                updater()
            elif user_settings_input == 4:
                print("\nLeaving settings...")
                break
            else:
                print("\nThat option doesn't exist! Try Again!")
                sleep_2()
    else:
        print("\nThat option doesn't exist!")
        sleep_2()