document.addEventListener('DOMContentLoaded', function() {
    $('#confirmDeleteBtn').on('click', function() {
    let dateInput = document.querySelector('input[type="date"]');
    if (dateInput) {
        let today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
}
});
});

function confirmDelete()
{
    return confirm("Are you sure you want to deletereservation?");
}