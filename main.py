from pyscript import sync, display

# This tells the website the game has started
display("", target="loading-msg")

def run_game():
    try:
        # These will appear as pop-up boxes at the top of the browser
        name1 = sync.input("Enter the first name:")
        name2 = sync.input("Enter the second name:")

        if not name1 or not name2:
            print("You must enter two names!")
            return

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
            
            # This result will print onto the webpage itself
            print(f"--- RESULT ---")
            print(f"Names: {name1} & {name2}")
            print(f"Status: {flames[0]}")
        else:
            print("The names are too similar to calculate!")
            
    except Exception as e:
        print(f"Something went wrong: {e}")

# Start the game
run_game()
