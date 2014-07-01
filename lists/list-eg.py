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

animals.remove("cow") #remove the actual item if it finds it
animals.pop(1); #remove the item at index from the list and return it to you
del(animals[1]) #like .pop in that it will remove the item at the given index, but it won't return it
animals.sort()
print animals