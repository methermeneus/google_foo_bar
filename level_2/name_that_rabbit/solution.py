def answer (names):
    """
    Reason doesn't matter. Just... Put names in order of magnitude, greatest to
    least. Magnitude is the sum of all the letters' places in the alphabet. So,
    Annie = 43, Liz = 47, and Bonnie = 59 (which means these three names should
    be in the opposite order). Where names have the same value, put them in
    reverse alphabetical order: So, since Al and CJ both = 13, the order should
    be CJ, Al.

    That's it.

    Alphabetical order is easy. Just put all names of the same value through a
    sort. The real problem seems to be sorting the names by value in the first
    place.
    """
    # Don't process if we don't need to.
    if len(names) == 1:
        return names


    # I need direct values; Python doesn't seem to put these numbers in the
    # right order otherwise.
    def numberize (name):
        namenum = 0
        alphanum=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range (0,len(name)):
            namenum += alphanum.index(name[i])
        return namenum

    for i in range(0,len(names)):
        x=numberize (names[i])
        xstr=''
        if x < 10:
            xstr='000'+str(x)
        elif x < 100:
            xstr='00'+str(x)
        elif x < 1000:
            xstr='0'+str(x)
        else:
            xstr=str(x)
        names[i] = xstr + names[i]
    
    # I feel like an idiot for spending all this time trying complex themes and
    # implementing my own sort functions. Then, I realized, "Hey, doesn't
    # Python have that list-sorting function that does exactly what I need?"
    result = sorted(names)

    for i in range (0,len(result)):
        result[i] = result[i][4:]

    result.reverse()

    return result
