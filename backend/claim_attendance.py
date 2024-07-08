def load_codes():
    with open('codes.txt', 'r') as file:
        codes = file.read().splitlines()
    return set(codes)

def main():
    codes = load_codes()
    student_code = input("Enter your attendance code: ")
    if student_code in codes:
        print("Attendance claimed successfully!")
        # Remove the code so it cannot be reused
        codes.remove(student_code)
        with open('codes.txt', 'w') as file:
            for code in codes:
                file.write(code + "\n")
    else:
        print("Invalid or already used code!")

if __name__ == "__main__":
    main()
