// frontend/js/app.js
const API = '/api/news'; // Proxy endpoint
const list = document.getElementById('news-list');
list.innerHTML = '<p>Loading news...</p>';

fetch(API)
  .then(r => {
    if (!r.ok) {
      throw new Error(`HTTP error! status: ${r.status}`);
    }
    return r.json();
  })
  .then(data => {
    list.innerHTML = ''; // Clear loading message
    if (data.list.length === 0) {
      list.innerHTML = '<p>No news available at the moment.</p>';
      return;
    }
    data.list.forEach(item => {
      const el = document.createElement('article');
      el.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p>`;
      list.appendChild(el);
    });
  })
  .catch(err => console.error('Could not fetch news:', err));
