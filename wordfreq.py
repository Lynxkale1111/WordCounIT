def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1

            ## if we skipped past the end of our current line, we stop processing our current line.
            # if we don't include this we get errors when running test.py
            if start >= len(line):
                break

            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
                start = end

            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end].lower())
                start = end
            else:
                words.append(line[start].lower())
                start += 1

    return words

def countWords(words, ignore):
    wdict = {}
    ignoreset = set()
    for wd in ignore:
        ignoreset.add(wd)
    for wd in words:
        if wd in ignoreset:
            continue
        wdict[wd] = wdict.get(wd, 0) + 1
    return wdict

def printTopMost(words, n):
    sortedWords = sorted(words.items(), key=lambda x: x[1], reverse=True)[:n]

    for word in sortedWords:
        print(word[0].ljust(20) + str(word[1]).rjust(5))
