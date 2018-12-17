def perm_gen_lex(a):
    permList = []

    '''Base Cases'''
    if len(a) == 1:
        return [a]
    if len(a) == 0:
        return []
    
    for char in range(len(a)):
        '''Separate out the character to stay at the beginning of the list (a)
           and the characters to alternate position in the list (tempList)'''
        pos = a[char]
        tempList = a[:char] + a[char+1:]

        '''Run the permutation algorithm on the simplified list'''
        permListItem = perm_gen_lex(tempList)

        '''Add the outcome of each previously simplified list to the overarching
           list'''
        for listItem in permListItem:
            permList.append(pos + listItem)
            
    return permList


