# amadoruavsapplication
**__Amogh Chaudhary's AmadorUAVs Software Application Code__**

__Task 1(task1.py):__

*Task Requirements:*
- Find the centroid of every collection, representing the “best” possible estimate of the ODLC’s position given N-ordered pairs describing (latitude, longitude) points. 
- Filter out outliers as best as possible
I used DBSCAN as a clustering algorithm and used matplotlib for me to see the clusters, and numpy to calculate the centroids.

__Task 2(task2.py):__

*Task Requirements:*
- Fix the flight plan by traversing within the geofence with a 25ft distance from the edge instead of exceeding its bounds (see demonstration image). 
- Generate a .plan file (hint: use JSON) which can be imported in QGC. Learn how these files are formatted by installing QGC on your personal computer
I moved the points so all of them were within the geofence, but not all paths yet.

__Task 3(task3.py):__

*Task Requirements:*
- Write generator script(s) for shape and/or character.
- Train a YOLOv8n model on this data (hint: is there a way to not manually label every image?).
- Correctly recognize the shape and character of the ODLC.
I implemented some shapes & text in image generation, but some need to be implemented/fixed.

__**Note:**__

I successfully completed the first task and made good progress on the second task as well. I did run into a challenge there with the geofence intersecting with the flight path, even after applying the buffer, and I wasn't able to create the JSON output format, but with a bit more time, I feel I would be able to resolve the issues. I also made progress on Task #3 but didn't get to finish it as I need to fix some bugs I have as a result of the way my functions interacted with the Pillow library. However, I did enjoy the learning experience I received as a result of working on this, and I'd love any feedback and suggestions regarding some of my code in this assignment or the way I code in general to improve.

