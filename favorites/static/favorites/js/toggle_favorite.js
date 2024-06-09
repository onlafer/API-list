$(document).ready(function() {
    $('.favorite-button').on('click', function() {
        var itemId = $(this).data('item-id');
        var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: 'POST',
            url: '/favorite/toggle-favorite/',
            data: {
                'item_id': itemId,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response) {
                if (response.status === 'added') {
                    $(this).html('Удалить из избранного <i class="bi bi-suit-heart-fill"></i>');
                } else if (response.status === 'removed') {
                    $(this).html('Добавить в избранное <i class="bi bi-suit-heart"></i>');
                } else if (response.status === 'redirect') {
                    window.location.href = response.url;
                }
            }.bind(this)
        });
    });
});