tC = int(raw_input())

for i in xrange(tC):
    
    nStrings = int(raw_input())
    
    li = []
    nAwe = 0
    
    for j in xrange(nStrings):
        
        a = raw_input()
        li.append(a)
    
    for a in xrange(len(li)):
        
        for b in xrange((a + 1), len(li)):
            
            if(li[a][0] == (li[b][0]) ):
                
                currentString = li[b] + li[a]
                revString = currentString[::-1]
                
                if currentString == revString:
                    nAwe += 1
                    
    print nAwe
                
                                
    
    