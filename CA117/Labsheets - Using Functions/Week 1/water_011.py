import sys

def water(available, capacity, count=0):
    for litre in capacity:
        if available - int(litre) >= 0:
            available -= int(litre)
            count += 1
        else:
            return count
    return count

def main():
    litresAvailable = int(sys.stdin.readline())
    litreCapacity = sys.stdin.readline().split()
    print(water(litresAvailable, litreCapacity))

if __name__ == "__main__":
    main()