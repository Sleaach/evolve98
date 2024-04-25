import pandas as pd
def df():

    print("\nÇıkmak için <>")

    while True:
        data = input("Veri: ")
        index = input("Index: ")

        if data == "<>" or index == "<>":
            break
        series = pd.Series(data, index=[index])

        with open("data.txt", "a") as file:
            file.write(series.to_string() + '\n')
