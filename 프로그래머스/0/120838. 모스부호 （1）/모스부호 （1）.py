def solution(letter):
    morse_code = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z'
    }
    
    morse_words = letter.split(' ')
    result = ''.join([morse_code[word] for word in morse_words])
    
    return result

print(solution(".... . .-.. .-.. ---"))
print(solution(".--. -.-- - .... --- -."))