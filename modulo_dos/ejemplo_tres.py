def palindrome3(word):
    resersed = word[::-1]

    if resersed == word:
        result = f'La palabra {word} es un palindromo'
        return result
    
    result = f'La palabra {word} no es un palindromo'
    return result


def palindrome2(word):
    reversed = word[::-1]

    if reversed == word:
        return True
    return False

def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False



if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindrome3(word)
    print(result)
    # if result is True:
    #     print('{} si es un palindromo'.format(word))
    # else:
    #     print('{} no es un palindromo'.format(word))