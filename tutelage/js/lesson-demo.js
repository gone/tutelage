// ensure the web page (DOM) has loaded
document.addEventListener( "DOMContentLoaded", function() {

/*
  // Create timeline and pause baseplayer
  Popcorn.player( "baseplayer" );
  var baseplayer = Popcorn.baseplayer( "#baseplayer" );
  baseplayer.pause();
  var timeline   = Timeline("timeline", baseplayer, 190);

  // Add YouTube video and create timeline
  var video = Popcorn.youtube( "#video", "http://www.youtube.com/watch?v=CIhnDmG4iPM" );
  var timeline = Timeline("timeline", video, 190);
  video.pause();
 */

  // Create a popcorn instance by calling Popcorn("#id-of-my-video")
  var video    = Popcorn( "#video" );
  var timeline = Timeline("timeline", video, 208.7);
  video.pause();

  // load lesson timing
  // MyLessonTiming(baseplayer, tempTime);
  MyLessonTiming(video);

}, false );

