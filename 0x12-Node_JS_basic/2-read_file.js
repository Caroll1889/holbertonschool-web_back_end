const fs = require('fs');

module.exports = function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf8').split('\n');
  } catch (error) {
    throw Error('Cannot load the database');
  }

  data = data.slice(1, data.length);

  console.log(`Number of students: ${data.length}`);

  const obj = {};
  let student;
  data.forEach((item) => {
    student = item.split(',');
    if (!obj[student[3]]) obj[student[3]] = [];
    obj[student[3]].push(student[0]);
  });

  //
  for (const key of Object.keys(obj)) {
    if (key) {
      console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
    }
  }
};
