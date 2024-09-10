def diff(one, two):
    arr =[[0] * len(one) for _ in range(len(two))]
    def lcs(i, j):
        if i >= len(one) or j >= len(two):
            return 0
        elif one[i] == two[j]:
            bruh = 1 + lcs(i+1, j+1)
            arr[i][j] = bruh
            return bruh
        else:
            return max(lcs(i, j+1), lcs(i+1, j))
    curr = lcs(0,0)
    res = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == curr:
                res += one[i]
                curr -= 1

    return res

print(diff("BHDEFCK", "ABCDEFK")) #Expected: BDEFK
