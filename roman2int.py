



def roman_to_int(rom):
    roman_to_int_mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    
    total = 0
    i = 0

    while i < len(rom):
        if i + 1 < len(rom) and rom[i:i + 2] in roman_to_int_mapping:
            print(rom[i:i+2])
            total += roman_to_int_mapping[rom[i:i + 2]]
            i += 2
            
        else:
            total += roman_to_int_mapping[rom[i]]
            i += 1
    
    return total

rom = "MMMM"
integer_value = roman_to_int(rom)
print(f"The Roman numeral {rom} is equivalent to the integer value {integer_value}")


