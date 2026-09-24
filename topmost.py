import sys
import wordfreq
import urllib.request

def main(input_stop, input_content, words_to_print):

# get stopwords
    stop_words_file = open(input_stop, encoding="utf-8")

    stop_words = []
    for line in stop_words_file:
        stop_words.append(line.strip())

    stop_words_file.close()

# tokenize input
    if input_content[:7] == 'http://' or input_content[:8] == 'https://':
        response = urllib.request.urlopen(input_content)
        lines = response.read().decode("utf8").splitlines()
    else:
        content_file = open(input_content, encoding="utf-8")
        lines = []
        for line in content_file:
            lines.append(line.strip())
        content_file.close()
    content_words = wordfreq.tokenize(lines)

# count words
    word_count = wordfreq.countWords(content_words, stop_words)

# print top words
    wordfreq.printTopMost(word_count, words_to_print)


main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
