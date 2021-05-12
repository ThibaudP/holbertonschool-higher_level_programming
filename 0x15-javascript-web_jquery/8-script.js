$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  $.each(data.results, (i, movie) => {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  });
});
