def applyRunLengthEncoding(serie):
    i =1
    encodedSerie=list()
    char=serie[0]

    for c in serie[1:]:
        if c == char:
            i=i+1

        else:
            encodedSerie.append([char,i])
            char = c
            i=1
    encodedSerie.append([char,i])
    return encodedSerie
try:
    print("Write the serie you want to encode. \nPlease use quotation marks!! ")
    serie= (input())
    print(serie)
    print("Encoded Serie: ",applyRunLengthEncoding(serie))
except:
    print("Error: You should write your input using quotation marks! Try again.")


