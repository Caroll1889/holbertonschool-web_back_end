const sinon = require('sinon');
const { expect }  = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils')


describe('Stubs', function () {
  it('Is the same math', () => {
    const spyUtils = sinon.stub(Utils, 'calculateNumber');
    spyUtils.returns(10)
    const spyConsole = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(spyConsole.calledOnceWithExactly('The total is: 10')).to.be.true;

    spyUtils.restore();
    spyConsole.restore();
  });
});