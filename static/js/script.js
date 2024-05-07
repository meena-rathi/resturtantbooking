


// document.addEventListener('DOMContentLoaded', function() {
//     console.log('DOMContentLoaded event fired.'); 
//     let form = document.getElementById('booking-form');
//     let dateInput = document.querySelector('#id_date');

//     if (!dateInput) {
//         console.log('Date input:', dateInput);
//         console.error("Element with ID 'id_date' not found.");
//         return; 
//     }

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded event fired.');

    document.body.addEventListener('input', function(event) {
        console.log('Event target:', event.target);
        if (event.target.id === 'id_date') {
            handleDateInput(event.target);
        }
    });

    function handleDateInput(dateInput) {
        let form = document.getElementById('booking-form'); // Check if the ID is correct
        if (!form) {
            console.error("Booking form not found.");
            return;
        }

        console.log('Form:', form); // Moved inside the function
        console.log('Date Input:', dateInput); // Moved inside the function

        let today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('value', today);
        dateInput.setAttribute('min', today);


        form.addEventListener('submit', function(event) {
            let selectedDate = new Date(dateInput.value);
            let currentDate = new Date(today);

            // Prevent form submission if the selected date is in the past
            if (selectedDate < currentDate) {
                event.preventDefault();
                alert('Date cannot be in the past.');
            }
            const emailInput = form.querySelector('#id_email').value.trim().toUpperCase();
            const existingEmails = document.querySelectorAll('.existing-email');
            for (let i = 0; i < existingEmails.length; i++) {
                if (existingEmails[i].innerText.trim().toUpperCase() === emailInput) {
                    event.preventDefault();
                    showAlert('You already have a reservation with this email.');
                    return;
                }
            }
        });
    }

    var deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default form submission
    
            var bookingId = this.getAttribute('data-booking-id');
            var deleteForm = document.getElementById('delete-form-' + bookingId);
            console.log('Delete form:', deleteForm); // Move the log here
            if (deleteForm) {
                var confirmation = confirmDelete();
                if (confirmation) {
                    deleteForm.submit();
                }
            } else {
                console.error('Delete form not found for booking ID:', bookingId);
            }
        });
    });
    
    function confirmDelete() {
        return confirm("ARE YOU SURE YOU WANT TO DELETE THIS RESERVATION?".toUpperCase());
    }
});