firma = "Audi"
limit = 25
i = 0

while i <= limit:
    if i == 0:
        print("w salonie " + firma + " nie ma samochodow")
    if i != 0:
        print("Przywieziono auto, w salonie " + firma + " jest " + str(i) + " samochodow")
    if i == limit:
        print("Osiagnieto limit aut w salonie " + firma)

    i = i + 1
