const html = require('fs').readFileSync('mikupad.html', 'utf8');
const regex = /<textarea[\s\S]*?id="prompt-area"[\s\S]*?<\/textarea>/i;
const match = html.match(regex);
console.log(match);
