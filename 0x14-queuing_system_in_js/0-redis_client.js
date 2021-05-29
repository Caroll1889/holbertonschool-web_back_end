import redis from 'redis';
const client = redis.createClient();

client.on("error", function(error) {
    console.log(`Redis client not connected to the server: ${error.message}` );
});

client.on('connect', function() {
    console.log('Redis client connected to the server')
})