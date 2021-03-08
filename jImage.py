from PIL import Image
import numpy as np


def __Extract(bList,msgLen):
    '''
    __Extract(bList,msgLen)
    ----------------------
    Purpose:
    extracts the selected amount of binaries from the image's byte list
    
    Args:
    bList   - list - byte list from which the program is extracting data
    msgLen  - int  - amount of bytes that the program is extracting
    
    Notes:
    number of bits extracted = (msgLen * 8)
    '''
    bret = ''
    for i in range(msgLen*8):
        bina = list(__GetBin(bList[i]))
        bret += bina[len(bina)-1]
    return bret


def __Save(img,bList):
    '''
    __Save(img,bList)
    ----------------
    Purpose:
    Saves the image with the modified byte list

    Args:
    img   - Image - The image obj, the program is saving the new byte array here
    bList - list  - The modified Byte list that the program is saving
    '''
    arr = bytes(bList)
    newImage = Image.frombytes(img.mode, img.size, arr)
    newImage.save('Encoded.png')


def __GetBin(intero):
    '''
    __GetBin(intero)
    ----------------
    Purpose:
    returns the integer converted to bynary (str)

    Args:
    intero - int - the ingeger that has to be converted
    '''
    bina = bin(intero)[2:]
    for i in range(len(bina),8):
        bina = "0" + bina
    return bina


def __GetInt(binario):
    '''
    __Getint(binario)
    ----------------
    Purpose:
    returns the binary converted to integer (int)

    Args:
    binario - str - the binary that has to be converted
    '''
    return int(binario,2)


def __Inject(lista,data):
    '''
    __Inject(lista,data)
    --------------------
    Purpose:
    modifies the given Byte list (lista) by hiding
    the message (str(bin)) in there

    Args:
    lista  - list - byte list that the program is hiding the given data into
    data   - str  - data that the program is hiding inside the given list
    '''
    for i in range(len(data)):
        bina = list(__GetBin(lista[i]))
        bina[len(bina)-1] = data[i]
        inte = __GetInt(''.join(bina))
        lista[i] = inte

            
def __GetBytes(binario):
    '''
    __GetBytes(binario)
    -------------------
    Purpose:
    returns the Byte array got from the given binary (binario)

    Args:
    binario - str - binary that the program gets the Byte array from
    '''
    ints = []
    for i in range(0,len(binario),8):
        bina = binario[i:i+8]
        ints.append(__GetInt(bina))
    return bytes(ints)


def __GetImageByteList(image):
    '''
    __GetImageByteList(image)
    -------------------------
    Purpose:
    returns the given image's list of bytes

    Args:
    image - Image (PIL) - Image object that the program is taking the list of bytes from
    '''
    return list(image.tobytes())


def EncodeFile(imagePath,filePath):
    '''
    EncodeFile(imagePath,filePath)
    ---------------------------
    Purpose:
    Hides the file at the given filePath in the image at the given imagePath

    Args:
    imagePath - str - path to the selected image
    filePath  - str - path to the selected file
    '''
    fileBytes = open(filePath,"rb").read()
    fileBin = ''.join([__GetBin(b) for b in fileBytes])
    __EncodeBina(imagePath,fileBin)


def EncodeText(imagePath,message):
    '''
    EncodeText(imagePath,message)
    ------------------------
    Purpose:
    Hides the given message in the image at the given imagePath

    Args:
    imagePath - str - path to the selected image
    message   - str - the message that the program is hiding
    '''
    message = message.replace(" ","|").replace("\n","<>")
    binMessage = ''.join([__GetBin(b) for b in bytearray(message.lower(),'utf8')])
    __EncodeBina(imagePath,binMessage)

    
def __EncodeBina(imagePath,bina):
    '''
    EncodeBina(imagePath,bina)
    ------------------------
    Purpose:
    Hides the given binary string in the image at the given imagePath

    Args:
    imagePath - str - path to the selected image
    bina      - str - the binary string that the program is hiding
    '''
    img = Image.open(imagePath)
    imageByteList = __GetImageByteList(img)
    __Inject(imageByteList,bina)
    __Save(img,imageByteList)


def DecodeFile(imagePath,msgLen,ext):
    '''
    DecodeFile(imagePath,msgLen,ext)
    ---------------------------
    Purpose:
    Decodes the file hidden in the given imagePath by extracting the specified amount of data,
    then saves the extracted file with the given extention

    Args:
    imagePath - str - path to the selected image
    msgLen    - int - amount of bytes that the program is extracting
    ext       - str - the extention that will be given to the extracted file
    '''
    extractedBina = __DecodeBina(imagePath,msgLen)
    fileBytes = __GetBytes(extractedBina)
    decodedFile = open('decoded.'+ext,'wb')
    decodedFile.write(fileBytes)


def DecodeText(imagePath,msgLen):
    '''
    DecodeText(imagePath,msgLen)
    ---------------------------
    Purpose:
    returns the decoded text hidden in the given imagePath,
    which is decoded by extracting the specified amount of data

    Args:
    imagePath - str - path to the selected image
    msgLen    - int - amount of bytes that the program is extracting
    '''
    extractedBina = __DecodeBina(imagePath,msgLen)
    message = __GetBytes(extractedBina).decode('utf8')
    message = message.replace("|"," ").replace("<>","\n")
    return message


def __DecodeBina(imagePath,msgLen):
    '''
    DecodeBina(imagePath,msgLen)
    ---------------------------
    Purpose:
    returns the decoded binary string hidden in the given imagePath,
    which is decoded by extracting the specified amount of data

    Args:
    imagePath - str - path to the selected image
    msgLen    - int - amount of bytes that the program is extracting
    '''
    img = Image.open(imagePath)
    imgByteList = __GetImageByteList(img)
    extractedBina = __Extract(imgByteList,msgLen)
    return extractedBina


def __DisplayBin(bina):
    #DEBUG
    b = str(bina)
    for i in range(0,len(b),8):
        print(str(int(i/8)) + "\t" + b[i:i+8])
