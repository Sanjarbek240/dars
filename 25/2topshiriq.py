import pickle

foydalanuvchi1 = {'ism': 'Ali', 'password': 2025, 'score': 80},{'ism': 'Laylo', 'password': 'abcd', 'score': 90}
with open('foydalanuvchi.pkl', 'wb') as fayl:
    pickle.dump(foydalanuvchi1, fayl)