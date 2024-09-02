document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('add').addEventListener('click', function () {
        const time = prompt("Enter the time (e.g., 09:00 - 10:00):");
        if (time) {
            const day = prompt("Enter the day (e.g., Monday):");
            if (day) {
                fetch('/index.php?action=add', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({ time, day })
                }).then(response => response.text())
                  .then(() => location.reload());
            }
        }
    });

    document.querySelectorAll('.edit').forEach(button => {
        button.addEventListener('click', function () {
            const time = button.getAttribute('data-time');
            const day = button.getAttribute('data-day');
            const newDay = prompt("Edit the day:", day);
            if (newDay) {
                fetch('/index.php?action=edit', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({ time, day, newDay })
                }).then(response => response.text())
                  .then(() => location.reload());
            }
        });
    });

    document.querySelectorAll('.delete').forEach(button => {
        button.addEventListener('click', function () {
            const time = button.getAttribute('data-time');
            const day = button.getAttribute('data-day');
            if (confirm(`Are you sure you want to delete ${day} at ${time}?`)) {
                fetch('/index.php?action=delete', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: new URLSearchParams({ time, day })
                }).then(response => response.text())
                  .then(() => location.reload());
            }
        });
    });
});