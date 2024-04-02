function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to handle scroll event
function handleScroll() {
    var sections = document.querySelectorAll('.section');
    sections.forEach(function(section) {
        if (isInViewport(section)) {
            section.classList.add('visible');
        } else {
            section.classList.remove('visible');
        }
    });
}


document.addEventListener('DOMContentLoaded', function() {
    // Function to handle reservation button click
    function redirectToReservation() {
        // Redirect to the reservation page
        window.location.href = "reservation"; // Update with the correct URL of your reservation page
    }

    // Add click event listener to reservation button
    var reservationButton = document.getElementById('reservation-btn');
    if (reservationButton) {
        reservationButton.addEventListener('click', redirectToReservation);
    } else {
        console.error("Reservation button not found.");
    }
});
//window.addEventListener('scroll', handleScroll);

// document.addEventListener('DOMContentLoaded', function() {
//     // Function to handle reservation button click

//         console.log("Reservation button clicked");
//         // You can add additional logic here if needed
//         // For example, redirecting to the reservation page
//         //window.location.href = "/reservation";
//     // Add click event listener to reservation button
//     var reservationButton = document.getElementById('reservation-btn');
//     if (reservationButton) {
//         reservationButton.addEventListener('click', reservation);
//     } else {
//         console.error("Reservation button not found.");
//     }

// });

// window.addEventListener('scroll', handleScroll);