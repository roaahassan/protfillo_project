function editTimetable(id, day, time, subject) {
    document.getElementById('tId').value = id;
    document.getElementById('day').value = day;
    document.getElementById('time').value = time;
    document.getElementById('subject').value = subject;
    document.querySelector('button[name="create"]').setAttribute('name','update');
}