import os
import pyautogui
from python_imagesearch.imagesearch import imagesearch
import time
import random
import npcs

# Paths
scriptPath = os.path.dirname(os.path.abspath(__file__))
littleImages = npcs.getNpcs()

glitter = os.path.join(scriptPath, r"images\glitter.png")
startAttackButton = os.path.join(scriptPath, r"images\start_attack.png")
cancelAttackButton = os.path.join(scriptPath, r"images\buttons.png")
rewardObtained = os.path.join(scriptPath, r"images\reward.png")
sunkButton = os.path.join(scriptPath, r"images\sunk.png")
repairingButton = os.path.join(scriptPath, r"images\repairing.png")


def bot_loop():
    seek_attempt = 0
    while True:
        sunk_location = imagesearch(sunkButton)
        if sunk_location[0] != -1 and sunk_location[1] != -1:
            print("Sunk detected")
            pyautogui.leftClick(sunk_location[0] + 15 - 1920, sunk_location[1] + 15)

        attack_attempt = 0
        is_attacking = False
        is_npc_finished = False
        time.sleep(1 / 3)
        npc_location = find_npc_location()
        time.sleep(1 / 3)
        glitter_location = find_glitter_location()

        repair_check()

        if seek_attempt > 5:
            seek_attempt = 0
            pyautogui.leftClick(random.randint(45, 1900), random.randint(45, 800))

        if npc_location[0] != -1 and npc_location[1] != -1:
            print("Going to npc : " + str(npc_location))
            pyautogui.leftClick(npc_location[0] + 10 - 1920, npc_location[1] + 10)
            pyautogui.leftClick(npc_location[0] + 50 - 1920, npc_location[1] + 50)
            while is_attacking == False and is_npc_finished == False:
                if attack_attempt > 8:
                    break
                time.sleep(1 / 3)
                buttonLocation = imagesearch(startAttackButton, 0.99)
                print("Attack Button Location : " + str(buttonLocation))
                attack_attempt += 1
                if buttonLocation[0] != -1 and buttonLocation[1] != -1:
                    is_attacking = True
                    pyautogui.press('f')
                    pyautogui.keyUp('f')
                    while is_attacking == True:
                        time.sleep(1 / 3)
                        cancelLocation = imagesearch(cancelAttackButton, 0.90)
                        print("Cancel Button Location : " + str(cancelLocation))
                        if cancelLocation[0] != -1 and cancelLocation[1] != -1:
                            is_attacking = False
                            is_npc_finished = True
        elif glitter_location[0] != -1 and glitter_location[1] != -1:
            print("Going to glitter : " + str(glitter_location))
            is_reward_obtained = False
            pyautogui.leftClick(glitter_location[0] + 10 - 1920, glitter_location[1] + 10)
            reward_attempt = 0
            while is_reward_obtained == False:
                reward_obtained_location = imagesearch(rewardObtained, 5)
                print("Reward Message Location : " + str(reward_obtained_location))
                if reward_obtained_location[0] != -1 and reward_obtained_location[1] != -1:
                    is_reward_obtained = True
                reward_attempt += 1
                if reward_attempt > 10:
                    break
                time.sleep(1 / 3)

        seek_attempt += 1


def find_npc_location():
    for i in range(len(littleImages)):
        location = imagesearch(littleImages[i])
        if location[0] != -1 and location[1] != -1:
            return location
    return [-1, -1]


def repair_check():
    repairingButtonLocation = imagesearch(repairingButton)
    print("Repair : " + str(repairingButtonLocation))
    if repairingButtonLocation[0] == -1 and repairingButtonLocation[1] == -1:
        pyautogui.press('q')
        pyautogui.keyUp('q')
        print("Repairing")

def find_glitter_location():
    return imagesearch(glitter)


if __name__ == "__main__":
    bot_loop()
