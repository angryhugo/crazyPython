animals=["cat","dog","cow","tiger"]

# animals[2]="sheep" 
# IndexError: list assignment index out of range
animals.append("sheep")
print animals

slice_animals=animals[1:3]
print slice_animals # ["dog","cow"]
print len(animals)

print animals[:3] #first three" 
print animals[3:] #last two

cow_index = animals.index("cow")
animals.insert(cow_index,"elephant")

for animal in animals:
    print animal

animals.sort()
print animals