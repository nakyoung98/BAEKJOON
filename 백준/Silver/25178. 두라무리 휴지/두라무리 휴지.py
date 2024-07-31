import sys

input = sys.stdin.readline

VOWELS = set(["a", "e", "i", "o", "u"])


def solution(wordLength):
    word1 = input().rstrip()
    word2 = input().rstrip()

    result = compare(word1, word2)

    print(result)


def compare(word1, word2):
    result = "YES"

    word1ConsonantandVowel = [
        # 배열을 쓴 이유: 순서 중요 (배치 따지기 위함)
        [letter for letter in word1 if letter not in VOWELS],  # 자음
        # 딕셔너리를 쓴 이유, 순서 미중요, 각 모음의 개수만 중요
        getVowels(word1),  # 모음
    ]
    word2ConsonantandVowel = [
        [letter for letter in word2 if letter not in VOWELS],  # 자음
        getVowels(word2),  # 모음
    ]

    # 처음과 마지막 글자가 같아야함
    if word1[0] != word2[0] or word1[-1] != word2[-1]:
        result = "NO"
        return result

    # 자음은 자음끼리의 순서가 둘이 일치해야 함
    for letter1, letter2 in zip(word1ConsonantandVowel[0], word2ConsonantandVowel[0]):
        if letter1 != letter2:
            result = "NO"
            return result

    # 모음은 배치 순서는 상관없지만 가지고있는 모음의 종류와 개수는 같아야함 => 딕셔너리 개수 비교
    for vowel in VOWELS:
        if word1ConsonantandVowel[1][vowel] != word2ConsonantandVowel[1][vowel]:
            result = "NO"
            return result

    return result


def getVowels(word):
    result = {vowel: 0 for vowel in VOWELS}
    for letter in word:
        if letter in VOWELS:
            result[letter] += 1

    return result


wordLength = int(input())
solution(wordLength)
