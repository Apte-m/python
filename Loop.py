count = int(input())
result = 0
for x in range(count):
     x =  int (input())
     if x == 0:
         result =  result + 1
      
print(result)

value = int(input())

result = 0
while True:
    if value % 2 == 0:
        result += + 1
        value = value // 2 
        
    if value % 2 != 0:
       break
   
print(result)