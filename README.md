# MOLA-Chrome-Extn

Overview 
  A chrome extension which will perform sentiment analysis on the english tweets from the Twitter. It adds a tag "Detcted Mood" for every english tweet which can be either Positive, Negative or Neutral 

The MOLA-Chrome-Extn project is designed on a client-server based model. 
  Server - A web server is designed using Python Flask frame work and deployed on GCP.
  Client - Here client is a chrome extension which is requesting the server apis to perform sentiment analysis.
  
Accessing API End-Points
  The Server is deployed on GCP and is already running(Public IP: 34.125.24.7). The server has two REST API endpoints
  1. /api/language-detection
    To access this api from postman use the following command
    > curl --location --request POST 'http://34.125.24.7:50000/api/language-detection' --header 'Content-Type: application/json' --data-raw '[{"tweet_text": "Stats on Twitter World Cup"}, { "tweet_text": "As the saying goes, be careful what you wish, as you might get it"}, { "tweet_text": "I love USC ❤️"}]'
  3. /api/sentiment-score
    To access this api from postman use the following command
    > curl --location --request POST 'http://34.125.24.7:50000/api/sentiment-score' --header 'Content-Type: application/json' --data-raw '[{"tweet_text": "Stats on Twitter World Cup"}, { "tweet_text": "As the saying goes, be careful what you wish, as you might get it"}, { "tweet_text": "I love USC ❤️"}]'
    
Running The Server On Local
  1. pip3 install -r requirements.txt
  2. nohup python server.py > log.txt 2>&1 &
  3. Access the APIs using localhost
  
    
Adding a chrome extension

  Please follow the instructions https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/#load-unpacked to load the extension. Please choose "ChromeExtension" from the github while selecting the chrome extension directory. This should add an extension to your chrome with USC logo. On going to a twitter page and and clicking on the extension icon should display a "Detected Mode" tag for every tweet.
  
Limitations

  The chrome extensions might not work as the GCP hhtps is not working because. Requesting a http from secured Twitter website is giving a Mixed COntent Error
