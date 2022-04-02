def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
final_hangman = '''
       ┌--------┐
       |        |
       |        O
       |       -┼-
       |       ┌┴┐
       |                SORRY YOU'RE DEAD
    ___|___             
'''
colored_text = colored(255, 0, 0, final_hangman)
print(colored_text)

