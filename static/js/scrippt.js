


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

    // Function to handle form submission
    function handleFormSubmission(event) {
        event.preventDefault(); // Prevent default form submission

        // Find the form element
        var form = document.getElementById('booking-form');
        if (!form) {
            console.error("Booking form not found.");
            return;
        }

        // Serialize form data
        var formData = new FormData(form);

        // Send form data asynchronously to backend view
        fetch('/reservation/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                // Display JavaScript alert
                alert('You already have a reservation with this email.');
            } else {
                window.location.href = '/view_reservation.html';
                
                //form.submit();
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Add event listener for form submission
    var form = document.getElementById('booking-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmission);
    } else {
        console.error("Booking form not found.");
    }


    // Function to display alert message
    function showAlert(message) {
        alert(message);
    }

    // Event listener for input on the date field
    document.body.addEventListener('input', function(event) {
        console.log('Event target:', event.target);
        if (event.target.id === 'id_date') {
            handleDateInput(event.target);
        }
    });

    // Function to handle input on the date field
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
    }

    // Event listener for delete buttons
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

    // Function to confirm deletion
    function confirmDelete() {
        return confirm("ARE YOU SURE YOU WANT TO DELETE THIS RESERVATION?".toUpperCase());
    }
});