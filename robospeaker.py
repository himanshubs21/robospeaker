# this program is made to speak the input provided by user
# currently it supports only macos
# robospeaker
import os
if __name__ == '__main__':
    print('Welcome to RoboSpeaker 1.1. Created by Himanshu!')
    while True:
        order = input("Enter what do you want me to speak! ")
        if order == 'q':
            os.system("say ' bye bye friend!!'")
            break
        command = f'say {order}'
        os.system(command)
