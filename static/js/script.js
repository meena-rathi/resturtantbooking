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

// Add scroll event listener
window.addEventListener('scroll', handleScroll);