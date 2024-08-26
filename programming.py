# ACE Task Submission: Keypad Mapping
keypad_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
digits = input("Enter Digits: ")

def keypad_mapper():
    i = 0
    mapped_lst = []
    
    while i < len(digits):
        if i == 0:
            digit = int(digits[i])
            charset = keypad_map[digit]
            mapped_lst = list(charset)
        elif i >= 0:
            digit = int(digits[i])
            charset = keypad_map[digit]
            mapping_lst = list(charset)
            result_lst = []
            
            for j in mapped_lst:
                for k in mapping_lst:
                    result_lst.append(j+k)
            mapped_lst = result_lst
        i += 1
    print(mapped_lst)
    
if digits.isdigit() and "1" not in digits:
    keypad_mapper()
else:
    print("Invalid: Only Digits 2-9 Should Be Given As Input!")