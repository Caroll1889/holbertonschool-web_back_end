export default function updateUniqueItems(item) {
  if (!(item instanceof Map)) {
    throw Error('Cannot process');
  }
  for (const [el, val] of item.entries()) {
    if (val === 1) {
      item.set(el, 100);
    }
  }
  return item;
}
