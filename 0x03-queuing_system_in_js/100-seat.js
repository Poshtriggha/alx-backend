import kue from 'kue';

const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');
const queue = kue.createQueue();

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;
const totalSeats = 50;

setAsync('available_seats', totalSeats);

const app = express();
const port = 1245;

const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
};

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});


app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats > 0) {
      const newSeats = currentSeats - 1;
      await reserveSeat(newSeats);

      if (newSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});


app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
