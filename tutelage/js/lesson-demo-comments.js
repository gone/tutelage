/*
This file adds the comments for this specific demo, and it automatically rolls the comments.

Dependencies:
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
  <script type="text/javascript" src="./js/comment-roll-widget.js"></script>
*/

// declare a couple of functions
var CommentRollTick;
var _addLessonDemoComments;

function addLessonDemoComments(pUpdateTime) {
  // create comment roll widget
  comment_roll = CommentRoll("tips");

  // add comment (see below for dirty details)
  _addLessonDemoComments();

  // add automatic comment rolling
  CommentRollTick = function() {
    comment_roll.nextComment();
    setTimeout("CommentRollTick()", pUpdateTime)
  }
  CommentRollTick();
}

_addLessonDemoComments = function() {
  // add comments
  comment_roll.addComment("bzzpinkygirl", "Feb 11, 2012", "I baked the chicken in the oven the day before. Then in the morning I boiled left over uncooked chicken bones then added carrots and parsley to make chicken broth. Turned out very good! All 3 of my children enjoyed it!");
  comment_roll.addComment("theeartofseduction", "Feb 9, 2012", "Heavy cream instead of milk, and an egg wash to smooth over crust, for that nice grandmas goodies appeal.");
  comment_roll.addComment("Mikenopolis", "Jan 19, 2012", "@omgphud look up \"Hurry Up Chicken Pot Pie-Food Network\" from Paula Deen it's pretty good");
  comment_roll.addComment("tvaldez108", "Dec 28, 2011", "Tried it, THE BEST!!!!!!! Just make sure to heat till thickens or use less broth. I will NEVER buy a frozen pot pie ever again!");
  comment_roll.addComment("someone2know77", "Nov 12, 2011", "Just finished eating this!! AWESOME!!!!! One slight addition, I rubbed the inside of the pie crusts with poultry seasoning to give a hint of a dressing taste...3 of us devoured the pie...so full! (and did an egg wash to the top crust)");
  comment_roll.addComment("sweetiestgirl", "Nov 2, 2011", "i just use cream of chicken soup and then add the chicken and frozen veggies...works just as well :)");
  comment_roll.addComment("phoodphanatic124", "Nov 2, 2011", "nice! if you're looking for something savory, i always use a bit of oyster flavored sauce or hoisin sauce if you want that sweetness. i cant wait to try this recipe at home! :)");
  comment_roll.addComment("neinsager", "Nov 2, 2011", "@neinsager oh i also grated some cheddar cheese over the filling before placing the top crust.");
  comment_roll.addComment("Pizztoff", "Oct 28, 2011", "Wheres the potatoes? How can you have a pot pie with no potatoes?! =P");
  comment_roll.addComment("RCasto", "May 17, 2011", "I've made this simple recipe twice so far and it's been a hit! And it's really easy and not that time consuming. I tweaked it a little bit, just according to what I prefer, but this makes a good foundation to build upon for a good chicken pot pie.");
  comment_roll.addComment("UseeMeTube60", "Dec 21, 2010", "@kammi6586 Yes, take a chicken breast and cut it up in small cubes....Then place in pan and fry for three to five minutes...Does not have to be cooked thoroughly through because it will be baked for 30-40 minutes at 425 degrees in oven. Hope this helps?");
  comment_roll.addComment("onyxone144", "Aug 16, 2010", "@kammi6586 Not a stupid question. You could boil a whole chicken, or bake and bone a whole chicken. Take the skin and fat off the chicken. After it has cooled shred the chicken then mix w/ veggies and sauce. Put in the crust like she instructed, then enjoy.");
  comment_roll.addComment("kammi6586", "Jun 10, 2010", "This is a stupid question but could one one of you tell me how to cut and cook the chicken? is that a chicken breast? i really appriciate your help and if you can help me by e-mail it would be great. Thanks");
}

