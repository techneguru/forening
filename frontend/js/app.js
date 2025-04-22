const API = 'https://DIN_SERVER:8080/api/v1/db/data/v1/breforening/news';
fetch(API, { headers: { 'xc-auth': 'DIN_API_KEY' } })
  .then(r=>r.json()).then(data=>{
    const list = document.getElementById('news-list');
    data.list.forEach(item=>{
      const el = document.createElement('article');
      el.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p>`;
      list.appendChild(el);
    });
  });
