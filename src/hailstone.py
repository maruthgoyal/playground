def hailstone(num):
    
    nSteps = 0
        
    while(num != 1):
        
        if(num % 2 == 0):
            
            num /= 2
            nSteps += 1
                
        else:
                
            num = (3 * num) + 1
            nSteps += 1
            
    return nSteps

print "It takes ", hailstone(input("ENTER: ")), " steps for the number 19356"