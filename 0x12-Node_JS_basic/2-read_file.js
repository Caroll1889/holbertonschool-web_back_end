const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    let data = fs.readFileSync(path, 'utf8').split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);

    const obj = {};
    data.forEach((item) => {
      const student = item.split(',');
      if (!obj[student[3]]) obj[student[3]] = [];
      obj[student[3]].push(student[0]);
    });

    for (const key in obj) {
      if (key) {
        console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
      }
    }
  } catch (error) {
    throw Error('Cannot load the database');
  }
};
