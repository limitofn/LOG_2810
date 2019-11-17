import Objet as obj

def fillArrayFromFile(fileName):
    f = open(fileName, "r")
    fileContent = f.readlines()

    listObject = []

    for line in fileContent:
        inputNode = [x for x in line.strip().split(' ')]
        listObject.append(obj.Objet(inputNode[0],inputNode[1],inputNode[2]))
    return listObject