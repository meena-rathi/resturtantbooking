
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

    // Function to handle form submission
    function handleFormSubmission(event) {
        event.preventDefault(); // Prevent default form submission

        // Find the form element
        var form = document.getElementById('booking-form');
        if (!form) {
            console.error("Booking form not found.");
            return;
        }

        // Validate all fields
        var isValid = validateForm(form);

        if (isValid) {
            // Serialize form data
            var formData = new FormData(form);

            // Send form data asynchronously to backend view
            fetch('/reservation/', {
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
                if (data.exists) {
                    // Display JavaScript alert
                    showAlert('You already have a reservation with this email.');
                } else {
                    window.location.href = '/view_reservation.html';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }

    function validateForm(form) {
        var isValid = true;

        // Validate email
        var emailField = form.elements['email'];
        var email = emailField.value.trim();
        var emailError = document.getElementById('email-error');
        var emailValidationResult = validateEmail(email);
        if (emailValidationResult !== '') {
            isValid = false;
            emailError.textContent = emailValidationResult;
            emailError.style.color = 'red'; // Display error in red
        } else {
            emailError.textContent = '';
        }

        // Validate contact number
        var contactNumberField = form.elements['contact_number'];
        var contactNumber = contactNumberField.value.trim();
        var contactNumberError = document.getElementById('contact-number-error');
        if (contactNumber.includes(' ') || !contactNumber.match(/^\d+$/) || contactNumber.length < 10) {
            isValid = false;
            contactNumberError.textContent = 'Invalid contact number.';
            contactNumberError.style.color = 'red'; // Display error in red
        } else {
            contactNumberError.textContent = '';
        }

        // Validate number of people
        var numberPeopleField = form.elements['number_people'];
        var numberPeople = numberPeopleField.value.trim();
        var numberPeopleError = document.getElementById('number-people-error');
        if (!numberPeople.match(/^\d+$/) || parseInt(numberPeople) <= 0) {
            isValid = false;
            numberPeopleError.textContent = 'Number of people must be a positive number.';
            numberPeopleError.style.color = 'red'; // Display error in red
        } else {
            numberPeopleError.textContent = '';
        }

        // Validate date
        var dateField = form.elements['date'];
        var date = dateField.value;
        var dateError = document.getElementById('date-error');
        var today = new Date().toISOString().split('T')[0];
        if (date < today) {
            isValid = false;
            dateError.textContent = 'The reservation date cannot be in the past.';
            dateError.style.color = 'red'; // Display error in red
        } else {
            dateError.textContent = '';
        }

        // Validate time
        var timeField = form.elements['time'];
        var time = timeField.value.trim();
        var timeError = document.getElementById('time-error');
        if (time === '') {
            isValid = false;
            timeError.textContent = 'Time is required.';
            timeError.style.color = 'red'; // Display error in red
        } else {
            timeError.textContent = '';
        }

        return isValid;
    }

    function validateEmail(email) {
        var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        var allowedDomains = ['gmail.com', 'yahoo.com', 'hotmail.com']; // Add allowed domains here

        if (!re.test(email)) {
            return 'Invalid email format'; // Return error message for incorrect format
        }

        var domain = email.split('@')[1];
        if (!allowedDomains.includes(domain.toLowerCase())) {
            return 'Invalid email domain'; // Return error message for invalid domain
        }

        return ''; // Empty string means email is valid
    }

    // Add event listener for form submission
    var form = document.getElementById('booking-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmission);
    }

    // Event listener for input on the email field
    var emailField = document.getElementById('id_email');
    if (emailField) {
        emailField.addEventListener('input', function(event) {
            var email = event.target.value.trim();
            var emailError = document.getElementById('email-error');

            var emailValidationResult = validateEmail(email);
            if (emailValidationResult !== '') {
                emailError.textContent = emailValidationResult;
                emailError.style.color = 'red'; // Display error in red
            } else {
                emailError.textContent = '';
            }
        });
    }

    // Event listener for input on the contact number field
    var contactNumberField = document.getElementById('id_contact_number');
    if (contactNumberField) {
        contactNumberField.addEventListener('input', function(event) {
            var contactNumber = event.target.value.trim();
            var errorSpan = document.getElementById('contact-number-error');

            // Check if the contact number has spaces
            if (contactNumber.includes(' ')) {
                errorSpan.textContent = 'Spaces are not allowed in the contact number.';
                errorSpan.style.color = 'red';
                return;
            }

            // Check if the contact number consists only of digits
            if (!contactNumber.match(/^\d+$/)) {
                errorSpan.textContent = 'Contact number must contain only digits.';
                errorSpan.style.color = 'red';
                return;
            }

            // Check if the contact number has less than 10 digits
            if (contactNumber.length < 10) {
                errorSpan.textContent = 'Contact number is incomplete.';
                errorSpan.style.color = 'red';
                return;
            }

            // If all validations pass, clear any previous error message
            errorSpan.textContent = '';
        });
    }

    // Event listener for input on the date field
    document.body.addEventListener('input', function(event) {
        if (event.target.id === 'id_date') {
            handleDateInput(event.target);
        }
    });

    // Function to handle input on the date field
    function handleDateInput(dateInput) {
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