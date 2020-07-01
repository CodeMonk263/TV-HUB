# Vids-Collector

Website for Collecting Videos from the WeB 

Included start file is a bash script to initialize all packages and run the servers

just run ->

>> ./start 
 
------- OR ---------
 
>> bash start

NOTE: Make sure you have npm, python, pip, and git bash installed!

To start the program next time just run ->

>> ./run

NOTE: The server is running on all ips across the same wifi hence to access this website on phone just type in your phone browser ->

http://<your host machine ip>:8000

To find host ip simply type in cmd -> 

>> ipconfig 

-----------------------------------------

Instructions on using the app ->

Backend api can be accessed by going to ->

http://<your host machine ip>:8000/api

The backend api can be used to get a fresh list of videos by clicking Change Page button and entering the page number to get videos from. Once api call is done, you are returned with a "Success" message which means api call has been successfully completed. Now simply come back to home page, refresh it and you will be welcomed with your requested page and its videos.

If you want to stream a video just use click on the WATCH button and u will be redirected to an api call which will fetch the final video link for you by using selenium. Wait for some time and once the video is fetched the src field will be something other than "None".

Once that happens just return back to the home page and refresh it. After that the video of your choice will have its background changed to blue and ready to watch. Just click on the WATCH button again.

There is a search field where you can add search strings too! (Very experimental breaks down often)

Authors:

Shaurya Vijayvargiya
