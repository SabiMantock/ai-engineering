name = "Sabi"
realm = "Mortal"
qi = 15
qi = qi + 10
technique = "Fireball"
spirit_stones = 30
age = 27

print(f"Name: {name}")
print(f"Realm: {realm}")
print(f"Qi: {qi}")
print(f"Technique: {technique}")
print(f"Spirit Stones: {spirit_stones}")
print(f"Age: {age}")

# Training day calculation
qi = qi + 25
spirit_stones = spirit_stones - 10
print(f"Qi: {qi}")
print(f"Spirit Stones: {spirit_stones}")
print(f"{name} is {age} cultivating for 3 years")
print("Qi: {qi}")

# To be used later.
# while qi < 100:
#     qi = qi + 7
#     print("Training...", qi)
# print("BREAKTHROUGH!")

# Technique Scrolls
scroll = "ashen palm strike"
print(scroll.title())
print(scroll.upper().replace(" ", "-"))
print(scroll[0])
print(len(scroll))

print(scroll[0:5])    # characters 0,1,2,3,4 — stops BEFORE 5
print(scroll[:5])     # same thing
print(scroll[-5:])    # from 11 to the end

