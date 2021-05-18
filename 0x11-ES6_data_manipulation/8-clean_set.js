export default function cleanSet(set, startString) {
  const newArr = [...set];
  //   const newWord = startString.length;
  if (!startString || startString.length === 0) {
    return '';
  }
  const words = newArr.filter((x) => x.startsWith(startString)).map((x) => x.slice(3)).join('-');
  return words;
}
