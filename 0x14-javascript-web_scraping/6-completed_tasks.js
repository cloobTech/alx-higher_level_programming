#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);

    const tasks = {};

    data.forEach(task => {
      if (task.completed) {
        const userId = task.userId;
        if (userId in tasks) {
          tasks[userId]++;
        } else {
          tasks[userId] = 1;
        }
      }
    });

    console.log(tasks);
  }
});
