const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect, assert } = require('chai');

describe('getPaymentTokenFromApi', function() {
  describe('result true', function() {

    it('resolve', function(done) {
      getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.include({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => done(error))
    });
  });
});