function editTimetable(id, day, srt_tim,end_tim, activity) {
    document.getElementById('id').value = id;
    document.getElementById('day').value = day;
    document.getElementById('stime').value = srt_tim;
    document.getElementById('etime').value = end_tim;
    document.getElementById('act').value = activity;
    document.querySelector('button[name="create"]').setAttribute('name','update');
}