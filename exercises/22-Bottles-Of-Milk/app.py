def number_of_bottles():
   for i in range(99, 0, -1): 
    print(f"{i} Bottles of beer on the wall, {i} bottles of beer\nTake one down and pass it around {i-1} bottles \
    of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

number_of_bottles()