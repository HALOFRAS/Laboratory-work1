a=input("Строка: ")
print( "".join( [e for e in a if e not in "уеыаоэяиюeyuioa"] ))