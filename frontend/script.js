document.getElementById('generate-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const numStudents = document.getElementById('num_students').value;

    fetch('https://<your-firebase-functions-url>/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ num_students: numStudents })
    })
    .then(response => response.json())
    .then(data => {
        alert('Codes generated successfully');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('claim-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const studentCode = document.getElementById('student_code').value;

    fetch('https://<your-firebase-functions-url>/claim', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ student_code: studentCode })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Attendance claimed successfully');
        } else {
            alert('Invalid or already used code');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
