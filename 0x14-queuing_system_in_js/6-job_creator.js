import kue from 'kue';

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('completed', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
