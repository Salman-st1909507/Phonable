from abc import ABC, abstractmethod


class ABCD(ABC):
    
    def __init__(self) -> None:
        super().__init__()
        self.x = 'x'
        self.y = 'y'
    def method_a(self):
        print(self.x)
        print(self.y)

class ABCDE(ABCD):
    def __init__(self) -> None:
        super().__init__()
    # def method_a(self):
        
    #     print(self.x)

ABCDE().method_a()