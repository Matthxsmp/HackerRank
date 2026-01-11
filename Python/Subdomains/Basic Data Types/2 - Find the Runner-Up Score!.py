if __name__ == '__main__':
    n = int(input())
    list = list( map( int, input().split()))
    list = [ m for m in list if m != max( list )]
    print( max( list ))





# HackerRank

# Excercise : Find the Runner-Up Score!