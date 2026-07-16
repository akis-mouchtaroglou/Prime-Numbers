
count = int(input("How many numbers do you want to generate?  "))
numbers = [2]
print("Generated numbers:")

for i in range(count):
    print (numbers[0 + i])
    k = 0
    def repeater(numbers , i , k): 

       
        while (numbers[-1] + 1 + k) % numbers[i] == 0:
            k = k + 1
           
           
            i = len(numbers) - 1 
        
        if i > 0:
            repeater (numbers , i - 1 , k)
        else:
            #
            numbers.append(numbers[-1] + 1 + k)
            
    repeater (numbers , i , k)




        