
def answer (document, searchTerms):
    """
    Altered from a "minimum [character] window" solution by liborm on Stack
    Overflow, page
    http://stackoverflow.com/questions/32453728/find-minimum-window-substring
    """
    # Okay, let's try a different approach. A little cleaner, hopefully kinder
    # on memory. Get a head and tail, loop through looking for terms and just
    # move the substring indeces around as needed.
    from collections import Counter
    words = document.split (' ')

    def substrings (word_list, search_terms):
        target_count = Counter(search_terms)
        test_count = Counter()
        head = enumerate (word_list)
        tail = enumerate (word_list)

        for i_head, word_head in head:
            test_count [word_head] += 1

            while not target_count - test_count:
                i_tail, word_tail = tail.next()
                yield (i_tail, i_head +1)
                test_count[word_tail] -= 1

    def smallest_substring (word_list, search_terms):
        min_len = len (word_list) + 1
        min_start, min_end = None, None

        for start, end in substrings (word_list, search_terms):
            if end - start < min_len:
                min_start, min_end = start, end
                min_len = end - start

        return (min_start, min_end)

    head, tail = smallest_substring (words, searchTerms)
    result = ""
    for i in range (head, tail):
        result += words[i]
        if i < tail - 1:
            result += " "
    return result
