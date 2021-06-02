import redis from 'redis';
import express from 'express';
import { promisify } from 'util';
import kue from 'kue';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
let reservationEnabled;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats;
}

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  reserveSeat(50);
  reservationEnabled = true;
});

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const available = await getCurrentAvailableSeats;
  res.json({ numberOfAvailableSeats: available });
});

app.get('/reserve_seat', async (req, res) => {
  if (reservationEnabled === false) {
    res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);
  });
});

app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let available = getCurrentAvailableSeats();

    if (available <= 0) {
      done(Error('Not enough seats available'));
    }

    available -= 1;

    reserveSeat(available);

    if (available <= 0) {
      reservationEnabled = false;
    }

    done();
  });
  res.json({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log(`Server running at: http://localhost:${port}/`);
});
