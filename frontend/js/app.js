const API = 'http://noco:8080/api/v1/db/data/v1/breforening/news';
const API_KEY = 'default_api_key';

fetch(API, { headers: { 'xc-auth': API_KEY } })
  .then(r => r.json()).then(data => {
    const list = document.getElementById('news-list');
    data.list.forEach(item => {
      const el = document.createElement('article');
      el.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p>`;
      list.appendChild(el);
    });
  });
