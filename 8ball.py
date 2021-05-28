import sys
import random
from playsound import playsound

ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (type 'exit' to quit)\n ")
    answers = random.randint(1, 20)

    if question == "exit":
        sys.exit()

    elif answers == 1:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nIt is certain\n")

    elif answers == 2:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nAs I see it, yes.\n")

    elif answers == 3:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nReply hazy, try again.\n")

    elif answers == 4:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nDon't count on it.\n")

    elif answers == 5:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nIt is decidedly so.\n")

    elif answers == 6:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nMost likely.\n")

    elif answers == 7:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nAsk again later.\n")

    elif answers == 8:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nMy reply is no.\n")

    elif answers == 9:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nWithout a doubt\n")

    elif answers == 10:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nOutlook good.\n")

    elif answers == 11:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nBetter not tell you now.\n")

    elif answers == 12:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nMy sources say no\n")

    elif answers == 13:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nYes definitely.\n")

    elif answers == 14:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nYes.\n")

    elif answers == 15:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nCannot predict now.\n")

    elif answers == 16:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nOutlook not so good.\n")

    elif answers == 17:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nYou may rely on it.\n")

    elif answers == 18:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nSigns point to yes.\n")

    elif answers == 19:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nPlease go away.\n")

    elif answers == 20:
        print("\nShaking...\n")
        playsound('D:/python projects/8ball/sound.mp3')
        print("\nVery doubtful.\n")
