# Ex No: 1 - IMPLEMENTATION OF STRING MATCHING USING BRUTE FORCE APPROACH

def search(pat, txt):
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1
        if j == M:
            print("Pattern found at index", i)

txt = input("Enter Input String: ")
pat = input("Enter search pattern: ")
search(pat, txt)
