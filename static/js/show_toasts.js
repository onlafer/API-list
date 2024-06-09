var options = {
  animation: true,
  delay: 16000,
};

var toastEls = document.querySelectorAll('.toast');

toastEls.forEach(function (toastEl, index) {
  var toast = new bootstrap.Toast(toastEl, options);
  setTimeout(function () {
    toast.show();
  }, index * 500); // Увеличиваем задержку между показом каждого "toast" сообщения на 100 миллисекунд
});