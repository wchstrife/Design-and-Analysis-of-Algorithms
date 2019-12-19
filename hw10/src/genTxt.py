import random

with open("./data/random_data.txt","a+",encoding="utf-8") as f:
    for i in range(0, 2000000):
        c = random.choice('1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
        f.write(c)
    

