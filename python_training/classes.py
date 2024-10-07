
from enum import Enum
import sys
import random
from typing import List


class Cutting(Enum):
    HEAVY_SABAB="//"
    LIGHT_SABAB="/0"
    CLOSE_WATAD="//0"
    SAPARATED_WATAD="/0/"
    

class Word:
    
    def __init__(self, text:str, prosodicWriting:str, cuttings:list):
        self.text = f"{text} "
        self.prosodicWriting = f"{prosodicWriting} "
        self.cuttings = cuttings

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
        

    def printCuttings(self):
        for word in self.firstHalf.words:
            printCuttings(word.cuttings)
        print('\t')

        for word in self.secondHalf.words:
            printCuttings(word.cuttings)
        print('\n')

def printText(string:str):
    toBePrinted=string.encode("utf-8")
    sys.stdout.buffer.write(toBePrinted)

word1= Word("ثم","ثما",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])
word2= Word("تولى","تولل",[Cutting.CLOSE_WATAD,Cutting.LIGHT_SABAB])
word3= Word("أمرهم","أمرهم",[Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD])
word4= Word("معاوية","موعاوية",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD])

word5= Word("فعاش","فاعاش",[Cutting.LIGHT_SABAB,Cutting.SAPARATED_WATAD])
word6= Word("عشرًا","عشرن",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])
word7= Word("بعد","بعد",[Cutting.SAPARATED_WATAD])
word8= Word("عشرٍ","عشرن",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])
word9= Word("خالية","خالية",[Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD])


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


word10= Word("حتى","حتتى",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])
word11= Word("إذا","إذا",[Cutting.CLOSE_WATAD])
word12= Word("أوفاهم","أوفاهمو",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD])
word13= Word("عشرينا","عشرينا",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])

word14= Word("مات","ماتا",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])
word15= Word("من","منا",[Cutting.CLOSE_WATAD])
word16= Word("التاريخ","تاريخ",[Cutting.LIGHT_SABAB,Cutting.SAPARATED_WATAD])
word17= Word("في","في",[Cutting.LIGHT_SABAB])
word18= Word("ستينا","ستتينا",[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB])

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

rajazweight1=[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD,
              Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD,
              Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD]

rajazweight2=[Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD,
              Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.CLOSE_WATAD,
              Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB,Cutting.LIGHT_SABAB]

def printCuttings(list:list):
    for item in list:
        printText(item.value)

# verse1.printVerse()
# verse1.printProsodicWriting()
# verse1.printCuttings()
# printCuttings(rajazweight1)

# print("\n")

# verse2.printVerse()
# verse2.printProsodicWriting()
# verse2.printCuttings()
# printCuttings(rajazweight2)

def print_half_verse(poem:list):
    for word in poem:
        printText(word.text)
    print("\n")
    
def printPoemsProsodicWriting(poem:list):
    for word in poem:
        printText(word.prosodicWriting)
    print("\n")
    
def remove_list_from_list(list:list,to_be_removed_list):
    
    for to_be_removed_list_item in to_be_removed_list:
        if isInList(list,to_be_removed_list_item):
            list.remove(to_be_removed_list_item)
            
    return list

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


def reverse(string):
    reversedString=""
    for index in range(len(string)):
        reversedString+=string[len(string)-1-index]
             
    return reversedString


def soFarSimilar(rajaz:str, cutting:str):
    if len(cutting)>len(rajaz):
        return False
    
    for index in range(len(cutting)): 
        if cutting[index] != rajaz[index]:
            return False
    return True

def cuttings_to_string(list:list):
    string=""
    for item in list:
        string=string+item.value
    return string

def does_rhyme(second_half_verse:HalfVerse, rhyme_letter:str):
    second_half_verse_length=len(second_half_verse.words)
    last_word:str= second_half_verse.words[second_half_verse_length-1].prosodicWriting
    last_word_len=len(last_word)
    
    printText(last_word)
    print("\n")
    printText(last_word_len.__str__())
    print("\n")
    printText(last_word.find(rhyme_letter).__str__())
    print("\n")
    
    # if last_words_rhyme_letter == rhyme_letter:
    if last_word.find(rhyme_letter)==last_word_len-2:
        return True
    else:
        return False

