from threading import Lock


class Singleton:
    _instacnce = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instacnce:
            with Lock():
                if cls not in cls._instacnce:
                    cls._instacnce[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instacnce[cls]



if __name__ == "__main__":
    obj1= Singleton()
    obj2 = Singleton()
    print(id(obj1))
    print(id(obj2))
    obj3 = Singleton()
    print(id(obj3))
