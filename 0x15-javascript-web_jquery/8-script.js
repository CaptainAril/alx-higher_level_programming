$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done(function (json) {
  for (const movie of json.results) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
