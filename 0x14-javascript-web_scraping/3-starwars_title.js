#!/usr/bin/node
/* Prints the title of a Star Wars movie where
 * the episode number matches a given integer
 */
const request = require('request');
const episode = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';
request(API_URL + episode,
  function (err, response, body) {
    if (err) {
      console.error(err);
    } else if (response.statusCode === 200) {
      const responseJSON = JSON.parse(body);
      console.log(responseJSON.title);
    } else {
      console.log('Error code: ' + response.statusCode);
    }
  });
