import random



def reverse_array(array):
    reversed_array=[]
    for index in range(len(array)):
        reversed_array.append(array[len(array)-1-index])

    return reversed_array

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