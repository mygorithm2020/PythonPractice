#-*- coding: utf-8 -*-
import random

TRIALS = 100000

for j in range(2, 100):
    same_birthdays = 0
    for _ in range(TRIALS):    
        birthdays = []
        for i in range(j):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f'{j}명 일때 {same_birthdays / TRIALS * 100}%')