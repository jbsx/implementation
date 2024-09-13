import sys

if len(sys.argv) != 3:
    print("Error: Expected 2 arguments")
    sys.exit()
arg1 = sys.argv[1]
arg2 = sys.argv[2]

#insert at idx
def iidx(at, og, ins):
    return og[:at] + ins + og[at:]

#______________________________________________

def longest_common_substr(one, two):
    arr = [[0] * len(one) for _ in range(len(two))]
    
    def lcs(i, j):
        if i >= len(one) or j >= len(two):
            return 0
        elif one[i] == two[j]:
            bruh = 1 + lcs(i+1, j+1)
            arr[j][i] = bruh
            return bruh
        else:
            return max(lcs(i, j+1), lcs(i+1, j))

    curr = lcs(0,0)
    res = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == curr:
                res += one[j]
                curr -= 1

    return res

def diff(og, new):
    lcs = longest_common_substr(og,new)

    curr = 0
    res1 = ""
    res2 = ""
    for i in lcs:
        while curr < len(og):
            if og[curr] != i:
                res1 += og[curr]
                res2 += "-"
                curr += 1
            else:
                res1 += i
                res2 += " "
                curr += 1
                break

    curr = 0
    for i in lcs:
        while curr < len(new):
            if new[curr] != i:
                res1 = iidx(curr, res1, new[curr])
                res2 = iidx(curr, res2, "+")
                curr += 1
            else:
                curr += 1
                break

    return (res1, res2)


bruh = diff(arg1, arg2)
print(bruh[0])
print(bruh[1])
