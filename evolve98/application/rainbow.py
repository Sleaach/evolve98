import random
def rainbow():
    colors = ["🔴","🟠","🟡","🟢","🔵","🟣","⚫️","⚪️","🟤"]

    for i in range(900000):
        randm = random.choice(colors)
        print(randm)
