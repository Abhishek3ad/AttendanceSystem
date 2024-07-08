from flask import Flask, render_template, request, redirect, url_for, flash
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_unique_codes(n):
    codes = set()
    while len(codes) < n:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        codes.add(code)
    return list(codes)

def load_codes():
    try:
        with open('codes.txt', 'r') as file:
            codes = file.read().splitlines()
        return set(codes)
    except FileNotFoundError:
        return set()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_students = int(request.form['num_students'])
    codes = generate_unique_codes(num_students)
    
    with open('codes.txt', 'w') as file:
        for code in codes:
            file.write(code + "\n")
    
    flash('Codes generated successfully!')
    return redirect(url_for('index'))

@app.route('/claim', methods=['GET', 'POST'])
def claim():
    if request.method == 'POST':
        student_code = request.form['student_code']
        codes = load_codes()
        
        if student_code in codes:
            codes.remove(student_code)
            with open('codes.txt', 'w') as file:
                for code in codes:
                    file.write(code + "\n")
            flash('Attendance claimed successfully!')
        else:
            flash('Invalid or already used code!')
        
        return redirect(url_for('claim'))
    
    return render_template('claim.html')

if __name__ == '__main__':
    app.run(debug=True)
