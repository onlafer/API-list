const links = document.querySelectorAll('.accordion-link');

links.forEach(link => {
    link.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});