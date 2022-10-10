
def malo_talo_meter(is_male,is_tall):
    if is_male and is_tall:
        print("You are a tall male")
    elif is_male and not (is_tall):
        print("You are a short male")
    elif not (is_male) and is_tall:
        print("You are not a male but are tall")
    else:
        print("You are either not male or not tall or both")
is_male =  input("say True if u are male otherwise u gay\n")
is_tall =  input("say True if u are tall otherwise u lebo\n")
print(is_tall.phrase[0].upper())
print(is_male.phrase[0].upper())
malo_talo_meter(is_male,is_tall)
print("boolean input lina sik yo technique milena")
