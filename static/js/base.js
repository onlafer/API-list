let rotated = false;
const paragraph = document.getElementById('categoryList');
const arrow = document.getElementById('chevronArrow');

function rotateImage() {
    const img = document.querySelector('.nav-item .down-arrow');
    if (rotated) {
        img.style.transform = 'rotate(0deg)';
        rotated = false;
    } else {
        img.style.transform = 'rotate(180deg)';
        rotated = true;
    }
    if (paragraph.classList.contains('text-white')) {
        paragraph.classList.remove('text-white');
        arrow.classList.remove('chevron-fill');
    } else {
        paragraph.classList.add('text-white');
        arrow.classList.add('chevron-fill');
    }
}