multi_line="""Beau is
39 years old"""

escaped_str="He said, \"Python is great!\"\nNew line here."
path_str="C:\\path\\to\\file"

age=25
formatted=f"Gem is {age} years old."
print(formatted)

phrase="Beau is cool"

print(phrase.upper())
print(phrase.lower())
print(phrase.title())
print(phrase.startswith("Beau"))
print(phrase.endswith("cool"))
print(phrase.replace("cool","great"))
print(phrase.split(" "))
print("  hello  ".strip())

print(phrase[0])
print(phrase[-1])
print(phrase[0:4])
print(phrase[5:])
print(len(phrase))