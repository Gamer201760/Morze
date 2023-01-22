# SUPER MEGA MORSE CODE DECODER AND ENCODER
# Данная программа сделана учениками Яндекс.Лицея Бикташевым Искандером и Азаматом

# Словарь для перевода из латиницы в азбуку Морзе
MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',  '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '.....',
    ' ': ' '
}

valid_characters = ('-', '.', ' ')


# Проверка текст на корректность
def check_text(text: str) -> bool:
    for i in text.upper():
        if i not in MORSE_CODE:
            return False
    return True


# Функция кодирования текта
def encode_to_morse(text: str) -> str:
    morse: list[str] = []
    for i in text.upper():
        morse.append(MORSE_CODE[i])  # Кодируются ТОЛЬКО буквы латинского алфавита и цифры
    return ' '.join(morse)  # Разделитель между буквами - 1 пробел, между словами - 3 пробела


def check_code(text: str) -> bool:
    for s in text:
        if s not in valid_characters:
            return False
    return True


# Функция декодирования текта
def decode_from_morse(code: str) -> str:
    code = code.split('   ')  # Бьём код по словам
    text = ''  # Тут будет хранится финальный текст
    for i in code:  # Бежим по словам
        for b in i.split():  # Бежим по буквам
            for s, c in MORSE_CODE.items():  # Бежим по словарю
                if b == c:  # Сравниваем
                    text += s  # Записываем
        text += ' '  # Пробел между словами
    return text  # Вернули предложение


# Функция main
def main():
    print('Добро пожаловать в минималистичный кодировщик латиницы в азбуку Морзе.')
    inp = input('Что хотите сделать? (закодировать - 1, декодировать - 2, выйти - 3)\n')
    while inp != '3':
        if inp == '1':
            text = input('Введите текст, который хотите закодировать:\n')
            while not check_text(text):
                text = input('Данный текст нельзя закодировать, введите другой:\n')
            print(f'Закодированный текст:\n{encode_to_morse(text)}')
        elif inp == '2':
            text = input('Введите текст, который хотите декодировать:\n')
            while not check_code(text):
                text = input('Данный текст нельзя декодировать, введите другой:\n')
            print(f'Декодированный текст:\n{decode_from_morse(text)}')
        else:
            print('Невозможно распознать комнаду.')
        inp = input('Что еще хотите сделать? (закодировать - 1, декодировать - 2, выйти - 3)\n')
    print('Пока!')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Пока!')
        exit()