'''Given an array of strings words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.You should pack your words in a greedy
approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each
 line has exactly maxWidth characters.Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be
assigned more spaces than the slots on the right.For the last line of text, it should be left-justified and no
extra space is inserted between words.'''

def fullJustify(words, L):
    result = []

    i = 0
    while i < len(words):
        # count words in one line
        size, begin = 0, i
        while i < len(words):
            if size == 0:
                newsize = len(words[i])
            else:
                newsize = size + len(words[i]) + 1
            if newsize <= L:
                size = newsize
            else:
                break
            i += 1

        # count space number
        spaceCount = L - size
        if i - begin - 1 > 0 and i < len(words):
            everyCount = spaceCount / (i - begin - 1) + 1
            spaceCount %= i - begin - 1
        else:
            everyCount = 1

        # add space
        j = begin
        while j < i:
            if j == begin:
                s = words[j]
            else:
                s += ' ' * everyCount
                if spaceCount > 0 and i < len(words):
                    s += ' '
                    spaceCount -= 1
                s += words[j]
            j += 1
        s += ' ' * spaceCount
        result.append(s)

    return result
words="#Easy-to-learn Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly."
L=15
print(fullJustify(words, L))