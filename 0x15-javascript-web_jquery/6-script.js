const $myheader = $('header');
const $updateHeader = $('div#update_header');

$updateHeader.on('click', function () {
  $myheader.text('New Header!!!');
});
