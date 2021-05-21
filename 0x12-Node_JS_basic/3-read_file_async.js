const fs = require('fs');

module.exports = function countStudents(path) {
    const promise = (resolve, reject) => {
        fs.readFile(path, (error, data) => {
           if (error) {
            reject(Error('Cannot load the database'))
           }
            if (data) {
                let newData = data.toString().split('\n')
                newData = newData.slice(1, newData.length);
                console.log(`Number of students: ${newData.length}`);
                const obj = {};
                let student;
                newData.forEach((item) => {
                    student = item.split(',');
                    if (!obj[student[3]]) obj[student[3]] = [];
                    obj[student[3]].push(student[0]);
                });
                for (const key of Object.keys(obj)) {
                    if (key) {
                        console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
                    }
                }
            } 
            resolve()
        })
    }
    return new Promise(promise)
};
