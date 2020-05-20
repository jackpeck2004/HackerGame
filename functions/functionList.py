from tools.parseInput import Decode

functions = [func for func in dir(Decode) if callable(
    getattr(Decode, func)) and not func.startswith("__")]

