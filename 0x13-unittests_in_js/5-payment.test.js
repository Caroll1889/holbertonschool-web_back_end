const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('hooks', () => {
  let sConsole;
  beforeEach(() => {
  // runs before each test
    sConsole = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // runs after each test
    sConsole.restore();
  });

  it('console is logging The total is: 120', () => {
    sendPaymentRequestToApi(100, 20);
    expect(sConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(sConsole.calledOnce).to.be.true;
  });

  it('console is logging The total is: 20', () => {
    sendPaymentRequestToApi(10, 10);
    expect(sConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(sConsole.calledOnce).to.be.true;
  });
});
