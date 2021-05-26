const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('Integers', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 7), 8);
    });
  });

  describe('One float', function () {
    it('should return 8', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 6.7), 8);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber('SUM', 3.7, 1), 5);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 5.3), 6);
    });
  });

  describe('Two floats', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
    });
  });

  describe('Subtract two integers', function () {
    it('should return -1', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
    });
  });

  describe('Subtract one float', function () {
    it('should return 0', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.9, 3), 0);
    });
  });

  describe('Subtract two float', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 6.6, 3.2), 4);
    });
  });

  describe('Subtract two float', function () {
    it('should return 0', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 4.2, 3.9), 0);
    });
  });

  describe('Divide two floats', function () {
    it('should return 1', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 4.2, 3.9), 1);
    });
  });

  describe('Divide one float', function () {
    it('should return 1.3', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 4.2, 3), 1.3333333333333333);
    });
  });

  describe('Divide one integer, and a 0', function () {
    it('should return "Error"', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 2.2, 0), 'Error');
    });
  });

  describe('Divide two integers', function () {
    it('should return 1', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 2, 2), 1);
    });
  });
});