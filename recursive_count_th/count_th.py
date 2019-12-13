'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    matches = []
    # ** Define inner function to keep track of values in outer function **

    def count_th_inner(word):
        # Step 1: If 'th' is in the word, add word to outer array
        if 'th' in word:
            matches.append(word)
        # Step 2: Find index of 'th' in the word, and slice the word at that index + 2. Repeat Step 1.
            th_index = word.find('th')
            new_word = word[th_index + 2:]
            return count_th_inner(new_word)
        # Step 3: If 'th' not in word, return length of matches
        else:
            return len(matches)

    return count_th_inner(word)
