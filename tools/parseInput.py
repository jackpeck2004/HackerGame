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

    def base64(flag):
        tmp = base64.b64decode(flag)
        # flag = flag.encode('ascii')
        # flag = flag.decode('ascii')
        # print(tmp)
        return str(tmp)


class Encode():

    def base64(flag):
        print(flag)
        message_bytes = flag.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return str(base64_message)


'''
message = "Python is fun"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')
'''
