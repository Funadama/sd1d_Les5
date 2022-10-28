Torch = False
def ABC(Amount):
    listOfABC = ["a", "b", "c", "d"]
    listOfABC = listOfABC[:Amount]
    answer = input(">").lower()
    if answer in listOfABC:
        return listOfABC.index(answer)
    else:
        print(" It has to be "+ str(listOfABC) + "!")
        return ABC(Amount)

def coolPrint(Messages, BehindTEXTS):
    Line = ""
    TopLine = ""
    Count = 0
    longest = 0
    NextBehind = 1
    listOfABC = ["A", "B", "C", "D"]
    BehindTEXTList = BehindTEXTS.split("\n")
    alleRegels = Messages.split("\n")
    for Message in alleRegels:
        if len(Message) > longest:
            longest = len(Message)
    while longest > Count:
        TopLine += "■"
        Count += 1
    if "" == BehindTEXTList[0]:
        print("▮■" + TopLine + "■▮")
    else:
        print("▮■" + TopLine + "■▮ A= " + BehindTEXTList[0])
    Turn = 0
    for Message in alleRegels:
        if NextBehind < len(BehindTEXTList):
            BehindTEXT = " " + listOfABC[NextBehind] + "= " + BehindTEXTList[NextBehind]
            NextBehind += 1
        else:
            BehindTEXT = ""
        line = alleRegels[Turn]
        while len(line) < longest:
            line += " "
        print("▮ " + line + " ▮" + BehindTEXT)
        Turn += 1
    if NextBehind < len(BehindTEXTList):
        BehindTEXT = " " + listOfABC[NextBehind] + "= " + BehindTEXTList[NextBehind]
    else:
        BehindTEXT = ""
    print("▮■" + TopLine + "■▮" + BehindTEXT)


def Splitway():
    Torch = False
    coolPrint(
        "Stanley walked through the hallway into the meeting room. Once again, he was greeted\nwith an empty room, filled with a large table with several chairs up against it. Business \ncharts riddled with statistics littered the walls. Stanley walk forward\nComing to two opposite staircases,\nStanley walked upstairs to his boss's office.",
        "Walk upstairs\nWalk downstairs")
    answer = ABC(2)
    if answer == 0:
        coolPrint(
            "Stepping into his manager's unnecessarily large office, Stanley was once again \nstunned to find not an indication of any human life. Shocked, unraveled, Stanley \nwondered in disbelief who orchestrated this, what dark secrets were being held from him!\n\nWhat he could not have known was that the keypad behind the boss's desk guarded the \nterrible truth that his boss had been keeping from him, and so the boss had assigned \nit an extra secret pin number:\n2 - 8 - 4 - 5.",
            "Enter 2-8-4-5 into the keypad")
        input(">")
        coolPrint(
            "Yet amazingly, buy pushing random buttons into the keypad, \nStanley discovered the correct code by sheer luck. Bravo, \nStanley. The panel on the wall opened up and Stanley walked \nin and saw a large button with a light bulb insignia stuck \nout of a control deck. He pushed the button, and lights flicked \non to reveal an enormous packed with television screens. What \nhorrible secret does this place hold? Stanley thought to himself, \nbut did he have the strength to find out?",
            "")
        input(">")
        coolPrint(
            "A catwalk rose out of the ground and connected the current platform \nwith another one in the distance. Stanley walked onto the catwalk \nthat lead to a monstrously large screen that read 'Mind Controls \nIdle, Awaiting Input...'",
            "Walk up to the screen")
        input(">")
        coolPrint(
            "Stanley walked up to the large screen and came \nto a control deck with two buttons: \n'OFF' and 'ON'. Knowing what was best \nto do, he pushed the 'OFF' button to \nend this madness once and for all.",
            "Push 'OFF'\nPush 'ON'")
        answer = ABC(2)
        if answer == 0:
            coolPrint(
                "He had won!\n\nHe had defeated the machine!\nUnshackled himself from someone else's command! \nAnd he went to the nederland as a (Newkomer)\nBecause of his trama\nand he loved it in the nederlands (:",
                "")
            input("ending 5")
        else:
            coolPrint(
                "Stanley pushed the 'OFF' button and the room...\n...Wait, Stanley, you just activated the controls. didn't you? After they \nkept you enslaved for all these years you go and try to take control of this \nmachine for yourself, Is that what you wanted? Control? This isn't how the story \ngoes, you were supposed to get to this ontrol deck, turn the controls OFF, and leave. \nIf you're going to throw my story off track, you're going to have to do much better \nthan that, for example; and I think you'll find this pertinent:\nWork ending",
                "")
            input("ending 2")
    else:
        coolPrint(
            "But Stanley just couldn't do it. He considered the possibility \nof facing his boss, admitting he had left his post during work \nhours. He might be fired for that. And in such a competitive \neconomy, why had he taken that risk? All because he had \nbelieved everyone had vanished? His boss would think he was crazy.\n\nAnd then something occurred to Stanley.",
            "")
        input(">")
        coolPrint(
            "Maybe, He thought to himself. Maybe, I am crazy. All of my \nco-workers blinking mysteriously out of existence in a single \nmoment, for no reason at all? None of it made any logical sense. \n\nCrazy ending",
            "")


