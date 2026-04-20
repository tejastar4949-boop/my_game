import streamlit as st  # This is the 'Web Engine'

# This replaces the pinck background with a clean website title
st.title("🔥 FLAMES Relationship App By Surya Teja.S")

# Instead of input(), we use text_input for web boxes
name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

# We wrap your logic in a button so it only runs when clicked
if st.button("See Results"):
    if name1 and name2:
        # --- YOUR ORIGINAL LOGIC STARTS HERE ---
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

            # Instead of print(), we use st.success to show a green box
            st.success(f"Result: {flames[0]}")
        # --- YOUR ORIGINAL LOGIC ENDS HERE ---
    else:
           st.warning("Please type both names first!")
