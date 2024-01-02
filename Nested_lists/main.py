if __name__ == '__main__':
    dic = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic[name] = score
    
    names = [i for i in dic]
    marks = [dic[i] for i in dic]
    
    low = min(marks)
    while low in marks:
        index = marks.index(low)
        marks.pop(index)
        names.pop(index)   
    
    second_lowest = min(marks)
    indices = [i for i, mark in enumerate(marks) if mark == second_lowest]
    
    records = [names[i] for i in indices]
    records.sort()
    for names in records:
        print(names)
    
