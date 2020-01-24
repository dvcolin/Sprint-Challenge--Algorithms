'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    matches = []

    def count_th_inner(word):
        nonlocal matches
        # Check if 'th' is in word
        if 'th' in word:
            # If 'th' in word, append word to matches list
            matches.append(word)
            # Find index of substring and slice word
            th_index = word.find('th')
            word = word[th_index + 2:]

            return count_th_inner(word)
            # Else return the length of matches
        else:
            return len(matches)

    return count_th_inner(word)
