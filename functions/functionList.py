from tools.parseInput import Decode

tmp = [func for func in dir(Decode) if callable(
    getattr(Decode, func)) and not func.startswith("__") ] 

tmp.append("reset")
tmp.append("submit")

functions = tmp

