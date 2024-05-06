
document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('reservationForm');
    let dateInput = document.getElementById('id_date');
    
    // Set the minimum allowed date to today
    let today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
    
    form.addEventListener('submit', function(event) {
        let selectedDate = new Date(dateInput.value);
        let currentDate = new Date(today);
        
        // Prevent form submission if the selected date is in the past
        if (selectedDate < currentDate) {
            event.preventDefault();
            alert('Date cannot be in the past.');
        }
    });
});

// });

// function confirmDelete()
// {
//     return confirm("Are you sure you want to deletereservation?");
// }