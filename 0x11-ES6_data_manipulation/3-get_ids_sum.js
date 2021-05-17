export default function getStudentIdsSum(listOfStudent) {
  const ids = (element) => element.id;
  const acum = (acumulator, num) => acumulator + num;
  return listOfStudent.map(ids).reduce(acum, 0);
}
