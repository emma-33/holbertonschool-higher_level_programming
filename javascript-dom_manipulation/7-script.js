document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      data.results.forEach((movie) => {
        const newList = document.createElement('li');
        const moviesList = document.querySelector('#list_movies');

        newList.textContent = movie.title;
        moviesList.appendChild(newList);
      });
    });
});
