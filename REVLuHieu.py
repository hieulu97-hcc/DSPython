'''
# Name: Hieu Lu
# Date: March 16, 2026
# Module: 03REV - Review Python Fundamentals
# This program asks the user to enter a text string and then counts
# how many times each vowel appears in the text. It checks each character one by
# one and stores the vowel counts in a dictionary. After that, it calculates the
# total number of vowels found in the text. The program then prints a clear report
# that shows the count for A, E, I, O, and U, along with the total vowel count.
# I used functions, constants, loops, dictionaries, and selection statements to
# organize the program and make it easier to read.
'''

# CONSTANTS
TITLE = "Welcome to vowel counter program!"
PROMPT = "Enter any text: "
LINE = "-"
REPORT_TITLE = "VOWEL COUNT REPORT:"
VOWELS = "AEIOU"


'''
This function displays the title, asks the user to enter a text string, and converts the input to uppercase
so the program can count vowels consistently. Then it calls the function
that counts the vowels and receives both the dictionary and total count.
Finally, it calls the report function to display the results.
'''
def main():
    print(TITLE)
    print(LINE * len(TITLE))

    text = input(PROMPT).upper()

    vowel_dict, total = findVowelCount(text)
    generateReport(vowel_dict, total)


'''
This function accepts one text string as an argument. It creates a dictionary
to store the count for each vowel and uses a loop to check each character in
the text. If the character is one of the vowels, the function increases that
vowel's count and also increases the total vowel count. At the end, it returns
both the dictionary and the total count back to main.
'''
def findVowelCount(text):
    vowel_dict = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    total = 0

    for ch in text:
        if ch in vowel_dict:
            vowel_dict[ch] = vowel_dict[ch] + 1
            total = total + 1

    return vowel_dict, total


'''
Accepting the vowel dictionary and total vowel count as arguments.
It prints a formatted report that shows each vowel and its count in a clean
table style. After listing all vowel counts, it prints the total number of
vowels found in the entered text.
'''
def generateReport(vowel_dict, total):
    print()
    print(REPORT_TITLE)
    print("-" * 20)
    print(f'{"Vowel":<10}{"Count":>10}')
    print("-" * 20)

    for vowel in VOWELS:
        print(f'{vowel:<10}{vowel_dict[vowel]:>10}')

    print("-" * 20)
    print(f'{"Total":<10}{total:>10}')
    print("-" * 20)


main()