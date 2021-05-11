export default function guardrail(mathFunction) {
  const arr = [];
  let value;
  try {
    value = mathFunction();
  } catch (error) {
    value = `${error.name}: ${error.message}`;
  }
  arr.push(value);
  arr.push('Guardrail was processed');
  return arr;
}
