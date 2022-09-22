bottles = 39
bottles_in_boxes = 6

print("Number of Bottles:" , bottles)

print("Number of Bottles That Can Fit in a Single Box:" , bottles_in_boxes)

print("Number of Full Boxes:" , str(bottles // bottles_in_boxes))

print("Bottles Left Over:" , str(bottles % bottles_in_boxes))