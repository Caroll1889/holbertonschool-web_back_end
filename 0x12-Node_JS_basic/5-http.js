const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;
const hostname = '127.0.0.1';

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const { url } = req;
  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const student = await countStudents(process.argv[2]);
      res.end(`${student.join('\n')}`);
    } catch (error) {
      res.end(error.message);
    }
  }
  res.statusCode = 404;
  res.end();
});
app.listen(port, hostname, () => {
});
module.exports = app;
