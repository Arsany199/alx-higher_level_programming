$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const myurl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(myurl + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
    $('DIV#hello').html(data.hello);
  });
}
