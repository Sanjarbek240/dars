class oquvchi:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
    def __str__(self):
        return f"oquvchi: {self.ism}, Yosh: {self.yosh}" 
o1 = oquvchi("Ali", 15)   
print(o1)    