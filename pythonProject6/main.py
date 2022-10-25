def ABC(Amount):
    listOfABC = ["a", "b", "c", "d"]
    listOfABC = listOfABC[:Amount]
    answer = input(":").lower()
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


coolPrint("[Start]\nThis is the story of a man named Stanley.\nStanley worked for a company in a big building where\nhe was employee number 427. Employee Number 427s\njob was simple: he sat at his desk in room 427, and he pushed\nbuttons on a keyboard.Orders came to him through a monitor\non his desk, telling him what buttons to push,\nhow long to push them, and in what order.","")
input(":")
coolPrint("This is what Employee 427 did every day of every month and every year, and\nalthough others might have considered it soul-rending, Stanley relished every\nmoment that the orders came in, as though he had been made exactly for this job.\n\nAnd Stanley was happy.\n\nAnd then one day, something very peculiar happened.\nSomething that would forever change Stanley. Something he would never quite forget.","")
input(":")
coolPrint("He had been at his desk for nearly an hour when he realized that not one\nsingle order had arrived on the monitor for him to follow. No-one had\nshowed up to give him instructions, call a meeting, or even say Hi.\nNever in all his years at the company had this happened - this complete \nisolation. Something was very clearly wrong. Shocked, frozen solid,\nStanley found himself unable to move for the longest time. But as he\ncame to his wits and regained his senses, he got up from his desk and\nstepped out of his office.", "Step out of your office\nClose your office door")
answer = ABC(4)
if answer == 0:
    print("A")
else:
    coolPrint("Stanley stands in the door way, taking one last look at the grand work space in front of him, and closes his \noffice door. Stanley simply couldn't handle the pressure. What if he had to make a decision? What if a crucial\noutcome fell under his responsibility? He had never been trained for that! No, this couldn't go any way except\nbadly. The thing to do now was to wait. Nothing will hurt me, Stanley thought, nothing will break me. In here\nI can be happy forever. I will be happy. Stanley waited. Hours passed. Then days. Had years gone by? He no\nlonger had the ability to tell. But one thing he was sure of was that some day, the answers would come.\nEventually, they would arrive. Very soon now, this will end. He will be spoken to. He will be told what to do.\nNow it's just a little bit closer. Here it comes...", "")
    input("ending 1 ")