if __name__ == '__main__':
    nested = [[input(), float(input())] for m in range(int(input()))]
    students = sorted(nested[m][0] for m in range(0,len(nested)) if nested[m][1]==sorted(list(set(m[1] for m in nested)))[1])
    print (*(students[m] for m in range(0,len(students))), sep=f'\n')





# HackerRank

# Excercise : Nested Lists