// ensure the web page (DOM) has loaded
document.addEventListener( "DOMContentLoaded", function() {

  // Create our popcorn instance
  //Popcorn.player( "baseplayer" );
  //var popcorn = Popcorn.baseplayer( "#baseplayer" );

  // Add YouTube Video and Timeline
  var popcorn  = Popcorn.youtube( "#video", "http://www.youtube.com/watch?v=CIhnDmG4iPM" );
  var timeline = Timeline("timeline", popcorn, 190);

  // add footnotes
  popcorn.footnote({ start: 0, end: 1, target: "footnote", text: "Please press play. " });
  popcorn.footnote({ start: 1, end: 2, target: "footnote", text: "Ready... " });
  popcorn.footnote({ start: 2, end: 5, target: "footnote", text: "Pop! " });
  popcorn.footnote({ start: 5, end: 7, target: "footnote", text: "Thank you. " });
  popcorn.footnote({ start: 7, end: 9, target: "footnote", text: "Thank you very much. " });
  popcorn.footnote({ start: 9, end: 30, target: "footnote", text: "Thank you very " + "very much!" });

  // Create our temptime widget
  var tempTime = TempTime("temptime");
  tempTime.tempTimeClear();
  tempTime.tempMessage("Convection Oven");
  tempTime.tempCelsius(174);
  tempTime.timeMessage("Roasted Herbed Chicken");
  tempTime.timeMainStart(01, 13, 24);
  tempTime.timeSubAStart(00, 15, 41);
  tempTime.timeSubBStart(00, 04, 25);
  tempTime.timeSubCStart(00, 00, 00);
  tempTime.tempTimeMessage("Green Beans on High Broil for 2 min or until golden brown.");

  // play the video right away
  popcorn.play();

}, false );

