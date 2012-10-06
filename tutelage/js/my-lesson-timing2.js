/*
This file puts all lesson timing in one place.

Dependencies:
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
  <script type="text/javascript" src="http://popcornjs.org/code/dist/popcorn-complete.js"></script>
*/
function MyLessonTiming(pVideo, pTempTime) {

  /*** utility functions ***/
  // image control utility functions
  var setImage = function(pStart, pEnd, pTarget, pImage, pCaption, pClass, pLink) {
    pVideo.footnote({ start: pStart, end: pEnd, target: pTarget, text:
      '<a href="' + pLink + '" target="_blank" class="' + pClass + '"><img src="' + pImage + '" alt=""></img>' +
      '<div class="caption">' + pCaption + '</div></a>'
    });
    // pVideo.image({ start: pStart, end: pEnd, // seconds
    //   href: "",
    //   src: pImage,
    //   text: "",
    //   target: pTarget
    // });
  }
  var setIngredient = function(pStart, pEnd, pIngredient, pCaption, pClass, pLink) {
    var image = "./img/icon_" + pIngredient + ".png";
    setImage(pStart, pEnd, "ingredients", image, pCaption, pClass, pLink);
  }
  var setTool = function(pStart, pEnd, pTool, pCaption, pClass, pLink) {
    var image = "./img/icon_" + pTool + ".png";
    setImage(pStart, pEnd, "tools", image, pCaption, pClass, pLink);
  }

/*** Template
  pVideo.code({ start: 0, end: 0, // seconds
    onStart: function(pOptions) {
    },
    onFrame: function(pOptions) {
    },
    onEnd: function(pOptions) {
    }
  });
 */

  // step timing variables
  // step[0] = video start
  // all other steps match text
  var video_start =   0.0;
  var video_end   = 208.7;
  var step = [
    video_start,
      5.5,    // step  1 - recipe  1
     11.5,    // step  2 - recipe  2
     24.0,    // step  3 - recipe  3
     31.0,    // step  4 - recipe  4
     47.5,    // step  5 - recipe  5
     64.0,    // step  6 - recipe  6
     93.0,    // step  7 - recipe  7
    133.0,    // step  8 - recipe  8
    156.0,    // step  9 - recipe  9
    163.5,    // step 10 - recipe 10
    video_end
  ];
  var bonus = [
    video_start,
      2.0,    // bonus  1 - intro song
    173.5,    // bonus  2 - Cartman
    179.0,    // bonus  3 - image 0
    182.5,    // bonus  4 - image 1
    186.0,    // bonus  5 - image 2
    189.5,    // bonus  6 - image 3
    193.0,    // bonus  7 - image 4
    196.5,    // bonus  8 - image 5
    200.0,    // bonus  9 - image 6
    203.5,    // bonus 10 - image 7
    207.0,    // bonus 11 - ending logo
    video_end
  ];

  // STEP 0 & STEP 1 TEXT
  pVideo.footnote({ start: video_start, end: step[2], target: "directions", text:
    "<h1 class='step_numbers'>Step 1:</h1>" +
    "Collect all ingredients and tools to create what's called your mise-en-place.<br/>" +
    "<br/>" +
    ""
  }); 

  pVideo.footnote({ start: video_start, end: step[2], target: "toolsings", text:
    "<h1>Ingredients:</h1><br/>" +
    "2 refrigerated pie crusts, softened<br/>" +
    "1/3 cup butter or margarine <br/>" +
    "1/3 cup chiffonade green onion<br/>" +
    "1/3 cup all-purpose flour<br/>" +
    "1/2 teaspoon salt<br/>" +
    "1/4 teaspoon pepper<br/>" +
    "1/2 cup milk<br/>" +
    "1 can chicken broth<br/>" +
    "2 1/2 cups shredded cooked chicken<br/>" +
    "2 cups mixed vegetables, thaw if frozen<br/>" +
    "<br/>" +
    "<h1>Tools:</h1><br/>" +
    "Oven<br/>" +
    "9\" Pie Plate (glass preferred)<br/>" +
    "2-Quart Saucepan<br/>" +
    "Chef's Knife<br/>" +
    "Stirring Spoon<br/>" +
    "Aluminum Foil/Pie Shield<br/>" +
    ""
  }); 
  
  pVideo.footnote({ start: video_start, end: step[1], target: "links", text:
    '<a href="http://en.m.wikipedia.org/wiki/Pot_pie" target="_blank">Wiki: Pot Pie</a><br/>' +
    '<a href="http://caloriecount.about.com/calories-chicken-pot-pie-i22906" target="_blank">Nutritional Information</a><br/>' +
    ''
  });

  // STEP 1
  setTool(      step[1], step[2], "knife",   "chef's knife",  "default","http://www.surlatable.com/search/searchContainer.jsp?q=chef%20knife&s=true");
  setTool(      step[1], step[2], "board", "cutting board", "default","http://www.surlatable.com/search/searchContainer.jsp?q=cutting%20board&s=true");
  pVideo.footnote({ start: step[1], end: step[3], target: "links", text:
    '<a href="http://en.wikipedia.org/wiki/Mise_en_place">Wiki: mise-en-place</a><br/>' +
    '<a href="http://www.youtube.com/watch?v=yJEQFgfv7iw">How to Chiffonade</a><br/>' +
    '<a href="http://m.youtube.com/index?desktop_uri=%2F&gl=US#/watch?v=bjQ0GSSVymU">Pie Crust from Scratch</a><br/>' +
    '<a href="http://www.elledecor.com/elle-decor/articles/chicken-stock-recipes">Homemade Chicken Broth Recipe</a><br/>' +
    ''
  });

  // STEP 2
  pVideo.footnote({ start: step[2], end: step[3], target: "directions", text:
    "<h1 class='step_numbers'>Step 2:</h1>" +
    "Preheat oven to 425*F/218*C, unroll pie crust and fit to lay in pie plate.<br/>" +
    ""
  });
  setIngredient(step[2], step[3], "pie_crust", "pie crust", "pie_crust","http://fresh.amazon.com/Search?input=pie+crust");
  setTool(      step[2], step[3], "plate", "pie plate", "pie_plate","http://www.surlatable.com/search/searchContainer.jsp?q=pie%20plate&s=true");

  // STEP 3
  pVideo.footnote({ start: step[3], end: step[4], target: "directions", text:
    "<h1 class='step_numbers'>Step 3:</h1>" +
    "In 2-Quart saucepan, melt butter over medium heat. Add onion; cook and stir 2 minutes or until tender.<br/>" +
    ""
  });
/*** Hide Saucepan
  setTool(      step[3], step[7], "ladle",      "ladle",    "default"); // display first
  setTool(      step[3], step[4], "saucepan",   "saucepan", "default"); // display first
  setTool(      step[5], step[7], "saucepan",   "saucepan", "default"); // display first
 */
/*** Hide Ladle
  setTool(      step[3], step[7], "saucepan",   "saucepan", "default"); // display first
  setTool(      step[3], step[4], "ladle",      "ladle",    "default"); // display first
  setTool(      step[5], step[7], "ladle",      "ladle",    "default"); // display first
 */
/*** Show Both
 */
  setTool(      step[3], step[7], "ladle",      "ladle",    "default"); // display first
  setTool(      step[3], step[7], "saucepan",   "saucepan", "default"); // display first
/*** Everything Else
 */
  setIngredient(step[3], step[4], "onion", "green onions", "green_onion");
  // setIngredient(step[3], step[4], "onion",      "onions",       "green_onion"); // green onions
  setTool(      step[3], step[4], "measuring_cup",    "1/3 cup",      "green_onion");
  setIngredient(step[3], step[4], "margarine",  "margarine",    "margarine");
  setTool(      step[3], step[4], "measuring_cup",    "1/3 cup",      "margarine");
  pVideo.footnote({ start: step[3], end: step[4], target: "links", text:
    '<a href="http://sliceoflifesunday.wordpress.com/the-history-of-pie/">History of Pot Pie</a><br/>' +
    ''
  });

  // STEP 4
  pVideo.footnote({ start: step[4], end: step[5], target: "directions", text:
    "<h1 class='step_numbers'>Step 4:</h1>" +
    "Stir in flour, salt and pepper until well blended. Cook 1 to 2 minutes, stirring constantly.<br/>" +
    ""
  });
  setIngredient(step[4], step[5], "flour",      "flour",        "flour");  // use "Flour" or "Flour_2"
  setTool(      step[4], step[5], "measuring_cup",      "1/3 cup",      "flour");
  setIngredient(step[4], step[5], "spice",         "salt",         "salt");
  setTool(      step[4], step[5], "ladle", "1/2 teaspoon", "salt");
  setIngredient(step[4], step[5], "spice",       "pepper",       "pepper");
  setTool(      step[4], step[5], "ladle", "1/4 teaspoon", "pepper");
  pVideo.footnote({ start: step[4], end: step[7], target: "links", text:
    '<a href="http://www.skinnytaste.com/2011/01/chicken-pot-pie-soup.html">Skinny Taste: Chicken Pot Pie Soup</a><br/>' +
    '<a href="http://thehealthyfoodie.net/2011/12/29/chicken-pot-pie/">The Healthy Foody: Chicken Pot Pie</a><br/>' +
    '<a href="http://www.sheknows.com/food-and-recipes/articles/803945/healthy-chicken-pot-pie">She Knows: Healthy Chicken Pot Pie</a><br/>' +
    '<a href="http://www.cookingforengineers.com/recipe/42/Traditional-Chicken-Pot-Pie">Cooking for Engineers: Traditional Pot Pie</a><br/>' +
    ''
  });

  // STEP 5
  pVideo.footnote({ start: step[5], end: step[6], target: "directions", text:
    "<h1 class='step_numbers'>Step 5:</h1>" +
    "Gradually stir in milk and chicken broth, cooking and stirring until simmering and thickened.<br/>" +
    ""
  });
  setIngredient(step[5], step[6], "milk",         "milk",          "milk");
  setTool(      step[5], step[6], "measuring_cup",      "1/2 cup",       "milk");
  setIngredient(step[5], step[6], "chicken", "chicken broth", "chicken_broth");
  setTool(      step[5], step[6], "measuring_cup", "14 ounces",     "chicken_broth");

  // STEP 6
  pVideo.footnote({ start: step[6], end: step[7], target: "directions", text:
    "<h1 class='step_numbers'>Step 6:</h1>" +
    "Stir in cooked and shredded chicken as well as thawed mixed vegetables. " +
    "Remove from heat. Spoon chicken mixture into crust-lined pie plate.<br/>" +
    ""
  });
  setIngredient(step[6], step[7], "chicken", "shredded chicken", "chicken_shredded");
  setTool(      step[6], step[7], "measuring_cup",         "1 cup",            "chicken_shredded");
  setIngredient(step[6], step[7], "vegetables",  "mixed vegetables", "vegetables_mixed");
  setTool(      step[6], step[7], "measuring_cup",         "1 cup",            "vegetables_mixed");

  // STEP 7
  pVideo.footnote({ start: step[7], end: step[8], target: "directions", text:
    "<h1 class='step_numbers'>Step 7:</h1>" +
    "Roll out and top with second crust; seal edge and flute.<br/>" +
    "Slit vents in several places in top crust (1/2\" - 1\" long)<br/>" +
    "<br/>" +
    ""
  });
  setIngredient(step[7], step[9], "pie_crust",        "pie crust",    "pie_crust");
  setTool(      step[7], step[8], "knife",     "paring knife", "pie_crust");
  pVideo.footnote({ start: step[7], end: step[8], target: "links", text:
    '<a href="http://www.youtube.com/watch?v=zO5gsFKZoA8&feature=youtube_gdata_player">Fluting</a><br/>' +
    ''
  });

  // STEP 8
  pVideo.footnote({ start: step[8], end: step[9], target: "directions", text:
    "<h1 class='step_numbers'>Step 8:</h1>" +
    "Cover crust edge with a Pie Shield 2- to 3-inch-wide strips of foil to prevent " +
    "excessive browning (you will remove foil during last 15 minutes of baking).<br/>" +
    ""
  });
  setTool(      step[8], step[9], "pie_shield",     "pie shield",     "pie_crust");
  setTool(      step[8], step[9], "foil", "aluminium foil", "pie_crust");
  pVideo.footnote({ start: step[8], end: step[9], target: "links", text:
    '<a href="http://www.amazon.com/Andersons-Baking-9-inch-Aluminum-Shield/dp/B0006GT4BY">Get your own Pie Shield</a><br/>' +
    ''
  });

  // STEP 9
  pVideo.footnote({ start: step[9], end: step[10], target: "directions", text:
    "<h1 class='step_numbers'>Step 9:</h1>" +
    "Bake 30 to 40 minutes or until crust is golden brown.<br/>" +
    ""
  });
  setIngredient(step[9], video_end, "pie", "chicken pot pie", "chicken_pot_pie");
  setTool(      step[9], step[10], "oven",          "oven",            "chicken_pot_pie");
  pVideo.footnote({ start: step[9], end: step[10], target: "links", text:
    '<a href="http://www.nytimes.com/2010/03/10/dining/10mini.htm">NYTimes: How to Top Chicken Pot Pie</a><br/>' +
    '<a href="http://www.huffingtonpost.com/mobileweb/2012/03/01/kfc-chunky-chicken-pot-pie_n_1312800.html">Huffington Post: KFC\'s Chunky Chicken Pot Pie</a><br/>' +
    '<a href="http://www.npr.org/templates/story/story.php?storyId=6949446">NPR: Pot Pie Reclaiming its place</a><br/>' +
    ''
  });

  // STEP 10
  pVideo.footnote({ start: step[10], end: bonus[2], target: "directions", text:
    "<h1 class='step_numbers'>Step 10:</h1>" +
    "Let stand 15 to 20 minutes before serving.<br/>" +
    ""
  });
  pVideo.footnote({ start: step[10], end: bonus[2], target: "links", text:
    '<a href="http://seattlemag.com/article/dining/reviews/comfort-food-pot-pies">Seattle Mag</a><br/>' +
    '<a href="http://www.yelp.com/search?find_desc=chicken+pot+pie&find_loc=Seattle%2C+WA">Yelp</a><br/>' +
    '<a href="http://chowhound.chow.com/topics/378440">Chowhound</a><br/>' +
    ''
  });

  // BONUS 1
  // do nothing

  // BONUS 2
  pVideo.footnote({ start: bonus[2], end: video_end, target: "directions", text:
    "<h1>Step 11:</h1><br/>" +
    "Enjoy!<br/>" +
    ""
  });
  setTool(      bonus[2], video_end, "plate",           "plate",           "chicken_pot_pie");
  setTool(      bonus[2], video_end, "fork",            "fork",            "chicken_pot_pie");
  pVideo.footnote({ start: bonus[2], end: bonus[3], target: "links", text:
    'Most early cookbooks do not contain recipes for "pot pie." This was a description of cooking method rather than a recipe.<br/>' +
    '<br/>' +
    'Traditionally made with carrots, peas, potatoes,celery and herbs.<br/>' +
    '<br/>' +
    '1839: Oldest American pot pie recipe<br/>' +
    '<br/>' +
    'The first frozen pot pie was made with chicken in 1951 by the C. A. Swanson Company.<br/>' +
    '<br/>' +
    'Savory Pies date back to the middle ages<br/>' +
    '<br/>' +
    '"The term [potpie], which first appeared in American print in 1785, probably refers to the deep pie pans or pots used to bake pies in, and it has remained primarily an Americanism."<br/>' +
    '---Encyclopedia of American Food and Drink<br/>' +
    ''
  });
 
  // BONUS 3
  pVideo.footnote({ start: bonus[3], end: bonus[4], target: "links", text:
    '<a href="http://culinaryarts.about.com/od/knivescutlery/ss/anat-knife.htm">Anatomy of a Chef\'s Knife</a><br/>' +
    '<a href="http://www.foodnetwork.com/healthy-meal-makeover-chicken-pot-pie/package/index.html">Healthy Pot Pies</a><br/>' +
    '<a href="http://www.cookinglight.com/m/eating-smart/recipe-makeovers/healthy-chicken-potpie-recipes-00412000067896/">More Healthy Pot Pies</a><br/>' +
    ''
  });
 
  // BONUS 4
  pVideo.footnote({ start: bonus[4], end: bonus[5], target: "links", text:
    'Traditionally made with carrots, peas, potatoes,celery and herbs.<br/>' +
    '<br/>' +
    'Dates to the Middle Ages<br/>' +
    ''
  });
 
  // BONUS 5
  pVideo.footnote({ start: bonus[5], end: bonus[6], target: "links", text:
    '"To make a pot Pie. Make a crust and put it round the sides of your pot, then cut your meat in small pieces, of whatever kind the pot pie is to be made of, and season it with pepper and salt, then put it in the pot and fill it with water, close it with paste on the top; it will take three hours doing."<br/>' +
    '---The Art of Cookery Made Plain and Easy, Mrs. [Hannah] Glasse, a new Edition with modern Improvements, facsimile 1805edition printed by Cottom and Stewart and sold at their Book-Stores in Alexandria and Fredericksburg 1805, introduction by Karen Hess [Applewood Books:Bedford MA] 1997 (p. 144)<br/>' +
    ''
  });
 
  // BONUS 6
  pVideo.footnote({ start: bonus[6], end: bonus[7], target: "links", text:
    'Oldest American pot pie recipe.<br/>' +
    '<br/>' +
    'Rub the bottom and sides of a porridge-pot, or small oven, with butter, and then with dry flour. Roll out some pieces of plain or standing paste about half an inch thick, line the sides of the pot or oven with the pieces of paste, letting them nearly touch the bottom. Having pared and sliced from the cores some fine cooking apples, nearly fill the oven with them; pour in enough water to cook them tender, put pieces of paste on the top, or put a paste all over the top, and bake it with moderate heat, having a fire both on and under the oven. When the apples are very soft, the crust brown, and the liquor quite low, turn the crust bottom upwards in a large dish, put the apples evenly over it, strew on a large handful of brown sugar, and eat it warm or cold, with sweet milk. This is quite a homely pie, but a very good one.<br/>' +
    '---the Kentucky Housewife, Lettice Bryan, facsimile reprint of 1839 edition stereotyped by Shepard & Stearns:Cincinnati [Image Graphics:Paducah KY] (p. 267-8)<br/>' +
    '<br/>' 
  });
 
  // BONUS 7
  pVideo.footnote({ start: bonus[7], end: bonus[8], target: "links", text:
    'A Peach pot pie, or cobler, as it is often termed, should be made of clingstone peaches, that are very ripe, and then pared and sliced from the stones. Prepare a pot or oven with paste, as directed for the apple pot-pie, put in the prepared peaches, sprinkle on a large handful of brown sugar, pour in plenty of water to cook the peaches without burning them, though there should be but very little liquor or syrup when the pie is done. Put a paste over the top, and bake it with moderate heat, raising the lid occasionally, to see how it is baking. When the crust is brown, and the peaches very soft, invert the crust on a large dish, put the peaches evenly on, and grate loaf sugar thickly over it. Eat it warm or cold. Although it is not a fashionable pie for company, it is very excellent for family use, with cold sweet milk.<br/>' +
    '---ibid (p. 268)<br/>' +
    ''
  });
 
  // BONUS 8
  pVideo.footnote({ start: bonus[8], end: bonus[9], target: "links", text:
	'<h1>1845 Pot Pie or Soup</h1><br/>' +
    'Scraps and crumbs of meat make a very good dinner, when made into soup. Put all your crumbs of meat into the dinner-pot. Slice in two onions, a carrot; put in a little salt and pepper, and water enough to cover it; then cover it with a crust, made with cream tartar...Stew it one hour and a half, or two hours. A flour thickening should be put in five minutes before you take it up. You make bake your potatoes, or slice them, and cooke them with the meat.<br/>' +
    '---The New England Economical Housekeeper and Family Receipt Book, Mrs. E.A. Howland [E.P. Walton and Sons:Montpelier VT] 1845 (p. 56)<br/>' +
    '<br/>'+
    '<h1>1877</h1><br/>' +
    '<a href="http://digital.lib.msu.edu/projects/cookbooks/display.cfm?TitleNo=40&PageNum=249">Chicken pot pie</a>, Buckeye Cookery, Estelle Woods Wilcox<br/>' +
    ''
  });
 
  // BONUS 9
  pVideo.footnote({ start: bonus[9], end: bonus[10], target: "links", text:
    '<h1>1951 First frozen pot pie</h1><br/>' +
    'Most early cookbooks do not contain recipes for "pot pie." This was a description of cooking method rather than a recipe. Notes here:<br/>' +
    'Potpie....A crusted pie made with poultry or meat, and, usually chopped vegetables. The term, which first appeared in American print in 1785, probably refers to the deep pie pans or pots used to bake pies in, and it has remained primarily an Americanism. The most popular pot pies have been chicken, Beef, and pork. The first frozen pot pie was made with chicken in 1951 by the C. A. Swanson Company.<br/>' +
    '---Encyclopedia of American Food and Drink, John F. Mariani [Lebhar-Friedman:New York] 1999 (p. 254)<br/>' +
    '<br/>' +
    'Pot pies have a long history in most Northern European cuisines, and if they were a specialty anywhere, it was in the British Isles. And a pot pie must be made in a pot that is completely lined with crust. Originally, this crust was not eaten; it was there to keep the taste of the iron pot away from the food.<br/>' +
    '---"ONE CRUST OR TWO?" Leslie Land, Los Angeles Times, September 24, 1992 (p. H11)<br/>' +
    '<br/>' +
    'Pot pies are as old as pastry-making itself. In the royal households of France and England, savory tarts were among a chef\'s most elaborate dishes...Sad to say, pot pies seem a relic of an age of family restaurants where a cook actually took his time to make such items--before such restaurants were conglomerated and homogenized. The last steamy gasp of the traditional pot pie may well have been the arrival of the frozen pot pie in supermarkets of the early 1950s, which made the idea of making one at home or in a restaurant obsolete, despite the lack of fresh flavor...Pot pies are as old as pastry making itself. And in the royal households of France and England, savory tarts were often among the most elaborate of dishes in a chef\'s repertoire, especially during the Elizabethan era, when the crusts would be decorated with heraldic devices, flowers, and curlicues of painstaking skill. Inside might be anything at all, including the famous "four-and-twenty blackbirds" or even a small child (unbaked and uneaten, I assure you). In America, where far more households had baking ovens than in Europe, the tart became known as the pot pie by the end of the 18th century, and was a fixture of American kitchens. In most cases it referred to a casserole dish topped with a pastry crust rather than to a mixture of ingredients baked in a pastry crust, so that the casserole could easily be hung above the fire or set on a grid to be baked by indirect heat. They were particularly welcome at church suppers because they were so easy to transport and were very festive at any family table.<br/>' +
    '---"POT PIES," John Mariani & Gail Bellamy, Restaurant Hospitality, April 1998 (p. 80)<br/>' +
    ''
  });
 
  // BONUS 10
  pVideo.footnote({ start: bonus[10], end: bonus[11], target: "links", text:
    '<h1>About chicken pot pie</h1><br/>' +
    'Primary evidence suggests recipes for chicken pot pie (in concept, but not name) were known in England as far back as the Middle Ages. As one would expect, these early meat pies were quite different from ones we know today. Robert May\'s Accomplist Cook [1685] lists several recipes for poultry pies (chicken, turkey, pheasant etc.). These generally still relied on Medieval flavors: pepper, salt, nutmeg, orange juice, lemon, chestnuts, mace, sugar, gooseberries, barberries, grapes etc. Vegetables were sometimes employed:<br/>' +
    '" artichock bottoms, or the tops of boild sparagus...Otherways for the liquoring or garnishing of these Pies, for variety you may put in them boil\'d skirrets, bottom of artichokes boil\'d, or boil\'d cabbidge lettice...whole onions being baked...Or bake them with candied lettice stalks, potatoes..."<br/>' +
    '---The Accomplisht Cook, Robert May, facsimile 1685 edition [Prospect Books:Devon] 2000 (p. 212-3)<br/>' +
    '<br/>' +
    'The oldest recipe we know (so far) specifically titled "pot pie" was published in the 1805 American edition of a classic English cook book. Hannah Glasse\'s Art of Cookery Made Plain and Easy classified "Pot Pie" in a special section titled "Several New Receipts Adapted To The American Mode of Cooking," This print evidence cements the "American-ness" of the Pot Pie. This book also offered "American" recipes for Indian Pudding, Mush, Buck-Wheat Cakes, Pumpkin Pie, Dough Nuts, Sausages, Blood Puddings, Cranberry Tarts, pickled peppers, pickled Beets, Peach Sweetmeats,, Quince Sweetmeats, Green Gage Sweetmeats, Maple Sugar, maple Molasses, Maple Beer, "famous" Thieves Vinegar, Spruce Beer, Eel Pie, Pork pie, raised Pork Pie, Bath Pudding, Short Gingerbread, Waffles & Crullers.<br/>' +
    ''
  });
 
  // BONUS 11
  pVideo.footnote({ start: bonus[11], end: video_end, target: "links", text:
    'Thanks for watching!  Move the timeline to review anything you missed.<br/>' +
    ''
  });

  // temptime control
  pTempTime.clear();
  pTempTime.redraw();
  pVideo.exec(step[2], function () {
    pTempTime.main.time.init("preheat", "./img/icon_oven.png", "Preheat Oven", "").start(00, 05, 00);
    pTempTime.main.temp.init("oven", "./img/icon_oven.png", "Oven", "").fahrenheit(425);
    pTempTime.redraw();
  });
  pVideo.exec(step[3], function () {
    pTempTime.sub[0].time.init("onion", "./img/icon_onion.png", "Melt Butter and Add Onion", "").start(00, 01, 00);
    pTempTime.sub[0].temp.init("big_burner", "./img/icon_burner_big.png", "Big Burner", "").details("Medium Heat");
    pTempTime.redraw();
  });
  pVideo.exec(step[4], function () {
    pTempTime.sub[1].time.init("flour", "./img/icon_flour.png", "Stir in Flour Salt and Pepper", "").start(00, 01, 30);
    pTempTime.sub[1].temp.init("big_burner", "./img/icon_burner_big.png", "Big Burner", "").details("Medium Heat");
    pTempTime.redraw();
  });
  pVideo.exec(step[5], function () {
    pTempTime.sub[2].time.init("chicken_broth", "./img/icon_chicken.png", "Stir in Milk and Chicken Broth", "").start(00, 04, 00);
    pTempTime.sub[2].temp.init("big_burner", "./img/icon_burner_big.png", "Big Burner", "").details("Medium Heat");
    pTempTime.redraw();
  });
  pVideo.exec(step[6], function () {
    pTempTime.sub[3].time.init("chicken_shredded", "./img/icon_vegetables.png", "Add Chicken and Mixed Vegetables", "").start(00, 05, 00);
    pTempTime.sub[3].temp.init("big_burner", "./img/icon_burner_big.png", "Big Burner", "").details("Medium Heat");
    pTempTime.redraw();
  });
  pVideo.exec(step[8], function () {
    pTempTime.sub[4].time.init("foil", "./img/icon_pie.png", "Baking with Foil", "").start(00, 20, 00);
    pTempTime.sub[4].temp.init("oven", "./img/icon_oven.png", "Oven", "").fahrenheit(425);
    pTempTime.redraw();
  });
  pVideo.exec(step[9], function () {
    pTempTime.sub[5].time.init("foil", "./img/icon_pie.png", "Baking after Foil", "").start(00, 15, 00);
    pTempTime.sub[5].temp.init("oven", "./img/icon_oven.png", "Oven", "").fahrenheit(425);
    pTempTime.redraw();
  });
  pVideo.exec(step[10], function () {
    pTempTime.sub[6].time.init("pie", "./img/icon_pie.png", "Let Cool", "").start(00, 15, 00);
    pTempTime.sub[6].temp.init("countertop", "./img/icon_countertop.png", "Countertop", "").details("Room Temperature");
    pTempTime.redraw();
  });
}

