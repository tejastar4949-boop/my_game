from pyscript import sync

def run_game():
    # 'sync.input' is the secret to making the pop-ups work!
    name1 = sync.input("Enter the first name:")
    name2 = sync.input("Enter the second name:")

    if name1 and name2:
        n1 = name1.lower().replace(" ", "")
        n2 = name2.lower().replace(" ", "")

        list1, list2 = list(n1), list(n2)
        for char in list1[:]:
            if char in list2:
                list1.remove(char)
                list2.remove(char)

        count = len(list1) + len(list2)
        flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

        if count > 0:
            while len(flames) > 1:
                split_index = (count % len(flames)) - 1
                if split_index >= 0:
                    flames = flames[split_index + 1:] + flames[:split_index]
                else:
                    flames.pop()

            print(f"🔥 Result for {name1} & {name2}: {flames[0]} 🔥")
        else:
            print("The names are too similar to calculate!")
    else:
        print("Please enter both names.")

# This line actually starts the code
run_game()
