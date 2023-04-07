import sys

class Magic(object):
    
    def __init__(self, magic, numbers=None):
        self.magic = magic
        self.numbers = numbers
        
        if self.numbers is None:
            self.numbers = []
    
    def find_magic(self):
        while self.magic:
            self.magic -= 1
            self.numbers.append("3") if self.magic % 2 == 0 else self.numbers.append("9")
            self.magic //= 2
        return self.numbers
    
    def __str__(self):
        self.numbers = Magic(self.magic).find_magic()
        return "".join(self.numbers)[::-1]
            
def main():
    number = int(sys.stdin.readline().strip())
    instance = Magic(number)
    print(instance)

if __name__ == "__main__":
    main()
