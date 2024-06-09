const uploadInput = document.getElementById('id_image');
const previewImage = document.getElementById('preview-image');
const reset = document.getElementById('reset');


uploadInput.addEventListener('change', function() {
const file = this.files[0];
if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        previewImage.src = e.target.result;
    }
    reader.readAsDataURL(file);
    reset.value = false;
}
});

function resetImage(defaultImageUrl) {
    previewImage.src = defaultImageUrl;
    reset.value = true;
}