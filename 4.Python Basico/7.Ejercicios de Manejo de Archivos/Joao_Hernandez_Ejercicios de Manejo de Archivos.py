
#Excecise 1
#Create a program that reads names from a list of songs on a file and the save them on a different file alphabetically 

def excercise_one():

    try:



        def open_and_read(path):
            with open(path) as file:
                new_song_list = []
                

                for line in file.readlines():
                    new_song_list.append(line)
                    new_song_list.sort()
                    print(f"Cancione: {line}")
                
                print(f"{new_song_list}")

            with open("C:\\Users\\jhmba\\Downloads\\Python\\Newfile.txt") as file:
                 for line in new_song_list:
                      with open("C:\\Users\\jhmba\\Downloads\\Python\\Newfile.txt", "a") as file:
                           file.writelines(line)
                
        open_and_read("C:\\Users\\jhmba\\Downloads\\Python\\Canciones.txt")

    except ValueError as error:
                print(f"Error [ValueError]: You tried to enter an incorrect value")

excercise_one()       