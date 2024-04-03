$(document).ready(function () {
  const myurl = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $helloElement = $('div#hello');

  function Salut () {
    return $.get({
      url: myurl,
      dataType: 'json'
    });
  }

  Salut().then((res) => {
    $helloElement.text(res.hello);
  });
});
