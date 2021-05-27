const { expect } = require('chai');
const request = require("request");

describe('Basic Integration', () => {
  describe('GET', () => {
    let url = 'http://localhost:7865';

    it('returns status 200', (done) => {
      request(url, function(error, response, body){
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal('Welcome to the payment system');
          done();
      });
    });     
  });
});