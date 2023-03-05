import sys

def lower(security, sums=0):
    for char in security:
        if char.islower():
            sums += 1
            break
    return sums

def upper(security, upc=0):
    sums = lower(security)
    for char in security:
        if char.isupper():
            upc += 1
            break
    sums += upc
    return sums

def numbers(security, nc=0):
    sums = upper(security)
    for char in security:
        if char.isnumeric():
            nc += 1
            break
    sums += nc
    return sums
    
def special(security, spc=0):
    sums = numbers(security)
    for char in security:
        if not char.isalnum():
            spc += 1
            break
    sums += spc
    return sums
    
def main():
    for data in sys.stdin:
        print(special(data.strip()))
        
if __name__ == "__main__":
    main()