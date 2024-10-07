from enum import Enum


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

ok_man ="0//0/0/"
ok ="0/0/"
ok2="0/0"
print((ok+ok2))

print(reverseString(ok_man))
print(reverseString(ok))
print(reverseString(ok2))
print(reverseString(ok)+reverseString(ok2))

print(soFarSimilar(ok_man,reverseString(ok)+reverseString(ok2)))


from classes import Cutting
    
    
print(Cutting.HEAVY_SABAB.value)
print(Cutting.HEAVY_SABAB.name)