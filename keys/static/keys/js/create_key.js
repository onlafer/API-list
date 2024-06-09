$(document).ready(function () {
    $('#create-key-button').on('click', function () {
        $.ajax({
            type: 'POST',
            url: '/api/create/',
            success: function (response) {
                if (response.status == 'redirect') {
                    window.location.href = response.url;
                }
                else {
                    response.objects.forEach(obj => {
                        $(obj.id).text(obj.value);
                    });
                }
            }
        });
    });
});
