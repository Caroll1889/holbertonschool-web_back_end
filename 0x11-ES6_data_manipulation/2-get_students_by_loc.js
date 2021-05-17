export default function getStudentsByLocation(listOfStudent, city) {
  return listOfStudent.filter((cities) => cities.location === city);
}
