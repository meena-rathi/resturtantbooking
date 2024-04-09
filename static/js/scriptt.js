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
    // var lunchItems = [
    //     { image: "{% static 'lunch2.jpg' %}", description: "Lunch Item 1 Descriptionoipo" },
    //     { image: "{% static 'image/lunch2.jpg' %}", description: "Lunch Item 2 Description" },
    //     { image: "{% static 'image/lunch3.webp' %}", description: "Lunch Item 3 Description" },
    //     { image: "{% static 'image/lunch4.webp' %}", description: "Lunch Item 4 Description" }
    //   ];
    //   var dinnerItems = [
    //     { image: "{% static 'image/slide1.jpg' %}", description: "Lunch Item 1 Descriptionoipo" },
    //     { image: "{% static 'image/dinner2.jpg' %}", description: "Dinner Item 2 Description" },
    //     { image: "{% static 'image/dinner3.webp' %}", description: "Dinner Item 3 Description" },
    //     { image: "{% static 'image/dinner4.webp' %}", description: "Dinner Item 4 Description" }
    //   ];
  
    //   var lunchItemsContainer = document.getElementById('lunch-items');
    //   var dinnerItemsContainer = document.getElementById('dinner-items');
  
    //   function displayItems(items, container) {
    //     container.innerHTML = "";
    //     items.forEach(function(item) {
    //       var col = document.createElement('div');
    //       col.classList.add('col-lg-3', 'col-sm-6');
    //       col.innerHTML = `
    //         <div class="menu-item">
    //           <img src="${item.image}" alt="Lunch"/>
    //           <p>${item.description}</p>
    //         </div>
    //       `;
    //       container.appendChild(col);
    //     });
    //   }
  
    //   // Display lunch items initially
    //   displayItems(lunchItems, lunchItemsContainer);
  
    //   // Event listener for Lunch button
    //   document.getElementById('Lunch-tab').addEventListener('click', function() {
    //     displayItems(lunchItems, lunchItemsContainer);
    //   });
  
    //   // Event listener for Dinner button
    //   document.getElementById('dinner-tab').addEventListener('click', function() {
    //     displayItems(dinnerItems, dinnerItemsContainer);
    //   });
  
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
// document.addEventListener("DOMContentLoaded", function() {
  