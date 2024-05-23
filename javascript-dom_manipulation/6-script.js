document.addEventListener('DOMContentLoaded', () => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const nameOfCharacter = data.name;
      document.querySelector('#character').textContent = nameOfCharacter;
    });
});
