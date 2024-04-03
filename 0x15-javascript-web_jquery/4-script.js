const $headerElem = $('header');
const $divtoggleHeader = $('DIV#toggle_header');

$divtoggleHeader.on('click', function () {
  const currentClass = $headerElem.attr('class');

  if (currentClass === 'green') {
    $headerElem.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerElem.toggleClass(`${currentClass} green`);
  }
});
