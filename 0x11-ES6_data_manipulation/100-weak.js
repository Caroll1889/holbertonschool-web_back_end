export const weakMap = new WeakMap();

export default function queryAPI(endpoint) {
  const count = weakMap.get(endpoint);
  weakMap.set(endpoint, count + 1);
  if (count === 5) {
    throw Error('Endpoint load is high');
  }
}
