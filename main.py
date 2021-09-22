# An array which satisfy a condition a[n] > a[n-1], will be a sorted array in ascending order


a = [1, 2, 3, 4, 5, 7]


# The number to be inserted
P = 8

# Function to find the index of P
def find_index(a, P):
   #if array 'a' is empty with no elements 
   if not a:       
      return 0

   return search_item(a, P, -1, len(a))  

   # a      => Array to where 'P' is to be inserted
   # P      => The number to be inserted into array 'a'
   # -1     => Starting index of array 'a'
   # len(a) => Last index of array 'a'


def search_item(a, P, start, end):

   # Find the middle element of array 'a'
   mid = int((start + end) / 2)

   # if P not found, index of P must be in the following index next to starting index
   if start == end - 1 and P != a[start]:
      return start + 1
 
   if P == a[mid]:
      return mid

   if P < a[mid]:
      return search_item(a, P, start, mid)

   if P > a[mid]:
      return search_item(a, P, mid, end)

print(find_index(a, P))