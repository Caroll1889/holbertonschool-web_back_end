import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (ch, message) => {
  if (ch === 'holberton school channel') {
    console.log(message);
  }

  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
