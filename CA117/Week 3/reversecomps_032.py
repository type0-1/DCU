import sys

triped = [word.strip() for word in sys.stdin]
lowered = [word.lower() for word in striped]
def binsearch(query, sorted_list):

   low = 0
   high = len(sorted_list) - 1
   
   while low <= high:
           mid = (low + high) // 2
           if sorted_list[mid] < query:             
              low = mid + 1
            elif sorted_list[mid] > query:
               high = mid - 1
            else:
               return True

    return False
result = [w for w in striped if len(w) >= 5 and binsearch(w[::-1].lower(), lowered)]
print(result)
