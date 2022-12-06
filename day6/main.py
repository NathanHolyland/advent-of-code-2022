def getStream():
    datastream = ""
    while True:
        x = input()
        if x == "":
            break
        datastream = datastream+x
    return datastream

def findMarker(datastream, length):
    for i in range(len(datastream)):
        sub = datastream[i:i+length]
        valid = True
        values = []
        for j in sub:
            if j in values:
                valid = False
            values.append(j)
        if not valid:
            continue
        else:
            return i+length

                

if __name__ == "__main__":
    print(findMarker(getStream(), 14))