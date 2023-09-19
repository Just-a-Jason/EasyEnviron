class Abstract:
    def __init__(self):
        raise TypeError(
            f"\033[91m{self.__class__.__name__} class cannot be instantiated\033[0m")
