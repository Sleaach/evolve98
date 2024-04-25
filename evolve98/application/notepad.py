def notebook():
    with open("note.txt", "r") as note:
            content = note.read()
            print(f"\n{content}")
