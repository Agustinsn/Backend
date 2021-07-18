n1=input("Ingrese la primera palabra: ")

arr1=list(n1)
for n in len(arr1):
    comp=list(n1)
    comp.reverse()
    if arr1[n]==comp[n]:
        print(True)
    else :print(False)


