const fs = require('fs');
const items = JSON.parse(fs.readFileSync('D:/10jo_Studio/01_pain_mining/data/processed/painpoints.json', 'utf8'));
const status = {};
items.forEach(i => { const s = i.status || 'new'; status[s] = (status[s] || 0) + 1; });
console.log(JSON.stringify({ total: items.length, status }));
