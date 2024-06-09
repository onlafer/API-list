const fileInput = document.getElementById('id_logo');
const imagePreview = document.getElementById('imagePreview');

fileInput.addEventListener('change', function () {
    const file = fileInput.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        imagePreview.src = e.target.result;
    }
    if (file) {
        reader.readAsDataURL(file);
        imagePreview.classList.remove('d-none');
    } else {
        imagePreview.classList.add('d-none');
    }
});