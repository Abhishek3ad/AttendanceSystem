import random
import string

def generate_unique_codes(n):
    codes = set()
    while len(codes) < n:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        codes.add(code)
    return list(codes)

def main():
    num_students = int(input("Enter the number of students present: "))
    codes = generate_unique_codes(num_students)
    print("Generated Codes:")
    for code in codes:
        print(code)
    
    # Save codes to a file
    with open('codes.txt', 'w') as file:
        for code in codes:
            file.write(code + "\n")

if __name__ == "__main__":
    main()
