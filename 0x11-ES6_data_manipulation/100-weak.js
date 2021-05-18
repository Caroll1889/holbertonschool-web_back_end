export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const count = weakMap.get(endpoint);
  if (count) {
    weakMap.set(endpoint, count + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
  if (count + 1 === 5) {
    throw Error('Endpoint load is high');
  }
}
