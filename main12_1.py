class StipChars:
    def __init__(self, chars):
        self.__counter = 0
        self.chars = chars


    def __call__(self, *args, **kwargs):
        if not  isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.chars)

s1 = StipChars("?:!.; ")
s2 = StipChars(" ")
res = s1(" Hello World! ")
res2 = s2(" Hello World! ")
print(res, res2, sep="\n")
