/*
Dependencies:
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script type="text/javascript" src="http://cdn.jquerytools.org/1.2.6/form/jquery.tools.min.js"></script>
  <script type="text/javascript" src="http://popcornjs.org/code/dist/popcorn-complete.js"></script>

Links:
  http://jsfiddle.net/popcornjs/qQ672/
  http://popcornjs.org/popcorn-docs/players/
  http://flowplayer.org/tools/rangeinput/
*/

function Timeline(pDivID, pPopcornInstance, pPlayTime)
{
  // utility functions
  var leadingZero = function(pValue, pNone) {
    if (pNone) {
      return "--";
    }
    if (pValue < 10) {
      return "0" + pValue;
    }
    return "" + pValue;
  }
  var timeDisplay = function(pS) {
    var sign;
    var d    = Math.floor((Math.abs(pS) / (60 * 60 * 24)));
    var h    = Math.floor((Math.abs(pS) / (60 * 60)) % 24);
    var m    = Math.floor((Math.abs(pS) / 60) % 60);
    var s    = Math.floor(Math.abs(pS) % 60);

    sign = "";
    if ((60 * 60 * 24) <= Math.abs(pS)) {
      d = d + "d, ";
    } else {
      d = "";
    }
    if ((60 * 60) <= Math.abs(pS)) {
      h = leadingZero(h, Math.abs(pS) < (60 * 60)) + ":";
    } else {
      h = "";
    }
    m = leadingZero(m, Math.abs(pS) < 60) + ":";
    s = leadingZero(s, pS == 0);
    return sign + d + h + m + s;
  }

  // get containing div
  var container = $("#" + pDivID);

  // add play, pause and stop buttons for timeline
  container.append('<button type="button" class="timeline_play"></button>');
  container.append('<button type="button" class="timeline_pause"></button>');
  // container.append('<button type="button" class="timeline_stop"></button>');

  // add time display and set to zero
  container.append('<div class="timeline_time"></div>');
  var addTime = function(pTime) {
    container.find(".current").remove();
    container.find(".max").remove();
    container.find(".timeline_time").append('<div class="current"></div><div class="max"></div>');
    container.find(".current").html(timeDisplay(pTime));
    container.find(".max").html(" / " + timeDisplay(pPlayTime));
  }
  addTime(0);

  // create timeline
  var rangeHTML =
    '<input type="range" class="timeline_frontend" min="0" max="' + pPlayTime + '" step="0.001" value="0" />';
  container.append(rangeHTML);
  container.find(":range").rangeinput({progress: true});


  // define play, pause and stop functions
  var play  = function(pTime) {
    pPopcornInstance.play(pTime);
  };
  var pause = function(pTime) {
    pPopcornInstance.pause(pTime);
  };
  var stop  = function() {
    var doStop = function() {
      pause(0);
      timeline.data("rangeinput").setValue(0);
    };
    doStop();
    // the timeline jumps back in place after stopping
    // this usually solves the problem, but not always
    setTimeout(doStop, 100);
    setTimeout(doStop, 250);
  };

  // update functions
  var switchPlayPause = function() {
    var isPaused = pPopcornInstance.paused();
    container.find(".timeline_play").toggleClass("hidden", !isPaused); // remove is playing
    container.find(".timeline_pause").toggleClass("hidden", isPaused); // remove if paused
  }
  var update = function(pValue) {
    container.find(".current").html(timeDisplay(pValue));
    addTime(pValue);
    switchPlayPause();
  }

  // enable buttons
  container.find(".timeline_play").click(function() { play(); var a_video=document.getElementById("video"); techPlayPause(a_video)});
  container.find(".timeline_pause").click(function() { pause(); });
  // container.find(".timeline_stop").click(function() { stop(); });

  // get timeline and handle
  var timeline = container.find(":range");
  var handle   = container.find(".handle");

  // popcorn updates timeline
  var popcornUpdatesTimeline = function() {
    timeline.data("rangeinput").setValue(this.currentTime());
    update(this.currentTime());
  }
  pPopcornInstance.listen("timeupdate", popcornUpdatesTimeline);

  // slider updates popcorn
  var timelineUpdatesPopcorn = function(pEvent, pValue)
  {
    play(pValue);
    update(pValue);
  };
  timeline.change(timelineUpdatesPopcorn);
  handle.mousedown(function() { pause(); });

  // prepare and return timeline controller
  var result   = {};
  result.play  = play;
  result.pause = pause;
  result.stop  = stop;
  result.time  = function(pTime) { timeline.data("rangeinput").setValue(pTime); };

  // show correct button
  switchPlayPause();

  //add techPlayPause function to slider
  container.find(".slider").click(function() { play(); var a_video=document.getElementById("video"); techPlayPause(a_video)});

  //set width of step buttons in timeline
  //create array
  //loop through all child divs of "timeline_steps" and determine width based on percentage of total
  //ultimate goal is to dynamically build/append each step div
  var sTimelineArray = [];



  // return object
  return result;
}

