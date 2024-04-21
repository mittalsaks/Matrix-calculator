#addition function
def add(M1,M2,n,m):
    for i in range (n):
        for j in range (m):
            M1[i][j]=M1[i][j]+M2[i][j]
    return
#substraction function
def sub(M1,M2,n,m):
    for i in range (n):
        for j in range (m):
            M1[i][j]=M1[i][j]-M2[i][j]
    return
#multipication function
def mul(M1,M2,n1,m1,m2):
    c=[]
    for i in range (n1):
        row=[]
        for j  in range (m2):
            temp=0
            row.append(temp)
        c.append(row)
    for i in range (n1):
        for j in range (m2):
            for x in range (m1):
                c[i][j]=c[i][j]+(M1[i][x]*M2[x][j])
    return c
#transpose function
def tra_fn(M1,N):
    def getCofactor(A, temp, p, q, n):
        i = 0
        j = 0
        for row in range(n):
            for col in range(n):
                if (row != p and col != q):
                    temp[i][j] = A[row][col]
                    j += 1
                    if (j == n - 1):
                        j = 0
                        i += 1
    def determinant(A, n):
        D = 0
        if (n == 1):
            return A[0][0]
        temp = []
        for i in range(N):
            temp.append([None for _ in range(N)])
        sign = 1 
        for f in range(n):
            getCofactor(A, temp, 0, f, n)
            D += sign * A[0][f] * determinant(temp, n - 1)
            sign = -sign
        return D
    def adjoint(A, adj):
        if (N == 1):
            adj[0][0] = 1
            return
        sign = 1
        temp = []
        for i in range(N):
            temp.append([None for _ in range(N)])
        for i in range(N):
            for j in range(N):
                getCofactor(A, temp, i, j, N)
                sign = [1, -1][(i + j) % 2]
                adj[j][i] = (sign)*(determinant(temp, N-1))
    def inverse(A, inverse):
        det = determinant(A, N)
        if (det == 0):
            print("Singular matrix, can't find its inverse")
            return False
        adj = []
        for i in range(N):
            adj.append([None for _ in range(N)])
        adjoint(A, adj)
        for i in range(N):
            for j in range(N):
                inverse[i][j] = adj[i][j] / det
        return True
    def display(A):
        for i in range(N):
            for j in range(N):
                print(A[i][j], end=" ")
            print()
    def displays(A):
        for i in range(N):
            for j in range(N):
                print(round(A[i][j], 6), end=" ")
            print()
    A = M1
    adj = [None for _ in range(N)]
    inv = [None for _ in range(N)]
    for i in range(N):
        adj[i] = [None for _ in range(N)]
        inv[i] = [None for _ in range(N)]
    print("Input matrix is :")
    display(A)
    print("\nThe Adjoint is :")
    adjoint(A, adj)
    display(adj)
    print("\nThe Inverse is :")
    if (inverse(A, inv)):
        displays(inv)

#input of matrixes
n1=int(input("No of rows in matrix1 "))
m1=int(input("No of columns in matrix1 "))
M1=[]
print("Enter the elements one by one")
for i in range (n1):
    row=[]
    for j in range (m1):
        ele = int(input())
        row.append(ele)
    M1.append(row)
n2=int(input("No of rows in matrix2 "))
m2=int(input("No of columns in matrix2 "))
M2=[]
print("Enter the elements one by one")
for i in range (n2):
    row=[]
    for j in range (m2):
        ele = int(input())
        row.append(ele)
    M2.append(row)
n3=int(input("No of rows in matrix3 "))
m3=int(input("No of columns in matrix3 "))
M3=[]
print("Enter the elements one by one")
for i in range (n3):
    row=[]
    for j in range (m3):
        ele = int(input())
        row.append(ele)
    M3.append(row)

#list of actions

print("WHAT DO YOU WANT TO PERFORM")
print("Enter 1 for Matrix Addition")
print("Enter 2 for Matrix Substraction")
print("Enter 3 for Matrix Multipilcation")
print("Enter 4 for Matrix Inverse")
choice=int(input("Enter: "))
if(choice==1):
    print("For additon of:")
    print("M1 and M2: Enter 1")
    print("M2 and M3: Enter 2")
    print("M1 and M3: Enter 3")
    print("M1,M2 and M3: Enter 4")
    c1=int(input())
    if(c1==1):
        if(n1==n2 and m1==m2):
            add(M1,M2,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Addition not possible!")
    elif(c1==2):
        if(n2==n3 and m2==m3):
            add(M2,M3,n2,m2)
            for i in range (n1):
                print(M1[i])
        else:
            print("Addition not possible!")
            
    elif(c1==3):
        if(n1==n3 and m1==m3):
            add(M1,M3,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Addition not possible!")        
    elif(c1==4):
        if(n2==n2==n3 and m1==m2==m3):
            add(M1,M2,n1,m1)
            add(M1,M3,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Addition not possible!")
if(choice==2):
    print("For subtraction of:")
    print("M1 and M2: Enter 1")
    print("M2 and M3: Enter 2")
    print("M1 and M3: Enter 3")
    print("M1,M2 and M3: Enter 4")
    c1=int(input())
    if(c1==1):
        if(n1==n2 and m1==m2):
            sub(M1,M2,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Subtraction not possible!")
    elif(c1==2):
        if(n2==n3 and m2==m3):
            sub(M2,M3,n2,m2)
            for i in range (n1):
                print(M1[i])
        else:
            print("Subtraction not possible!")
            
    elif(c1==3):
        if(n1==n3 and m1==m3):
            sub(M1,M3,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Subtraction not possible!")        
    elif(c1==4):
        if(n2==n2==n3 and m1==m2==m3):
            sub(M1,M2,n1,m1)
            sub(M1,M3,n1,m1)
            for i in range (n1):
                print(M1[i])
        else:
            print("Subtraction not possible!")
if(choice==3):
    print("For multiplication of:")
    print("M1 and M2: Enter 1")
    print("M2 and M3: Enter 2")
    print("M1 and M3: Enter 3")
    print("M1,M2 and M3: Enter 4")
    c1=int(input())
    if(c1==1):
        if(m1==n2):
            M1=mul(M1,M2,n1,m1,m2)
            for i in range (n1):
                print(M1[i])
        else:
            print("Multiplication not possible!")
    elif(c1==2):
        if(m2==n3):
            M1=mul(M2,M3,n2,m2,m3)
            for i in range (n1):
                print(M1[i])
        else:
            print("Multiplication not possible!")
            
    elif(c1==3):
        if(m1==n3):
            M1=mul(M1,M3,n1,m1,m3)
            for i in range (n1):
                print(M1[i])
        else:
            print("Multiplication not possible!")        
    elif(c1==4):
        if(m1==n2):
            M1=mul(M1,M2,n1,m1,m2)
            if(m2==n3):
                mul(M1,M3,n1,m2,m3)
                for i in range (n1):
                    print(M1[i])
            else:
                print("Multiplication not possible!")
        else:
            print("Multiplication not possible!")
if(choice==4):
    print("For transpose of:")
    print("M1 : Enter 1")
    print("M2 : Enter 2")
    print("M1 : Enter 3")
    print("To end finding transpose: Enter 0")
    c1=int(input())
    while(c1!=0):
        if(c1==1 and n1==m1):
            tra_fn(M1,n1)
        elif(c1==2 and n2==m2):
            tra_fn(M2,n2)
        elif(c1==3 and n3==m3):
            tra_fn(M2,n2)
        else:
            print("Inverse does not exists for the given matrix")
        c1=int(input("Enter next matrix whose inverse is to be found!"))+6

        