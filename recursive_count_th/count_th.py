'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0

    def count_th_inner(word):
        nonlocal count
        # Check if 'th' is in word
        if 'th' in word:
            # Find index of substring and slice word
            th_index = word.find('th')
            word = word[th_index + 2:]
            count += 1

            # Pass new word into function
            return count_th_inner(word)
            # Else return the count
        else:
            return count

    return count_th_inner(word)
