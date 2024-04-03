$(document).ready(function () {
  $.ajax({
    url: 'https://swapi.co/api/films/?format=json',
    type: 'GET',
    success: function (data) {
      $.each(data.results, function (i, film) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
