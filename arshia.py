import simpleaudio as sa
import time
wave_obj = sa.WaveObject.from_wave_file("war.wav")
play_obj = wave_obj.play()

time.sleep(5)

title = "INCONCLUSIVE"
print(f"You have arrived to {title}. Type carefully to decide your fate. Capital letters do not exist here. You have"+
      " forgotten your identity, all but your name.")

import cv2
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    img_name = "this_is_you.jpg"
    cv2.imwrite(img_name, frame)
    print("{}".format(img_name))
    break
cam.release()
cv2.destroyAllWindows()
from PIL import Image
block = Image.open("this_is_you.jpg")
newsize = (1000, 600) 
dub_block = block.resize(newsize)
dub_block.show()
name_choice = input("Recall your name player.\n")

print(f"You have been found {name_choice}. You start in a dark room. You have no idea how you have arrived but"+
      " you do know how you can leave. 2 doors await you. The first is blood red, and the second, pale white.")
door_choice = input("Which door do you wish to choose, red or white? \n")

if door_choice == "red":
    print("So you go through the red door. You enter a tower room with the owner unknown. The walls the same red color as the door. Footsteps"+
          " near from the outside of the door. You don't know if you are welcome here. Should you hide"+
          " under the bed or should you let them find you?")
    tower_choice = input("Do you hide or remain? \n")
    
    if tower_choice == "hide":
        print("You hide. The void under the bed is limited but you must hide. A queen enters the room with a crown taller"+
              " than heaven. Allies you weren't meant to be. She sets a half full glass of water on the floor."+
              " You can drink to avoid dehydration or spill for it is questionable?")
        drink_choice = input("drink or spill? \n")

        if drink_choice == "drink":
            print("You should have never trusted. Poison is hard to tell from water after all. Liquid take over"+
                  " and you are no longer. DEAD END")
    if tower_choice == "remain":
        print("So you take your stance. A queen enters the room with a crown taller than heaven. And the next moment you are threatened."+
              " Allow the queen to use your hidden power for herself or jump through the height of the window.")
        jump_choice = input("Should you jump or allow? \n")
        if jump_choice == "jump":
            print("You have met your end. Survival has challenged you here. DEAD END")

if door_choice == "white":

    from PIL import Image
    siren = Image.open("siren.jpg")
    newsize = (2000, 1200) 
    dub_siren = siren.resize(newsize)
    dub_siren.show()
    
    print("So you choose the white door. Trees surround you. Your location is assumed. The moon's light shines a pale white, like the color of"+
          " the door. The sound of a bird's last call repeats over and over. You hear the distinct wail of"+
          " sirens. Do you stay for them to find you or do you escape human nature?")
    siren_choice = input("Do you stay or leave? \n")

    if siren_choice == "stay":
        print("No questioning is allowed. They might be FBI or different generation peacekeepers. It doesn't"+
              " matter now. They have caught you illegaly entering in the darklands. They underestimate your"+
              " power and they accidently give you a moment to run. Will you take it or tell them your name?")
        run_choice = input("Will you run or speak? \n")

        if run_choice == "run":
            print("Run as fast as you can. They STEEL police don't make the same mistake twice. Hide within"+
                  " the trees for if you are caught, you will never see the sky.")

        if run_choice == "speak":
            print("They cower beneath you. They fear your name")

    if siren_choice == "leave":
        print("You walk farther into the woods. The sirens quiet as you go deeper. Nothing is recognizable."+
              " Then suddenly, a rabbit leaves its hiding to face you. It says to follow. Should you?")
        follow_choice = input("follow or stray? \n")
