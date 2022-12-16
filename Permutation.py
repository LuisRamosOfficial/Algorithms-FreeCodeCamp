def permute(string, pocket=""):
    print(f"string: {string}, pocket: {pocket}")
    input()
    if len(string) == 0:
        print(pocket)
    else:
        for i in range((len(string))):
            print(f"i: {i}")
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            print(f"letter: {letter}, front: {front}, back: {back}")
            input()
            together = front + back
            print(f"together: {together}")
            input()
            permute(together, letter + pocket)

print(permute("ABC", ""))