
WORDS_FILE = './WORD.LST'


def anagrams(word):
    ''' Receives a word and looks for anagrams within the
        words list of the WORDS_FILE.
    '''

    if not word or word == '':
        raise Exception('Word not provided.')

    # `word` letters sorted alphabetically
    word_letters = sorted(word)
    # words to test
    words = [w.rstrip() for w in open(WORDS_FILE)]
    return filter(lambda x: sorted(x) == word_letters, words)


if __name__ == "__main__":
    print(anagrams('train'))
    print('--')
    print(anagrams('drive'))
    print('--')
    print(anagrams('python'))
