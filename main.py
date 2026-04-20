# No imports needed for standard FLAMES logic in PyScript

def run_game():
    # PyScript will show a pop-up box in the browser for these inputs
    name1 = input("Enter the first name:")
    name2 = input("Enter the second name:")

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

            print(f"Result for {name1} & {name2}: {flames[0]}")
        else:
            print("The names are too similar to calculate!")
    else:
        print("Please provide both names.")

# Run the game
run_game()
