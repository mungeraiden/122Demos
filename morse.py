# Aiden Munger
# CPSC 122-01
# Intro to Python Lab
# 1/15/26
# Converts English to Morse Code or vice versa

english_morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}

def load_file(filename: str) -> list[str]:
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()
    return lines

def convert_english_to_morse(lines: list[str]) -> str:
    converted_texts = ""

    for line in lines:
        line = line.upper()
        print(repr(line))

        for char in line:
            print(repr(char))
            
            if char in english_morse_dict:
                converted_texts += english_morse_dict[char] + " " # Space to seperate morse strings
            elif char == " " or "\n":
                converted_texts += char
            else:
                print(f"Unrecognized character.")


    return converted_texts

def convert_morse_to_english(lines: list[str]):
    pass


def main():
    print("Enter -m for english to morse and -t for morse to english.\nFollow your command with the input file name and output filename.\CMD>", end="")

    user_str = "-m english.txt morse.txt"  # Example input for testing
    args = user_str.split(" ")
    conversion_type, infile_name, outfile_name = args
    lines = load_file(infile_name)

    print(lines)

    if conversion_type == "-m":
        converted_lines = convert_english_to_morse(lines)
        print("Converted Lines: ", converted_lines)
    elif conversion_type == "-t":
        pass
        converted_lines = convert_morse_to_english(lines)

main()
