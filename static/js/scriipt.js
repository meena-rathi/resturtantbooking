
// document.addEventListener('DOMContentLoaded', function() {
//     console.log('DOMContentLoaded event fired.'); 
//     let form = document.getElementById('booking-form');
//     let dateInput = document.querySelector('#id_date');

//     if (!dateInput) {
//         console.log('Date input:', dateInput);
//         console.error("Element with ID 'id_date' not found.");
//         return; 
//     }

function showAlert(message) {
    alert(message);
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded event fired.');

    // Function to handle form submission for edit form
    function handleEditFormSubmission(event) {
        event.preventDefault(); // Prevent default form submission

        // Find the form element
        var form = document.getElementById('edit-booking-form');
        if (!form) {
            console.error("Edit booking form not found.");
            return;
        }

        // Validate all fields
        var isValid = validateForm(form);

        if (isValid) {
            // Serialize form data
            var formData = new FormData(form);

            // Validate email address
            var emailField = form.elements['email'];
            var email = emailField.value.trim();
            var emailError = document.getElementById('email-error');
            var emailErrorMessage = validateEmail(email);
            if (emailErrorMessage) {
                // Display error message for invalid email
                emailError.textContent = emailErrorMessage;
                return; // Stop form submission if email is invalid
            } else {
                emailError.textContent = ''; // Clear previous error message
            }

            // Send form data asynchronously to backend view
            fetch('/reservation/edit/', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = '/view_reservation.html';
                } else {
                    console.error('Edit form submission failed:', data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }

    function validateForm(form) {
        var isValid = true;
        // Add validation for other fields here
        
        return isValid;
    }

    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        var allowedDomains = ['gmail.com', 'yahoo.com', 'hotmail.com']; // Add allowed domains here
    
        if (!re.test(email)) {
            return 'Invalid email format'; // Return error message for incorrect format
        }
    
        var domain = email.split('@')[1];
        if (!isValidDomain(domain)) {
            return 'Invalid email domain'; // Return error message for invalid domain
        }
    
        return ''; // Empty string means email is valid
    }

    function isValidDomain(domain) {
        var allowedDomains = ['gmail.com', 'yahoo.com', 'hotmail.com']; // Example allowed domains
        return allowedDomains.includes(domain.toLowerCase());
    }

    // Add event listener for edit booking form submission
    var editForm = document.getElementById('edit-booking-form');
    if (editForm) {
        editForm.addEventListener('submit', handleEditFormSubmission);
    }

    // Other event listeners and functions

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
