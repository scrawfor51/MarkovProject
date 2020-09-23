# MarkovProject




Stephen Crawford
Computational Creativity
9.22.2020

		Batkov: Curb your bat-thusiasm

SETUP:
	
	1. Download the master using git clone or by downloading as a zip.

	2. Download and install python3 if you do not already have it installed. 

	3. Open the file (if not cloned) in a IDE such as PyCharm or VS CODE.

	4. Navigate to the Main.py file. 

	5. Depending on the IDE, there should be a run button (a small green arrow), if not, you can right click on the file and there should be a run option. Finally, if that does not seem an option, 		you should be able to run the file by navigating to the file in your terminal and using the command:     python3 Main.py   



Personal Meaning:

This project is quite meaningful to me for a number of reasons. Growing up, I loved superheroes, powers, and all things associated. If it seemed like an underdog story where a once downtrodden good overcame the darkest evil whilst discovering there was something special about themselves all along—I was 100% in. In short, growing up in rural Maine, as an only child who experienced severe and traumatic bullying, superheroes drew me towards them like magnets. Not only did they have this intrinsic cool factor about them, but more often then not they stood as an example of someone somewhere, who in my mind, was able to overcome hardship and also gain the admiration of others. It was this combination of being undeniably good, while also holding the respect and adoration of their peers and communities that really drew me to the superhero/heroes arc which is so common in comic books. As a result, not only did I rewatch X-Men cartoons and movies dozens of times, but I became obsessed with the making of heroes, who they were, and where they came from. I can remember reading for hours two massive encyclopedias detailing the powers, backstories, and trivia of all the superheroes from the DC and Marvel universes and wanting to do nothing less but reread and fantasize about the day that I inevitably discovered my own powers. 

Of course, the last part never happened (or hasn’t yet…), but I continued to love superheroes and the like for years to come. As I grew older, I also came to enjoy comedy—especially the bizarre, or strange. In large part thanks to my dad’s insatiable desire to watch the WORST films he could find (favorite titles include Sharktopous, Zombeavers, and Tire), I became a media consumer on a strict diet of the obscure and the fantastical. This combination lead to various occurrences throughout the years, such as the year or two I had neon dyed hair, or the time I purposefully tried to breathe in a YMCA swimming pool because I was convinced for sure that I would be able to breathe underwater, but also lead to my long lasting fondness for both superheroes and oddball comedy. So here we are, you reading, I writing, a README for a project who’s stated purpose is to interlay the worlds of Batman (admittedly an overrated superhero in my opinion, but what can you do) and Curb Your Enthusiasm. 



Challenge:

This project was quite challenging for a number of reasons which will be further seen when you run through an examine the code. The most obvious of these challenges is the placement of the show quotes within the comic strip. As can be seen in the Main.py file, I was unable to find a convenient method of storing and entering the pixel coordinates for where I wanted the text to be inserted. This meant that I had to resign to using a stylistically poor and inefficient method of creating lists of coordinates for each image. Similarly, a further challenge I ran into was trying to get the inserted text to fit within the text bubbles of the comic strips. This was incredibly difficult given the strips were written so as to accommodate the original text only. What this resulted in was issues with overflow of the inserted text going outside the bounds of the text bubbles. I tried several different solutions including creating backgrounds for the text I was going to insert (basically making my own new bubbles over the old) as well as various manipulations of the text such as font size, and the division of quotes into different sized lines. Unfortunately, no solution I found was perfect and so this area requires further improvement. This will likely come along side improvement of the storage of the pixel coordinates given the fact that the placement of the text within the bubble greatly is greatly affected by how or what the coordinates are stored as. 

As mentioned, during this project I utilized the Pillow Library which I was unfamiliar with as well as handled data in forms I had not previously. Both of these areas pushed me outside my comfort zone significantly. Beyond fixing the issues mentioned above, I feel a next step for me with this project is to further familiarize myself with both the Pillow Library and the OS module so that I can try and create a more dynamic and intelligent program. My hope is that I may be able to make the program be able to in take any text file and any image and be able to  natively locate any text bubbles within the image, which it will cover up and then insert perfectly placed and sized text in. 


Creativity:

As discussed in class, our working definition for a computationally creative system is one which produces something which is novel, valuable, and intentional. In my opinion, I cannot say that my program is creative yet because of the last factor. While I due think that the output of the system is both novel and valuable—as the images while inspired by the Markov strips, are very different from other things I have seen; and the project has significant personal meaning and therefore value to me—I do not feel that it is acting with intention. My interpretation of the intention of the computationally creative system is that the system acts with some goal. Though my program executes with a specific purpose it lacks any ability to determine for itself what is “good” or “bad” and therefore has no ability to create different content with intention. Instead, the program creates new content simply when the user directs it to. This leads me to feel that my system is not yet computationally creative. 


Acknowledgments:

I wish to give full credit, acknowledgment, and thanks to numerous bodies which provided me with help and resources while completing this project. 
 For The Batman comic strips which I used, I owe thanks to both readcomiconline.to as well as Tom King and David Finch who were the author and artist respectively. 

For the quotes which I used to populate my art, I owe credit to Larry David and HBO who wrote, starred in, and aired the series. 

For Python guides I wish to acknowledge and recommend the websites stackoverflow.com, python-course.edu, and geeksforgeeks.org.

For help with the Pillow Library, I owe thanks and acknowledgment to mail.python.org, code-maven.com, and pillow.readthedocs.io.

Finally, I want to thank Professor Sarah Harmon for helping provide direction, advice, and patience during the creation of this project. 

