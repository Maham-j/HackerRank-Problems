if __name__ == '__main__':
    s = input()
    
    condition1 =any(char.isalnum() for char in s)
    print(condition1)
    
    condition2 =any(char.isalpha() for char in s)
    print(condition2)
    
    condition3 =any(char.isdigit() for char in s)
    print(condition3)
    
    condition4 =any(char.islower() for char in s)
    print(condition4)
    
    condition5 =any(char.isupper() for char in s)
    print(condition5)
    
