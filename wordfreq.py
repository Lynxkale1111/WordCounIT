def tokenize(lines):
    #create an empty list that will hold our tokens
    words = []
    for line in lines:
        start = 0
        # we keep going until we have processed all characters in the line
        while start < len(line):
            # skips over spaces
            while start < len(line) and line[start] == " ":
                start += 1

            ## if we skipped past the end of our current line, we stop processing our current line.
            # if we don't include this we get errors when running test.py
            if start >= len(line):
                break

            # check if character is letter
            if line[start].isalpha():
                # create variable end to use as end index and set it equal to our starting index.
                end = start
                # incrementally advance end as long as we stay inside our current line and the character is still a letter.
                while end < len(line) and line[end].isalpha():
                    # counter variable, moving the end pointer 1 character ahead
                    end += 1
                # we use append to extract the complete word and store it using start and end as index.
                words.append(line[start:end].lower())
                # set our start for the next word to the end of the current
                start = end

            # check if character is digit
            elif line[start].isdigit():
                # create variable end to use as end index and set it equal to our starting index.
                end = start
                # incrementally advance end as long as we stay inside our current line and the character is still a digit.
                while end < len(line) and line[end].isdigit():
                    # counter variable, moving the end pointer 1 character ahead
                    end += 1
                # we use append to extract the complete word and store it using start and end as index.
                words.append(line[start:end].lower())
                # set our start for the next word to the end of the current
                start = end
            else:
                # append our symbol using start as index since symbol is only 1 character.
                words.append(line[start].lower())
                # counter variable, moving the start pointer 1 character ahead
                start += 1

    return words

def countWords(words, ignore):
    wdict = {}
    ignoredict = set()
    for wd in ignore:
        ignoredict.add(wd)
    for wd in words:
        if wd in ignoredict:
            continue
        wdict[wd] = wdict.get(wd, 0) + 1
    return wdict
