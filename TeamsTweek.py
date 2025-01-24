from time import sleep
from keyboard import press_and_release




def AlwaysActive():
    while True:         
        press_and_release("F18")
        press_and_release("F19")

        sleep(60)


        
if __name__ == "__main__":
    AlwaysActive()



