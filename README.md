Hi Welcome to the Clumptracker Process Repository
Most of these files are my process learning and developing clump tracker. You can check those out as those are pretty short.
You should run CLUMPTRACKERBABY, which culminates my HSV-testing, morpholigcial filters testing(eroding, diluting image), and then finally the clump tracking logic(explained simply below)
*****HOW TO RUN*****
*Input*
Take some of the sample images uploaded, download them, then copy their exact folder path thing and paste it into line 26 the "img = cv.read()"
*Process*
OpenCV extracts all pixels within the HSV clamp I tested with the earlier color detection files
OpenCV then erodes it in order to get rid of noise
However this this function might make circles smaller so i dilute it as well
Then we fill in each hole to create perfect circles and then run Hough on the final image to extract all ball locations and radii.
***CLUMPING LOGIC EXPLAINED***
Essentially each circle creates a box around it with sidelength being 2x its radius and checks every ball to see it if its in that box. It then adds all balls in the box AND balls that
are in the same clump  as all of those balls into a new clump. This way, even if two balls are in the same clump(close together) but are maybe further away and thus have a smaller radii
and thus are not in each others squares, another ball acts as a bridge. I do this be recursively checking every ball.
*Output*
This code outputs the clumps it recognized from the image as text.
