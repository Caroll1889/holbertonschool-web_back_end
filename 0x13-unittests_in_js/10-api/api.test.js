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

  describe('GET/cart/30', () => {
    let url = 'http://localhost:7865/cart/30';

    it('return status 200 and id 30', (done) => {
      request(url,function(error, response, body){
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 30');
        done();
      })
    })
  })

  describe('GET/cart/3', () => {
    let url = 'http://localhost:7865/cart/3';

    it('return status 200 and id 30', (done) => {
      request(url,function(error, response, body){
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Payment methods for cart 3');
        done();
      })
    })  
  })

  describe('GET/cart/g23', () => {
    let url = 'http://localhost:7865/cart/g23';

    it('return status 404', (done) => {
      request(url,function(error, response, body){
        expect(response.statusCode).to.equal(404);
        done();
      })
    })  
  })

  describe('GET/cart/world', () => {
    let url = 'http://localhost:7865/cart/world';

    it('return status 404', (done) => {
      request(url,function(error, response, body){
        expect(response.statusCode).to.equal(404);
        done();
      })
    })  
  })
})