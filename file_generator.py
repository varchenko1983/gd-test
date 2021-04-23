import string
import random


def generate_file(file_name='test.txt', lines_count=10000, string_len=25):
    f = open(file_name, 'w')

    for i in range(lines_count):
        random_string = generate_string(string_len)
        f.write(random_string)
        f.write('\n')

    f.close()


def generate_string(num_letters=10) -> str:
    ascii_letters = string.ascii_letters
    letters = []

    for i in range(num_letters):
        letter = random.choice(ascii_letters)
        letters.append(letter)

    return ''.join(letters)


if __name__ == "__main__":
    generate_file(lines_count=100, string_len=50)


