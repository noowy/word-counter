import sys

def countWords(filename):
    textFile = str(open(filename).read())
    textFile = textFile.lower()
    listOfWords = textFile.split()
    returnList = [(listOfWords[0], 0)]
    buffTuple = ()

    for i in range (0, len(listOfWords)):
        count = 1
        mark = 0
        buffCount = 0
        for j in range (0, len(listOfWords)):
            if i == j:
                continue
            if listOfWords[i] == listOfWords[j]:
                count += 1

        if i == 0:
            returnList[0] = (listOfWords[0], count)
            continue

        if count > 1:
            for j in range (0, len(returnList)):
                if listOfWords[i] == returnList[j][0]:
                    mark = 1
                    break
            if mark != 1:
                buffTuple = (listOfWords[i], count)
                returnList.append(buffTuple)
        
        elif count == 1:
            buffTuple = (listOfWords[i], count)
            returnList.append(buffTuple)
    return returnList

def print_words(filename):
    outputList = countWords(filename)
    outputList.sort(key = lambda x: x[0][0])
    for i in range (0, len(outputList)):
        if i % 2 != 0:
            continue
        print outputList[i][0], outputList[i][1]
    return 0

def print_top(filename):
    outputList = countWords(filename)
    outputList.sort(key = lambda x: x[::-1], reverse = 1)
    for i in range (0, 20):
        try:
            print outputList[i][0], outputList[i][1]
        except IndexError:
            break
    return 0

def countMorethanOne(filename):
    count = 1
    listOfWords = countWords(filename)
    for i in range (0, len(listOfWords)):
        if i % 2 != 0:
            continue
        if listOfWords[i][1] > 1:
            count += 1
    print count
    return 0

def print_sorted(filename):
    outputList = countWords(filename)
    outputList.sort(key = lambda x: x[::-1], reverse = 1)
    for i in range (0, len(outputList)):
        if i % 2 != 0:
            continue
        try:
            print outputList[i][0], outputList[i][1]
        except IndexError:
            break
    return 0    

def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount file} '
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    elif option == '--countmore1':
        countMorethanOne(filename)
    elif option == '--sortcount':
        print_sorted(filename)
    else:
        print 'unknown option :' + option
        sys.exit(1)

if __name__ == '__main__':
    main()