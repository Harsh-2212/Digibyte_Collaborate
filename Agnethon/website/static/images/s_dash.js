let courses = [];

function addCourse() {
    const name = document.getElementById('name').value;
    const course = document.getElementById('courses').value;
    const grade = parseFloat(document.getElementById('grades').value);

    if (name && course && grade && !isNaN(grade)) {
        courses.push({ name: course, grade: grade });
        updateCoursesList();
        calculateGPA();
    } else {
        alert('Please enter valid data for the course!');
    }
}

function updateCoursesList() {
    const list = document.getElementById('coursesList');
    list.innerHTML = '';
    courses.forEach(course => {
        const li = document.createElement('li');
        li.textContent = `${course.name}: ${course.grade}`;
        list.appendChild(li);
    });
}

function calculateGPA() {
    let totalCredits = 0;
    let totalGradePoints = 0;

    courses.forEach(course => {
        totalCredits += 1; // assuming each course is 1 credit
        totalGradePoints += course.grade;
    });

    const gpa = totalGradePoints / totalCredits;

    document.getElementById('gpaValue').textContent = gpa.toFixed(2);
}
