import sys
import time
def animate_ascii(ascii_art):
    for line in ascii_art.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.003)  # Adjust the delay as needed
        sys.stdout.write('\n')
        time.sleep(0.003)  # Add an extra delay between lines

# ASCII art
ascii_art = """\x1b[34m
█▀▄▀█ █▀█ █▄▄ █ █░░ █▀▀
█░▀░█ █▄█ █▄█ █ █▄▄ ██▄

█▄░█ █░█ █▀▄▀█ █▄▄ █▀▀ █▀█
█░▀█ █▄█ █░▀░█ █▄█ ██▄ █▀▄

█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
						╔═══════════════════════╗
║ᶜʳᵉᵃᵗᵉᵈ ᵇʸ ᶜʸᵇᵉʳ ᵖˢʸᶜʰᵒ║
╚═══════════════════════╝
"""

# Animate the ASCII art
animate_ascii(ascii_art)
time.sleep(0.009)
def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(f"\r\x1b[32mLoading: {animation[i % len(animation)]}")
        sys.stdout.flush()
    sys.stdout.write('\n')  # Move to the next line after the animation
    sys.stdout.flush()
print("\x1b[33m")
def generate_combinations(operator_code):
    combinations = []
    for i in range(100000, 1000000):  # Generate 6-digit numbers
        combination = operator_code + str(i)
        combinations.append(combination)  
    return combinations

def add_last_two_digits(combinations, last_two_digits):
    return [combination + last_two_digits for combination in combinations]

def get_last_two_digits():
    while True:
        try:
            last_two_digits = input("\nEnter the last two digits of the mobile number: ")
            if len(last_two_digits) != 2 or not last_two_digits.isdigit():
                raise ValueError("Please enter exactly two digits.")
            return last_two_digits
        except ValueError as e:
            print(e)

def search_number(combinations, search_query):
    search_results = [number for number in combinations if search_query in number]
    return search_results

def get_operator_code(operator_choice):
    operator_codes = {
        1: '017',  # Grammen Phone
        2: '018',  # Robi
        3: '013',  # Grameen Phone
        4: '016',  # Airtel
        5: '019',  # Banglalink
        6: '015'   # Teletalk
    }
    return operator_codes.get(operator_choice, None)

# Print the choice bar for the user to select the operator
print("Choose the operator:")
print("1. Grammen Phone(017)")
print("2. Robi(018)")
print("3. Grameen Phone(013)")
print("4. Airtel(016)")
print("5. Banglalink(019)")
print("6. Teletalk(015)")

# Get the user's choice for the operator
while True:
    operator_choice = input("\n\nEnter your choice: ")
    if operator_choice.isdigit() and 1 <= int(operator_choice) <= 6:
        operator_code = get_operator_code(int(operator_choice))
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

# Generate all combinations of numbers with the selected operator code
combinations = generate_combinations(operator_code)

# Get the last two digits from the user
last_two_digits = get_last_two_digits()

# Add last two digits to each combination
combinations_with_last_two_digits = add_last_two_digits(combinations, last_two_digits)

# Print all generated combinations
print("\nAll generated combinations:")
for combination in combinations_with_last_two_digits:
    print("\x1b[32m", combination)

# Ask the user whether to search or save the results as a text file
while True:
    choice = input("\n\x1b[33mDo you want to search for a specific number or save the results as a text file? (search/save): ").lower()
    if choice == 'search':
        # Search for numbers based on user input
        search_query = input("\n\x1b[34mEnter some digits to search for: ")
        print("\n\x1b[32mSearching...")
        loading_animation()
        search_results = search_number(combinations_with_last_two_digits, search_query)

        # Print search results
        print("\n\x1b[32mSearch results:")
        for result in search_results:
            print(result)
        break
    elif choice == 'save':
        # Save results to a text file
        filename = input("\n\x1b[33mEnter the filename to save the results: ")
        with open(filename + ".txt", "w") as file:
            for result in combinations_with_last_two_digits:
                file.write(result + "\n")
        print("\x1b[32mResults saved successfully as", filename + ".txt")
        break
    else:
        print("\x1b[31mInvalid choice. Please enter 'search' or 'save'.")