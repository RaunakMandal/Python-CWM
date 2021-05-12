letters = ["a", "b", "c"]

# Add
letters.append("d")  # Add at end
print(letters)
letters.insert(1, "bro")  # Add at position (pos, elem)
print(letters)

# Remove
letters.pop()  # Remove from last
print(letters)
letters.pop(1)  # Remove from position (pos)
print(letters)
letters.remove("a")  # Removed first occurance
print(letters)
del letters[0:1]  # Removes from range
print(letters)
letters.clear()  # Clears
print(letters)
