def kg_to_lbs(weight_kg):
    return weight_kg * 2.20462

def lbs_to_kg(weight_lbs):
    return weight_lbs / 2.20462

def main():
    print("WEIGHT CONVERTOR APPLICATION")
    print("1. kg to lbs")
    print("2. lbs to kg")
    choice = int(input("Enter your choice (1 or 2): "))


    if choice == 1:
        weight_kg = float(input("Enter your weight in kgs: "))
        print("Weight in lbs: ", kg_to_lbs(weight_kg))

    elif choice == 2:
        weight_lbs = float(input("Enter your weight in lbs: "))
        print("Weight in kg: ", lbs_to_kg(weight_lbs))  

    else:
        print("invalid choice")

if __name__ == "__main__":
    main() 