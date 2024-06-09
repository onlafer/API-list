var filters = document.querySelectorAll('.filter');

filters.forEach(function(filter) {
    filter.addEventListener('change', function() {
        applyFilters();
    });
});

function applyFilters() {
    var selectedFilter = document.querySelector('input[name="API_type"]:checked').value;
    var newUrl = window.location.origin + window.location.pathname + '?API_type=' + selectedFilter;
    window.history.pushState({path: newUrl}, '', newUrl);
}