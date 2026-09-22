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
