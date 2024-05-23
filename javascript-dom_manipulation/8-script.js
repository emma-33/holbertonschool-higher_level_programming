document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const helloTranslation = document.querySelector('#hello');
      const helloElement = document.createElement('p');

      helloElement.textContent = data.hello;
      helloTranslation.appendChild(helloElement);
    });
});
