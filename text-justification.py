"""
Given an array of strings words and a width maxWidth,
format the text such that each line has exactly maxWidth characters
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is,
pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

* Center justify single word lines, with extra spaces going to the right side
* Hyphenated words can be split up to fit across lines

Phase 1: Placing words on different lines and distributing the remaining space, left-aligned.

Phase 2: If you only have one word on a line, that word should be centered.

Phase 3: Hyphenated words should ideally be on the same line,
but if they don't fit, break them right after the hyphen character and follow the same rules as other words for the broken pieces.

"""

def justify(words, maxWidth):
    res = []
    i = 0
    n = len(words)

    while i < n:
        line_words = [] # track the words in current line
        line_length = 0
        j = i

        # Fill as many whole words as possible into the line
        while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
            line_length += len(words[j])
            line_words.append(words[j])
            j += 1
        
        # words[i:j] fits, words[j] does not fit

        # Check if words[j] is hyphenated and can be broken up
        if j < n and "-" in words[j]:
            parts = words[j].split("-")
            to_add = "" # string to try and add
            num_gaps = len(line_words)
            
            for k, part in enumerate(parts):
                # extend candidate to potentially add
                candidate = to_add
                candidate += part if k == len(parts) - 1 else part + "-"
                if line_length + len(candidate) + num_gaps > maxWidth:
                    # candidate exceeds limit
                    # leftover parts go back into words[j]
                    words[j] = "-".join(parts[k:])
                    break

                to_add = candidate # update string to add
            
            if to_add:
                line_words.append(to_add)
                line_length += len(to_add)

        # create line string out of line_words
        space_count = maxWidth - line_length
        num_gaps = len(line_words) - 1
        line = ""

        if j == n:
            # Last line: left-justified
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        elif num_gaps == 0:
            # Single word line: center justify
            word = line_words[0]
            left = space_count // 2
            right = space_count - left
            line = " " * left + word + " " * right
        else:
            # Fully justified line
            space_each = space_count // num_gaps
            extra = space_count % num_gaps
            for idx, w in enumerate(line_words):
                line += w
                if idx != len(line_words) - 1:
                    line += " " * space_each
                    if extra > 0:
                        line += " "
                        extra -= 1

        res.append(line)
        i = j
    
    print(res)

    return res



def run_tests(justifyText):
    # 1. Basic Multiple Words
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert justifyText(words, maxWidth) == expected

    # 2. Single Word Fits Exactly
    words = ["Perfect"]
    maxWidth = 7
    expected = ["Perfect"]
    assert justifyText(words, maxWidth) == expected

    # 3. Single Word Shorter than Line
    words = ["Short"]
    maxWidth = 7
    expected = ["Short  "]
    assert justifyText(words, maxWidth) == expected

    # 4. Hyphenated Word Split Incrementally
    words = ["ab-cde-fg", "word"]
    maxWidth = 10
    expected = [
        "ab-cde-fg ",  # built incrementally: ab- + cde-
        "word      "   # leftover goes to next line
    ]
    assert justifyText(words[:], maxWidth) == expected

    # 5. Last Line Left-Justified
    words = ["Last", "line", "is", "left", "justified"]
    maxWidth = 20
    expected = [
        "Last  line  is  left",
        "justified           "
    ]
    assert justifyText(words[:], maxWidth) == expected

    # 6. Multiple Hyphen Splits
    words = ["super-extra-mega-long", "text"]
    maxWidth = 8
    expected = [
        " super- ",
        " extra- ",
        " mega-  ",
        "  long  ",
        "text    "
    ]
    assert justifyText(words, maxWidth) == expected

    print("All tests passed!")


run_tests(justify)
