nums = []
totEven = 0
totOdd = 0

print(end="Enter the Size: ")
size = int(input())

print(end="Enter " +str(size)+ " Numbers: ")
for i in range(size):
  nums.insert(i, int(input()))

for i in range(size):
  if nums[i]%2==0:
    totEven = totEven+1
  else:
    totOdd = totOdd+1

print("\nEven Number: " +str(totEven))
print("Odd Number: " +str(totOdd))
