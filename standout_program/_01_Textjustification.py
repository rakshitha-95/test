'''Given an array of strings words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.You should pack your words in a greedy
approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each
 line has exactly maxWidth characters.Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be
assigned more spaces than the slots on the right.For the last line of text, it should be left-justified and no
extra space is inserted between words.'''

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        width_left = maxWidth
        line = []
        res = []
        for i in words:
            if width_left - len(i) >= 0:
                line.append(i)
                width_left -= (len(i) + 1)
            else:
                width_left += 1
                if len(line) > 1:
                    extra_space = width_left // (len(line) - 1)
                    space_rem = width_left % (len(line) - 1)
                    for j in range(len(line) - 1):
                        line[j] += (extra_space + 1) * " "
                        if space_rem:
                            line[j] += " "
                            space_rem -= 1
                else:
                    line[0] = line[0] + " " * (maxWidth - len(line[0]))
                res.append("".join(line))
                line = [i]
                width_left = maxWidth - (len(i) + 1)
        for j in range(len(line) - 1):
            line[j] += " "
        last_line = "".join(line) + " " * (maxWidth - len("".join(line)))
        res.append(last_line)
        return res


if __name__ == "__main__":
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))