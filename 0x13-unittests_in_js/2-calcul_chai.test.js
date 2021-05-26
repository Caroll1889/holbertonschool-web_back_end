const chaiTest = require('chai')
const calculateNumber = require('./2-calcul_chai');


describe('calculateNumber', function () {
  describe('Integers', function () {
    it('should return 4', function () {
      chaiTest.expect(calculateNumber('SUM', 1, 7)).to.equal(8);
    });
  });

  describe('One float', function () {
    it('should return 8', function () {
      chaiTest.expect(calculateNumber('SUM', 1, 6.7)).to.equal(8);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      chaiTest.expect(calculateNumber('SUM', 3.7, 1)).to.equal(5);
    });
  });

  describe('One float', function () {
    it('should return 5', function () {
      chaiTest.expect(calculateNumber('SUM', 1, 5.3)).to.equal(6);
    });
  });

  describe('Two floats', function () {
    it('should return 5', function () {
      chaiTest.expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
    });
  });

  describe('Subtract two integers', function () {
    it('should return -1', function () {
      chaiTest.expect(calculateNumber('SUBTRACT', 2, 3)).to.equal(-1);
    });
  });

  describe('Subtract one float', function () {
    it('should return 0', function () {
      chaiTest.expect(calculateNumber('SUBTRACT', 2.9, 3)).to.equal(0);
    });
  });

  describe('Subtract two float', function () {
    it('should return 4', function () {
      chaiTest.expect(calculateNumber('SUBTRACT', 6.6, 3.2)).to.equal(4);
    });
  });

  describe('Subtract two float', function () {
    it('should return 0', function () {
      chaiTest.expect(calculateNumber('SUBTRACT', 4.2, 3.9)).to.equal(0);
    });
  });

  describe('Divide two floats', function () {
    it('should return 1', function () {
      chaiTest.expect(calculateNumber('DIVIDE', 4.2, 3.9)).to.equal(1);
    });
  });

  describe('Divide one float', function () {
    it('should return 1.3', function () {
      chaiTest.expect(calculateNumber('DIVIDE', 4.2, 3)).to.equal(1.3333333333333333);
    });
  });

  describe('Divide one integer, and a 0', function () {
    it('should return "Error"', function () {
      chaiTest.expect(calculateNumber('DIVIDE', 2.2, 0)).to.equal('Error');
    });
  });

  describe('Divide two integers', function () {
    it('should return 1', function () {
      chaiTest.expect(calculateNumber('DIVIDE', 2, 2)).to.equal(1);
    });
  });
});