//pause all other videos when playing an embedded technique video or lesson video
function techPlayPause(a_video) {
	var l_video = document.getElementById("video");
	var t_video = [];

	// Need code to determine how many technique videos are in the lesson, for now assumed
	var i = 0;
	while (i<2) {
		var t_string = 'vid_technique'+(i+1);
		t_video[i] = document.getElementById(t_string);

		if (t_video[i] == a_video) {
			i++;
		}
		else {
			t_video[i].pause();
			i++;
		}
	}

	if (a_video == l_video) {
		a_video.play();
	}
	else if (a_video.paused == true) {
		l_video.pause();
		a_video.play();
	}
	else {
		a_video.pause();
	}
}

//change panel visibility & toggle timeline images when clicked - see http://www.designchemical.com/blog/index.php/jquery/jquery-image-swap-using-click/

function toggle_visibility(name) {
 var id = document.getElementById(name);
 var nClass = $("."+name);
 console.log(nClass);

 if (nClass = '') {
	 if(id.style.display == 'block') {
		id.style.display = 'none';
		}
	 else {
		id.style.display = 'block';
		}
 }
 else if (id != '' ) {
	if(nClass.attr('display') == 'block') {
		nClass.attr('display') = 'none';
		}
	 else {
		nClass.attr('display') = 'block';
		}
 }
 else {
	return;
 }

}

$(".img_swap").live('click', function() {
	if ($(this).attr("id") == "lp_toggle") {
		toggle_visibility('left_panel');
	} else if ($(this).attr("id") == "rp_toggle") {
		toggle_visibility('technique_steps');
		toggle_visibility('timeline_steps');
	}

	if ($(this).attr("class") == "img_swap") {
      this.src = this.src.replace("_off","_on");
    } else {
      this.src = this.src.replace("_on","_off");
    }
	$(this).toggleClass("on");
});

$("#central_panel").live('click', function() {
	toggle_visibility('left_panel');
	toggle_visibility('right_panel');
	toggle_visibility('timeline');
});

$("#vol_toggle").live('click', function() {
	if ($("video").hasClass("muted") == false) {
		$("video").prop('muted', true); //mute
		$("video").addClass("muted");
	}
	else {
		$("video").prop('muted', false); //mute
		$("video").removeClass("muted");
	}
});

// step buttons take video to beginning of selected step
$('.step').live('click',function(){
	if ($(this).attr('id').length > 5) {
		stepTime = step[parseInt($(this).attr('id').substr($(this).attr('id').length - 2))];
	}
	else {
		stepTime = step[parseInt($(this).attr('id').substr($(this).attr('id').length - 1))];
	}

	$("video").get(0).currentTime = stepTime;

	techPlayPause($("video").get(0));

});

//technique buttons to play related technique video
$('.tech_img').live('click',function(){
	var techVidNum = $(this).attr('id').substr($(this).attr('id').length - 1);
	techVideoId = '#vid_technique' + techVidNum;
	techVidTime = step[techVidNum - 1];
	console.log(techVideoId);
	techVid = "#vid_technique2";
	console.log(techVid);

	$("video").get(0).currentTime = techVidTime;

	techPlayPause($(techVideoId).get(0));
});
