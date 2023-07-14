import os

def get_all_words() -> list[str]:
    """
    Gets all words in system dictionary
    :return: list of words as [str]
    """
    os.chdir("/usr/share/dict")
    with open("words") as f:
        words = list(filter(lambda x: len(x) > 0, f.read().split("\n")))
    return words


def starts_with(letter: str, words: list[str]) -> int:
    """
    Counts the number of words in the dict starting with the given letter
    :param letter: str
    :return: count (int)
    """
    ct = 0
    for word in words:
        if word[0] == letter:
            ct += 1
    return ct


def find_anagrams(word: str, word_dict: list[str]) -> list[str]:
    """
    Searches dictionary for all anagrams of a given word
    Example:
        word = "cat" | returns { "act" }
    :param word as str
    :return: set of anagrams as set[str]
    """
    return {possibility for possibility in enumerate_possibilities([char for char in word]) if possibility in word_dict and possibility != word}


def enumerate_possibilities(letters: list[str]) -> list[str]:
    """
    Enumerates all possible word configurations of a list of letters
    Example:
        letter = "c-a-t" | returns { "cat", "cta", "act", "atc", "tca", "tac" }
    :param letters as str
    :return: list of strings as set[str]
    """
    print(f"[enumerate] Letters: {letters}")
    if len(letters) == 1:
        return letters[0]
    else:
        return [word
                for letter in letters
                for word in add_words_to_letter(letter, enumerate_possibilities(remove_letter(letter, letters)))]


def remove_letter(letter: str, letter_list: list[str]) -> list[str]:
    """
    Removes the letter from the list of letters
    :param letter
    :param letter_list
    :return: list of letters w/ first instance of the specified letter removed
    """
    print(f"[remove_letter] letter: {letter} | list: {letter_list}")
    l = letter_list.copy()
    l.remove(letter)
    print(l)
    return l


def add_words_to_letter(letter: str, words: list[str]) -> list[str]:
    """
    Given a letter and a list of words, adds '{letter}{word-1}, ...'
    Example:
        letter: a, words: ['bc', 'cb'] | returns ['abc', 'acb']
    :param letter:
    :param words:
    :return: list of words
    """
    print(f"[add_words] letter: {letter} | words: {words}")
    if type(words) is not list:
        words = [words]
    print([letter+word for word in words])
    return [letter+word for word in words]


def insert_letter(letter: str, word: str, used: list[str]) -> list[str]:
    """
    Inserts the letter into all given words at beginning, end, & in between letters
    Example:
        letter: "a", word: "bc" | returns ["abc", "bac", "bca"]
        letter: "a", word: "bcd" | returns ["abcd", "bacd", "bcad", "bcda"]
    :param letter as char
    :param word: list of words as [str]
    :return: list of words as [str]
    """
    print(f"[insert_letter] letter: {letter} | word: {word} | used: {used}")
    if len(word) == 0:
        return [used+letter]
    else:
        if len(used) == 0:
            return [letter + word] + insert_letter(letter, word[1:], word[0])
        else:
            return [used+letter+word] + insert_letter(letter, word[1:], used+word[0])

def main():
    d = get_all_words()
    while True:
        ag = find_anagrams(input("Enter a word: "), d)
        print(f"\n\n Anagrams: {[w for w in ag]}")

main()