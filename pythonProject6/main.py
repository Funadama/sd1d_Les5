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
coolPrint()
ABC(3)