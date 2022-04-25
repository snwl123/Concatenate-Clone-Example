from io import StringIO

def cat(source, dest):
    listOfWords = source.readlines()
    catWord = ''
    for word in listOfWords:
        catWord += word
    return dest.write(catWord)

    
    