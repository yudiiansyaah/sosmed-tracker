from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama and reset colors after each print

def print_banner(text):

    font = {
        'Y': [
            'Y   Y',
            ' Y Y ',
            '  Y  ',
            '  Y  ',
            '  Y  '
        ],
        'U': [
            'U   U',
            'U   U',
            'U   U',
            'U   U',
            ' UUU '
        ],
        'D': [
            'DDDD ',
            'D   D',
            'D   D',
            'D   D',
            'DDDD '
        ],
        'S': [
            ' SSSS',
            'S   S',
            ' SSSS',
            'S   S',
            'SSSS '
        ],
        'T': [
            'TTTTT',
            '  T  ',
            '  T  ',
            '  T  ',
            '  T  '
        ],
        'R': [
            'RRRR ',
            'R   R',
            'RRRR ',
            'R  R ',
            'R   R'
        ],
        'A': [
            ' AAA ',
            'A   A',
            'AAAAA',
            'A   A',
            'A   A'
        ],
        'C': [
            ' CCCC',
            'C    ',
            'C    ',
            'C    ',
            ' CCCC'
        ],
        'K': [
            'K   K',
            'K  K ',
            'KKK  ',
            'K  K ',
            'K   K'
        ],
        'E': [
            'EEEEE',
            'E    ',
            'EEEEE',
            'E    ',
            'EEEEE'
        ],
         '.': [
           '   ',
          '   ',
          ' . ',
          '   ',
           '   '
        ],
        '\'': [
           '  ',
           '\'  ',
           '   ',
           '   ',
           '   '
        ],
        ' ': [
            '   ',
            '   ',
            '   ',
            '   ',
            '   '
        ]
    }
    
    lines = ['' for _ in range(5)]

    for char in text.upper():
        if char in font:
            for i, line in enumerate(font[char]):
                lines[i] += Fore.GREEN + line + Style.RESET_ALL + " "
        else:
             for i in range(5):
               lines[i] += "    "

    for line in lines:
        print(line)

if __name__ == "__main__":
    banner_text = "YUD'S TRACKER"
    print_banner(banner_text)