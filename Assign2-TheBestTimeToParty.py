#TheBestTimeToParty
# celebrities       Comes   Goes
# beyonce           6       7
# Taylor            7       9
# Brad              10      11
# Katy              10      12
# Tom               8       10
# Drake             9       11
# Alicia            6       8   

# [6 7)    <- notice that at 6:59, Beyonce is there, but 7, she will be gone 
# but the great thing about this, is that python intervals are integer;  why does this help us? 
# Answer: The range when someone is there, say 9-11 only needs to care about the times [9,10], inclusive. 
# therefore python's natural usage of lists that start inclusively at the first value, and end non-inclusive are perfect. 
# e.g. mylist[9:11] means it represents 9, 10 but not 11
######
# How to build this array above to represent my celebs and their comes/goes times? 
# I chose two arrays; one for the celebs, and one for the times.  In reality, the names of the celebs aren't given, however
# I think I will keep a list of their names.
def firstAttempt(): 

    celebs = ['beyonce', 'taylor', 'brad', 'katy', 'tom', 'drake', 'alicia']
    times = [list(range(6,7)), list(range(7,9)), list(range(10,12)), list(range(10,12)), list(range(8,10)), list(range(9,11)), list(range(6,8))]

    maxcount = 0
    maxindex = 0

    celebNames=['' for x in range(max(max(times)) + 1)]
    count=[0 for x in range(max(max(times)) + 1)]

    #print (times)
    #print (min(min(times)))

    for j in range(min(min(times)) , max(max(times))+1):
        for index, time in enumerate(times):
            if(time[0] == j):
                count[j] = count[j]+1
                celebNames[j] = ' '.join([celebNames[j],celebs[index-len(celebs)]])
            elif(len(time) > 1): 
                if(time[0] <= j) and (j < (time[len(time)-1] + 1)):
                    count[j] = count[j] + 1
                    celebNames[j] = ' '.join([celebNames[j],celebs[index-len(celebs)]])
        if(maxcount < count[j]):
            maxindex = j
            maxcount = count[j]

    print("The best time to meet a  celebrity is at ", maxindex, " and you would meet these people: ", celebNames[maxindex])

firstAttempt()

