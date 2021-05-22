const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => res.send('Hello Holberton School!'));
app.get('/students', async (req, res) => {
  const msj = 'This is the list of our students\n';
  try {
    const data = await countStudents(process.argv[2]);
    res.send(`${msj}${data.join('\n')}`);
  } catch (error) {
    res.send(`${msj}${error.message}`);
  }
});
app.listen(port);
module.exports = app;
