import redis from 'redis';
import express from 'express';
import { promisify } from 'util';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.filter((item) => item.id === id)[0];
}

// Redis

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const val = getAsync(`item.${itemId}`);
  return val;
}

// Express

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const current = await getCurrentReservedStockById(req.params.itemId);
  if (current) {
    res.send(current);
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
  }
  if (item.stock <= 0) {
    res.json({ status: 'Not enough stock available', itemId: item.id });
  } else {
    reserveStockById(item.id, item.stock - 1);
    res.json({ status: 'Reservation confirmed', itemId: item.id });
  }
});

app.listen(port, () => {
  console.log(`Server running at: http://localhost:${port}/`);
});
