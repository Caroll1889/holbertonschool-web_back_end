const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Integers', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber(1, 7), 8);
    });
  });

  describe('One round', function () {
    it('should return 8', function () {
      assert.strictEqual(calculateNumber(1, 6.7), 8);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(3.7, 1), 5);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1, 5.3), 6);
    });
  });

  describe('Two floats', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });
});