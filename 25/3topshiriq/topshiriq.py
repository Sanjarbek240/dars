import pickle

with open("students.txt", "r") as file:
    lines = file.readlines()
students = {}
for line in lines:
    name, scores = line.strip().split(":")
    score_list = list(map(int, scores.strip().split(",")))
    students[name] = score_list

with open("students.pkl", "wb") as pkl_file:
    pickle.dump(students, pkl_file)
with open("students.pkl", "rb") as pkl_file:
    loaded_students = pickle.load(pkl_file)
for name, scores in loaded_students.items():
    avg = sum(scores) / len(scores)
    print(f"{name}: ortacha bahosi = {avg:.2f}")
 

