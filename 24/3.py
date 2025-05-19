class Sinfxona:
    def __init__(self, oquvchilar):
        self.oquvchilar = oquvchilar

    def __getitem__(self, index):
        return self.oquvchilar[index]

    def __iter__(self):
        return iter(self.oquvchilar)

sinfxona = Sinfxona(["Diyor", "rahim", "ruxshona", "odina"])
print(sinfxona[1])

for oquvchi in sinfxona:
    print(oquvchi)
