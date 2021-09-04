def convert_to_square(arr, n):
    for row in arr:
        yield row + [1] * (n - len(row))
    for i in range(len(arr), n):
        yield [1]*n

def get_Sum_Diagonal(arr,m, n):

    mysum = -1

    size = max(m,n)
    sqr_mat = list(convert_to_square(arr, size))
    #print(sqr_mat)

    diagonal_ele = [sqr_mat[i][i] for i in range(size)]

    #one_d = [j for row in sqr_mat for j in row]
    one_d = sum(sqr_mat, [])

    shorlist = []
    for ele in diagonal_ele:
        if ( one_d.count(ele) - diagonal_ele.count(ele) ) > 1:
            shorlist.append(ele)

    mysum = sum(shorlist)
    return mysum


if __name__ == "__main__":
    m,n = list(map(int, input().split()))
    arr = []
    for i in range(m):
        row = list(map(int, input().split()))
        arr.append(row)

    res = get_Sum_Diagonal(arr, m,n)
    print(res)