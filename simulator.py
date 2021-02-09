from random import choice

questions = ["Why is the sky blue?: ", "Why are we here?: ",
             "Why are we not playing?:"]
question = choice(questions)
answer = input(questions).strip().lower()
print(answer)

while answer != "just because":
    answer = input("why..").strip().lower()
print("Oh okay..")
