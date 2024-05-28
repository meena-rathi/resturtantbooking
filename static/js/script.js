document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded event fired.');
    function handleFormSubmission(event) {
        event.preventDefault(); 
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
                var emailError = document.getElementById('email-error');
                if (data.exists) {
                    // Display error message in red
                    emailError.textContent = 'This email is already registered.';
                    emailError.style.color = 'red';
                } else {
                    window.location.href = '/view_reservation';
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

    function showAlert(message) {
        var alert = document.createElement('div');
        alert.className = 'alert alert-warning custom-alert alert-dismissible fade show';
        alert.setAttribute('role', 'alert');
        alert.innerHTML = message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>';

        document.body.appendChild(alert);

        // Auto-dismiss alert after 5 seconds
        setTimeout(function() {
            alert.classList.remove('show');
            alert.classList.add('fade');
            setTimeout(function() {
                alert.remove();
            }, 150);
        }, 5000);
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

    var contactForm = document.getElementById('booking-form');
    var submitAttempted = false; // Flag to track form submission attempts

    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            submitAttempted = true; // Set flag to true upon form submission

            var contactNumberField = document.getElementById('id_contact_number');
            var contactNumber = contactNumberField.value.trim();
            var errorSpan = document.getElementById('contact-number-error');

            // Reset error message
            errorSpan.textContent = '';

            // Validate only if submission has been attempted
            if (submitAttempted) {
                // Check if the contact number has spaces
                if (contactNumber.includes(' ')) {
                    errorSpan.textContent = 'Spaces are not allowed in the contact number.';
                    errorSpan.style.color = 'red';
                    event.preventDefault(); // Prevent form submission
                    return;
                }

                // Check if the contact number consists only of digits
                if (!contactNumber.match(/^\d+$/)) {
                    errorSpan.textContent = 'Contact number must contain only digits.';
                    errorSpan.style.color = 'red';
                    event.preventDefault(); // Prevent form submission
                    return;
                }

                // Check if the contact number starts with a '+' sign
                if (contactNumber.startsWith('+')) {
                    // Check if the contact number has at least 13 characters
                    if (contactNumber.length < 13) {
                        errorSpan.textContent = 'Contact number is incomplete. It must be at least 13 characters long.';
                        errorSpan.style.color = 'red';
                        event.preventDefault(); // Prevent form submission
                        return;
                    }
                } else {
                    // Check if the contact number has at least 12 digits
                    if (contactNumber.length < 12) {
                        errorSpan.textContent = 'Contact number is incomplete. It must be at least 12 digits long.';
                        errorSpan.style.color = 'red';
                        event.preventDefault(); // Prevent form submission
                        return;
                    }
                }
            }
        });

        // Reset the submitAttempted flag when user interacts with the contact number field
        var contactNumberField = document.getElementById('id_contact_number');
        contactNumberField.addEventListener('input', function(event) {
            submitAttempted = false;
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
                showCustomConfirm(function(confirmation) {
                    if (confirmation) {
                        showAlert("Reservation deleted successfully."); // Show alert on deletion
                        deleteForm.submit();
                    }
                });
            } else {
                console.error('Delete form not found for booking ID:', bookingId);
            }
        });
    });

    // Function to show custom confirmation dialog
    function showCustomConfirm(callback) {
        var overlay = document.createElement('div');
        overlay.className = 'custom-confirm-overlay';

        var confirmBox = document.createElement('div');
        confirmBox.className = 'custom-confirm-box';
        confirmBox.innerHTML = `
            <p>ARE YOU SURE YOU WANT TO DELETE THIS RESERVATION?</p>
            <div class="custom-confirm-buttons">
                <button class="custom-confirm-button confirm">Yes</button>
                <button class="custom-confirm-button cancel">No</button>
            </div>
        `;

        overlay.appendChild(confirmBox);
        document.body.appendChild(overlay);

        var confirmButton = confirmBox.querySelector('.confirm');
        var cancelButton = confirmBox.querySelector('.cancel');

        confirmButton.addEventListener('click', function() {
            document.body.removeChild(overlay);
            callback(true);
        });

        cancelButton.addEventListener('click', function() {
            document.body.removeChild(overlay);
            callback(false);
        });
    }
});