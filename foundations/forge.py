color = "dark"
element = "fire"
form = "palm"
full_name = f"{color} {element} {form}".title()
battle_cry = f"{full_name.upper().replace(' ', '-')}!!!"
sigil = f"{color[0]}.{element[0]}.{form[0]}".upper()
print(full_name)
print(battle_cry)
print(sigil)
print(f"Scroll length: {len(full_name)} characters")