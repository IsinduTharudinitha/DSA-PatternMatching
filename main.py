import regExpression as regular


if __name__ == '__main__':
    text = open("text.txt", 'r')
    pattern = open("pattern.txt", 'r')
    output = open("patternmatch.output", 'w')

    String = text.readline().strip()
    Pattern = pattern.readline().strip()

    output.writelines(str(regular.search(String, Pattern)))

    text.close()
    pattern.close()
    output.close()

