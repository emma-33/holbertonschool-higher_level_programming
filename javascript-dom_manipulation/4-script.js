document.querySelector('#add_item').addEventListener('click', () => {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';

  const classList = document.querySelector('.my_list');
  classList.appendChild(newElement);
});
