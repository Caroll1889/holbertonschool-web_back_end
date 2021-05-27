var expect  = require("chai").expect;
var request = require("request");

describe('Basic Integration', function() {
  describe('GET', function() {
    let url = 'http://localhost:7865';

    it('returns status 200', function() {
      request(url, function(error, response, body){
          expect(response.statusCode).to.equal(200)
      });
    });

    it('returns the correct body', function() {
      request(url, function(error, response, body) {
        expect(body).to.equal('Welcome to the payment system')
      });
    });
  });
});