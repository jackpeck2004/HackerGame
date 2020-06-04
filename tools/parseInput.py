import base64

def parseInput(inputFunction, flag):
    choice = inputFunction.split(' ')
    # print("\nYou chose the function", choice[1])
    if choice[0] == "d":
        flag = getattr(Decode, choice[1])(flag)
    elif choice[0] == "e":
        flag = getattr(Encode, choice[1])(flag)

    return flag


class Decode():

    def CeaserCypher(flag):
        s = int(input("offset: "))
        s *= -1
        result = ""
        for i in range(len(flag)):
            char = flag[i]
            if(char == " "):
                result += " "
            if(char == "_"):
                result += "_"
            if(char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def Base64(flag):
        f = flag.encode('ascii')
        tmp = base64.b64decode(f)
        tmp = str(tmp)
        tmp.lstrip("'")
        tmp = tmp[2:]
        tmp = tmp[:-1]
        return tmp


class Encode():

    def CeaserCypher(flag, s="ciao"):
        if(s == "ciao"):
            s = int(input("offset: "))
        result = ""
        for i in range(len(flag)):
            char = flag[i]
            if(char == " "):
                result += " "
            if(char == "_"):
                result += "_"
            if(char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def Base64(flag):
        print(flag)
        message_bytes = flag.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return str(base64_message)
