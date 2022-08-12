source = 'This is a book.'
pattern = 'is'

def bruteforce(pattern, source):
    for idx in range(len(source)-len(pattern)+1):
        # pattern의 처음부터 윈도우 문자열과 비교
        for j in range(len(pattern)):
            if source[idx+j] != pattern[j]:
                break
        else:
            return idx
    else:
        return -1

print(bruteforce(pattern, source))
