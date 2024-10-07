from enum import Enum
import sys
import random


class Cutting(Enum):
    HEAVY_SABAB=0,
    LIGHT_SABAB=1,
    CLOSE_WATAD=2,
    SAPARATED_WATAD=3
    

class Word:
    
    def __init__(self, text:str, prosodicWriting:str, cutting:str):
        self.text = f"{text} "
        self.prosodicWriting = f"{prosodicWriting} "
        self.cutting = f"{cutting}"

class HalfVerse:
    
    def __init__(self, words:list):
        self.words = words

class Verse:
    
    def __init__(self, firstHalf:HalfVerse, secondHalf:HalfVerse):
        self.firstHalf = firstHalf
        self.secondHalf = secondHalf
        
    def printVerse(self):
        for word in self.firstHalf.words:
            printText(word.text)
        print('\t')

        for word in self.secondHalf.words:
            printText(word.text)
        print('\n')
        
    def printProsodicWriting(self):
        for word in self.firstHalf.words:
            printText(word.prosodicWriting)
        print('\t')

        for word in self.secondHalf.words:
            printText(word.prosodicWriting)
        print('\n')
        

    def printCutting(self):
        for word in reversed(self.firstHalf.words):
            printText(word.cutting)
        print('\t')

        for word in reversed(self.secondHalf.words):
            printText(word.cutting)
        print('\n')

def printText(string:str):
    toBePrinted=string.encode("utf-8")
    sys.stdout.buffer.write(toBePrinted)


word1= Word("ثم","ثما","0/0/")
word2= Word("تولى","تولل","0/0//")
word3= Word("أمرهم","أمرهم","0//0/")
word4= Word("معاوية","موعاوية","0//0/0/")

word5= Word("فعاش","فاعاش","/0/0/")
word6= Word("عشرًا","عشرن","0/0/")
word7= Word("بعد","بعد","/0/")
word8= Word("عشرٍ","عشرن","0/0/")
word9= Word("خالية","خالية","0//0/")


firstHalf1=HalfVerse([
    word1,
    word2,
    word3,
    word4
    ])

secondHalf1=HalfVerse([
    word5,
    word6,
    word7,
    word8,
    word9
    ])

verse1= Verse(firstHalf1,secondHalf1)


word10= Word("حتى","حتتى","0/0/")
word11= Word("إذا","إذا","0//")
word12= Word("أوفاهم","أوفاهمو","0//0/0/")
word13= Word("عشرينا","عشرينا","0/0/0/")

word14= Word("مات","ماتا","0/0/")
word15= Word("من","من","//")
word16= Word("التاريخ","تتاريخ","/0/0/0")
word17= Word("في","في","0/")
word18= Word("ستينا","ستتينا","0/0/0/")

firstHalf2=HalfVerse([
    word10,
    word11,
    word12,
    word13
    ])

secondHalf2=HalfVerse([
    word14,
    word15,
    word16,
    word17,
    word18
    ])

verse2= Verse(firstHalf2,secondHalf2)

    
verse1.printVerse()
verse1.printProsodicWriting()
verse1.printCutting()
print("0//0/0/0//0/0/0//0/0/")

print("\n")
verse2.printVerse()
verse2.printProsodicWriting()
verse2.printCutting()
print("0/0/0/0//0/0/0//0/0/")




def printPoem(poem:list):
    for word in poem:
        printText(word.text)
    print("\n")
    
def printPoemCutting(poem:list):
    for word in poem:
        printText(word.cutting)
    print("\n")

def isInList(list:list, object)->bool:
    for item in list:
        if item==object:
            return True
        
    return False

def shuffle(list)->list:
    shuffledList=[]
    
    while True:
        randomWord=random.choice(list)
         
        if not isInList(shuffledList,randomWord):
            shuffledList.append(randomWord)
            
        if len(shuffledList) >= len(list):
            break

    return shuffledList 


def reverseString(string:str):
    reversedString=""
    for index in range(len(string)):
        reversedString+=string[len(string)-1-index]
             
    return reversedString


def soFarSimilar(rajaz:str, cutting:str):
    reversedRajaz=reverseString(rajaz)
    reversedCutting=(cutting)
    
    for index in range(len(cutting)): 
        if reversedCutting[index] != reversedRajaz[index]:
            return False
    return True

words = [word1,word2,word3,word4,
         word5,word6,word7,word8,word9,
         word10,word11,word12,word13,
         word14,word15,word16,word17,word18]

rajazweight1="0//0/0/0//0/0/0//0/0/"
rajazweight2="0/0/0/0//0/0/0//0/0/"
      

def generatePoem(list:list, cutting:str, wordsList:list):
    
    printPoem(list)
    print(cutting+'\n'+'\n')
    
    if cutting == rajazweight1 or cutting == rajazweight2:
        print("This is our Poem:")
        printPoem(list)
        print(cutting+'\n')
        
        return 
    
    if len(cutting) >= len(rajazweight1):
        return
    
    for index in range(len(wordsList)):
        word= wordsList[index]
        
        list.append(word)
        cutting += word.cutting
        
        if soFarSimilar(rajazweight1,cutting) or soFarSimilar(rajazweight2,cutting) :
            generatePoem(list, cutting, wordsList)
        
        list.pop()
        cutting= cutting.removesuffix(word.cutting)
        
    return

def generate(wordsList):
    poem=[]
    cutting:str=""
    counter=0
    triedWords=[]
    
    # /0/0//0 /0/0//0 /0/0//0
    while True:
        soFarSoGood = not soFarSimilar(rajazweight1,cutting) or not soFarSimilar(rajazweight2,cutting)
        randomWord = random.choice(wordsList)
        randomWord.cutting=reverseString(randomWord.cutting)
        
        printText(randomWord.text)
        print("\n")
        printText(randomWord.cutting)
        print("\nis in list: "+isInList(triedWords,randomWord).__str__())
        print("\nTried List:\n")
        printPoem(triedWords)
        # print("\n")
        # print("\n")
        print("Current poem:")
        printPoem(poem)
        print((cutting))
        print("\n")
        
        if not isInList(triedWords,randomWord):
            poem.append(randomWord)
            cutting += (randomWord.cutting)
            triedWords.append(randomWord)

        if not soFarSoGood and isInList(triedWords,randomWord):
            triedWords=[]

        if soFarSoGood and len(poem)>0:
            word = poem.pop()
            cutting= cutting.removesuffix((word.cutting))
            
        
        if cutting == rajazweight1 or cutting == rajazweight2:
            break
        
        if len(cutting) >= len(rajazweight1):
            break
        
        # if counter>=10 and len(poem)>0:
        #     word = poem.pop()
        #     cutting = cutting.removesuffix(word.cutting)
        #     counter=0
            
        # counter+=1
        
    print("This is our Poem:")
    printPoem(poem)



shuffledWords= shuffle(words)
printPoem(shuffledWords)

generate(shuffledWords)
# generatePoem([],"", shuffledWords)

