export default function cleanSet(set, startString) {
  let newString = '';
  // const newArr = [...set]
  if (!startString || startString.length === 0) return newString;

  set.forEach((word) => {
    if (word && word.startsWith(startString)) {
      newString += newString.length === 0 ? word.replace(startString, '') : word.replace(startString, '-');
    }
  });
  return newString;
}
