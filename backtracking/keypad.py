# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

ans = []
keydic = {
   '2': "abc", '3': "def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz" 
}

digits = input()

if not digits:
    print([])


def back(index, path):
    if len(path) == len(digits):
        ans.append(path)
        return

    for i in range(index, len(digits)):
        for j in keydic[digits[i]]:
            back(i + 1, path + j)


back(0, "")
print(ans)