words = [word1,word2,word3,word4,
         word5,word6,word7,word8,word9,
         word10,word11,word12,word13,
         word14,word15,word16,word17,word18]

def generate_half_verse_recursive(current_half_verse:list, cuttings:list, wordsList:list, results:list)->list|None:

    if cuttings_to_string(cuttings) == cuttings_to_string(rajazweight1) or cuttings_to_string(cuttings) == cuttings_to_string(rajazweight2):
        print('\n')
        print_half_verse(current_half_verse)
        printCuttings(cuttings)
        print('\n')
        # results.append(current_half_verse)
        return
        
    if len(cuttings) >= len(rajazweight1):
        return
        
    
    for index in range(len(wordsList)):
        word= wordsList[index]
        
        current_half_verse.append(word)
        cuttings=cuttings+word.cuttings

        soFarSoGood = soFarSimilar(cuttings_to_string(rajazweight1),cuttings_to_string(cuttings)) or soFarSimilar(cuttings_to_string(rajazweight1),cuttings_to_string(cuttings))
        
        if soFarSoGood:
            generate_half_verse_recursive(current_half_verse, cuttings, wordsList,results)
        
        # backtracking
        # if len(current_half_verse)>0:
        word:Word = current_half_verse.pop()
        cuttings= remove_list_from_list(cuttings,word.cuttings)
        
    return 


    
def generate_half_verse(wordsList):
    poem=[]
    cuttings:list=[]
    triedWords=[]
    
    while True:
        randomWord = random.choice(wordsList)
        
        if not isInList(triedWords,randomWord):
            poem.append(randomWord)
            cuttings=cuttings+randomWord.cuttings
            triedWords.append(randomWord)

        soFarSoGood = not soFarSimilar(cuttings_to_string(rajazweight1),cuttings_to_string(cuttings)) or not soFarSimilar(cuttings_to_string(rajazweight1),cuttings_to_string(cuttings))
        
        if not soFarSoGood and isInList(triedWords,randomWord):
            triedWords=[]

        # backtracking
        if soFarSoGood and len(poem)>0:
            word = poem.pop()
            cuttings= remove_list_from_list(cuttings,word.cuttings)
        
        # printText(randomWord.text)
        # print("\n")
        # printCuttings(randomWord.cuttings)
        # print("\nis in list: "+isInList(triedWords,randomWord).__str__())
        # print("\nTried List:\n")
        # print_half_verse(triedWords)
        # print("Current poem:")
        # print_half_verse(poem)
        # printCuttings(cuttings)
        # print("\n")
        
        if cuttings_to_string(cuttings) == cuttings_to_string(rajazweight1) or cuttings_to_string(cuttings) == cuttings_to_string(rajazweight2):
            break
        
        if len(cuttings) >= len(rajazweight1):
            break
        
    # print("This is our Poem:")
    # print_half_verse(poem)
    # printPoemsProsodicWriting(poem)
    # printCuttings(cuttings)
    
    return HalfVerse(poem)

def generate_verse(rhyme_letter:str,words):
    first_half = generate_half_verse(words)
    
    does_rhyme_flag:bool = False
    print(does_rhyme_flag)

    while not does_rhyme_flag:
        second_half = generate_half_verse(words)
        does_rhyme_flag = does_rhyme(second_half,rhyme_letter)
        print(does_rhyme_flag)

    print_half_verse(second_half.words)
    
    return Verse(first_half,second_half)
    
def generate_poem(verses_count,rhyme_letter:str, words):
    verses = []
    counter = verses_count
    while counter>0 :
        verses.append(generate_verse(rhyme_letter,words))
        counter-=1

    return verses

def print_poem(poem:list):
    
    for verse in poem:
        verse.printVerse()
        # verse.printProsodicWriting()
        # verse.printCuttings()
    

poem =  generate_poem(3,"ا",words)
print_poem(poem)
