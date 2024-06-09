$(document).on('click', '.deleteKeyBtn', function() {
    var itemId = $(this).data("id");
    $.ajax({
        type: 'POST',
        url: '/api/delete_api_key/',
        data: {
            'item_id': itemId,
        },
        success: function (response) {
            
            if (response.status === 'deleted') {
                $("#" + itemId).remove();
                var rows = document.querySelectorAll('tbody tr');
                if (rows.length == 0) {
                    document.getElementById("empty-list").classList.remove("d-none");
                } else {
                    for (var i = 0; i < rows.length; i++) {
                        var cell = rows[i].getElementsByTagName('td')[0];
                        cell.textContent = i + 1;
                    }
                }
            } else if (response.status === 'redirect') {
                window.location.href = response.url;
            }
        }
    });
});

$(document).on('click', '.changeKeyStatusBtn', function() {
    var itemId = $(this).data("id");
    $.ajax({
        type: 'POST',
        url: '/api/change_api_key_status/',
        data: {
            'item_id': itemId,
        },
        success: function (response) {
            icon = $("#" + itemId + " td:nth-child(4)" + " i");
            if (response.status === 'excluded') {
                $("#" + itemId + " td:nth-child(3)").text("Неактивен");
                icon.removeClass("bi-toggle2-on");
                icon.addClass("bi-toggle2-off");
            } else if (response.status === 'included') {
                $("#" + itemId + " td:nth-child(3)").text("Активен");
                icon.removeClass("bi-toggle2-off");
                icon.addClass("bi-toggle2-on");
            } else if (response.status === 'redirect') {
                window.location.href = response.url;
            }
        }
    });
});

$(document).on('click', '#create-key-button', function() {
    $.ajax({
        type: 'POST',
        url: '/api/create/',
        success: function (response) {
            if (response.status === 'redirect') {
                window.location.href = response.url;
            } else {
                var alertElement = document.getElementById("alert");

                if (alertElement.classList.contains("d-none")) {
                    alertElement.classList.remove("d-none");
                }
                if (response.status === 'error') {
                    alertElement.classList.remove("alert-success");
                    alertElement.classList.add("alert-danger");
                } else {
                    var newRow = document.createElement('tr');
                    newRow.setAttribute('id', response.key_id);

                    alertElement.classList.remove("alert-danger");
                    alertElement.classList.add("alert-success");
                    newRow.innerHTML = `<td></td><td>${response.key}</td><td>Активен</td><td><i class="bi bi-toggle2-on btn pt-0 changeKeyStatusBtn" data-id="${response.key_id}"></i><i class="bi bi-trash3-fill btn pt-0 deleteKeyBtn" data-id="${response.key_id}"></i></td>`;
                    $('#apikeys-tbody').append(newRow);

                    var rows = document.querySelectorAll('tbody tr');
                    if (rows.length - 1 == 0) {
                        document.getElementById("empty-list").classList.add("d-none");
                    }

                    for (var i = 0; i < rows.length; i++) {
                        var cell = rows[i].getElementsByTagName('td')[0];
                        cell.textContent = i + 1;
                    }
                }
                response.objects.forEach(obj => {
                    $(obj.id).text(obj.value);
                });
            }
        }
    });
});
