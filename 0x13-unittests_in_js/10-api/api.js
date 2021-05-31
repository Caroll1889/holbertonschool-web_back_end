const express = require('express');

const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}` )
});

app.get('/available_payments', (req, res) => {
  const pay = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };
  res.json(pay)
})

app.get('POST /login', (req, res) => {
  res.send(`Welcome ${req.body.userName}`)
})

app.listen(port, () => {
  console.log('API available on localhost port 7865');
});