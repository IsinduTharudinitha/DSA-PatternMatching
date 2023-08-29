def traverse(String, Pattern, breaking_point, pi):
    if breaking_point > len(String) - len(Pattern):
        return False

    q = 0
    for i in range(len(Pattern)):
        if String[i + breaking_point] != Pattern[i]:
            break
        q += 1

    if q == len(Pattern):
        return True

    if q == 0:
        return traverse(String, Pattern, breaking_point + 1, pi)

    return traverse(String, Pattern, breaking_point + (q - pi[q - 1][1]), pi)

def kmp(Str, Pattern):
    pi = []
    for i in range(len(Pattern) + 1):
        postfix = []
        prefix = []
        maxLength = 0

        sub = "".join(Pattern[: i])
        for j in range(1, i):
            prefix.append(sub[: j])
            postfix.append(sub[i - j:])

        for j in range(len(prefix)):
            if prefix[j] in postfix:
                if len(prefix[j]) > maxLength:
                    maxLength = len(prefix[j])

        if i != 0:
            pi.append([Pattern[i - 1], maxLength])

    return traverse(Str, Pattern, 0, pi)



def startWith(Str, Pattern):
    if kmp(Str[: len(Pattern) - 1], "".join(Pattern[1:])):
        return True
    else:
        return False



def endsWith(Str, Pattern):
    if kmp(Str[len(Str) - len(Pattern) + 1:], "".join(Pattern[0: len(Pattern) - 1])):
        return True and search(Str, "".join(Pattern[:len(Pattern) - 1]))
    else:
        return False


def start_with_and_ends_with(Str, Pattern):
    if kmp(Str, "".join(Pattern[1: len(Pattern) - 1])) and len(Str) == len(Pattern) - 2:
        return True
    else:
        return False


def search(Str, Pattern):

    if any(i == '|' for i in Pattern):
        return search(Str, Pattern.split('|')[0]) or search(Str, Pattern.split('|')[1])


    elif Pattern[0] == "^" and Pattern[-1] == "$":
        return start_with_and_ends_with(Str, Pattern)


    if Pattern[0] == "^":
        return startWith(Str, Pattern)


    elif Pattern[-1] == "$":
        return endsWith(Str, Pattern)

    return kmp(Str, Pattern)