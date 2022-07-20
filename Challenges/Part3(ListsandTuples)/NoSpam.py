menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Write code to print out all meals in the menu buy with spam removed.
# You can choose which approach you want to use:
# Remove spam from each list then print the list.
# Print out the items in each list as long as it's not spam.

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if "spam" in meal[index]:
#             break
#         else:
#             print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()