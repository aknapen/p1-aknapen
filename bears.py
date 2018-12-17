def bears(n):
    canWin = False
    '''Base Cases'''
    if n == 42:
        canWin = True
        
    elif n > 42:
        '''Different possible paths determined by value of n. canWin saves the
           status of the run as a whole (i.e. whether a solution that ends in 42
           has been reached)'''
        if not canWin and n % 2 == 0:
            canWin = bears(n//2)
            
        if not canWin and n % 5 == 0:
            canWin = bears(n-42)

        if not canWin and (n % 4 == 0 or n % 3 == 0):
            x = str(n)
            intList = [int(num) for num in x]
            if (len(intList) >= 2):
                if intList[-1] * intList[-2] > 0:
                    canWin = bears(n - (intList[-1] * intList[-2]))
                else:
                    canWin = False
            
    return canWin
        




print(bears(256))
