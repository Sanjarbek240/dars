class ballar:
    def __init__(self, ballar):
        self.ballar = ballar
    def add(self, qoshish):
        umumiy = self.ballar + qoshish.ballar
        return ballar(umumiy )   
    def __str__(self):
        return str(self.ballar) 
ballar1 = ballar([85, 90, 78])
ballar2 = ballar([92, 88, 75])

umumiy = ballar1.add(ballar2)
print(umumiy)