coolPrint("[Start]\nThis is the story of a man named Stanley.\nStanley worked for a company in a big building where\nhe was employee number 427. Employee Number 427s\njob was simple: he sat at his desk in room 427, and he pushed\nbuttons on a keyboard.Orders came to him through a monitor\non his desk, telling him what buttons to push,\nhow long to push them, and in what order.","")
input(">")
coolPrint("This is what Employee 427 did every day of every month and every year, and\nalthough others might have considered it soul-rending, Stanley relished every\nmoment that the orders came in, as though he had been made exactly for this job.\n\nAnd Stanley was unhappy tho.\n\nAnd then one day, something very peculiar happened.\nSomething that would forever change Stanley. Something he would never quite forget.","")
input(">")
coolPrint("He had been at his desk for nearly an hour when he realized that not one\nsingle order had arrived on the monitor for him to follow. No-one had\nshowed up to give him instructions, call a meeting, or even say Hi.\nNever in all his years at the company had this happened - this complete \nisolation. Something was very clearly wrong. Shocked, frozen solid,\nStanley found himself unable to move for the longest time. But as he\ncame to his wits and regained his senses, he got up from his desk and\nstepped out of his office.", "Step out of your office\nClose your office door")

answer = ABC(2)
if answer == 0:
    coolPrint("As he stepped out of his cubicle, Stanley was dumbfounded to find his day-to-day office,\nusually packed with his busy co-workers, was completely empty. No one was clacking attheir\nkeyboards, staring at screens, drinking their mugs of coffee, nothing.\n\nAs Stanley walked into the hallway, he came to an empty room with a set of two \nopen doors: One on his left, and one on his right. The way to the meeting room \nwas the left door, so without hesitation, he entered that one.","enter the left door\nEnter the right door")

    answer = ABC(2)
    if answer == 0:
        Splitway()
    else:
        coolPrint("This was not the correct way to the meeting room, and Stanley knew it perfectly \nwell. This of course was the way to the employee lounge, so perhaps Stanley \nwanted to stop by it first, just to admire it.\nBut eager to get back to business, Stanley left the employee lounge and came \nto a hallway with a door on his left and a door in front of him. Seeing as \nthe meeting room was through the left door, he entered that one.", "Enter the door on your left\nEnter the door in front of you")
        answer = ABC(2)
        if answer == 0:
            Splitway()
        else:
            coolPrint("Stanley was so bad at following directions, it's incredible he wasn't fired years ago. \nHe came to an enormous room filled will cargo crates, \ntrucks and forklifts. Yet, that was all on the deep floor \nof the factory, separating two rooms. Oh look, an elevator \nplatform. Why don't you jump on that, or try your \nluck at falling down the deep pit below.", "Fall down the pit\nJump on the elevator platform")
            answer = ABC(2)
            if answer == 0:
                coolPrint("*SPLAT*\n\nBut in his eagerness to prove that he is in control \nof the Story and no one gets to tell him what to do, \nStanley lept from the platform, and plunged to his death.\nGood job, Stanley. Everyone thinks you are very powerful.", "")
                input("ending 4 ")
            else:
                coolPrint("The elevator platform whirred into motion as it gradually moved to the other room.\nLook, Stanley, I think perhaps we've gotten off on the wrong foot here. I'm not \nyour enemy, really I'm not! I understand that investing your trust in someone else \ncan be difficult, but the fact is the Story has been about nothing but you, all this time!\nThere's someone you've been neglecting, Stanley; someone you've forgotten about. \nPlease, stop trying to make every decision by yourself. Now, I'm not asking for me...\n...I'm asking for her. The elevator platform came to a halt at the other room.", "Walk into the room\nJump off the platform\nPickup torche (:")
                answer = ABC(3)
                if answer == 0:
                    coolPrint("The door shut behind Stanley.\nStanley did not have a torch so he hit his head.\nThis is a very sad story about the death of a man named Stanley.\n\nGood morning Employee 427. ", "")
                    input("ending 4 ")
                elif answer == 2:
                    coolPrint("Stanley walk for hours with his torch in hand.\nStanley saw a light at the end.\n Good morning Employee 427. And he went to the nederland as a (Newkomer)\nBecause of his trama\nand he loved it in the nederlands (:", "")
                    input("ending 3 ")
                else:
                    coolPrint("*SPLAT*\n\nBut in his eagerness to prove that he is in control \nof the Story and no one gets to tell him what to do, \nStanley lept from the platform, and plunged to his death.\nGood job, Stanley. Everyone thinks you are very powerful.", "")
                    input("ending 4 ")

else:
    coolPrint("Stanley stands in the door way, taking one last look at the grand work space in front of him, and closes his \noffice door. Stanley simply couldn't handle the pressure. What if he had to make a decision? What if a crucial\noutcome fell under his responsibility? He had never been trained for that! No, this couldn't go any way except\nbadly. The thing to do now was to wait. Nothing will hurt me, Stanley thought, nothing will break me. In here\nI can be happy forever. I will be happy. Stanley waited. Hours passed. Then days. Had years gone by? He no\nlonger had the ability to tell. But one thing he was sure of was that some day, the answers would come.\nEventually, they would arrive. Very soon now, this will end. He will be spoken to. He will be told what to do.\nNow it's just a little bit closer. Here it comes...", "")
    input("ending 1 ")


