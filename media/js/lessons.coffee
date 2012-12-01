define ["jquery", "popcorn"], ($, Popcorn) ->
    makeIngredientText = (ingredient) ->
        return "<span class='panel-item ingredient'> #{ingredient.number} #{ingredient.measurement} #{ingredient.name} #{ingredient.prep} </span>"

    makeToolText = (tool) ->
        return "<span class='panel-item tool'> #{tool.name} #{tool.size} #{tool.type} </span>"

    makeLesson = (selector, data) ->
        pop = Popcorn(selector)
        step_div = $("#step_buttons")

        for step in data.steps
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: step.text,
                target: "step_text"
            });
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: step.title,
                target: "step_title"
            });
            tool_text = [makeToolText(tool) for tool in step.tools]
            ingredient_text = [makeIngredientText(ingredient) for ingredient in step.ingredients]
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: tool_text
                target: "tools"
            })
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: ingredient_text
                target: "ingredient"
            })

            button = makeStepButton(step, pop)
            step_div.append(button)


        return pop
    makeStepButton = (step, pop)->
        button = $("<div id='step-#{ step.order }' class='step'>#{ step.order + 1 }</div>")
        button.on "click", (event) ->
            pop.play(step.start_time)
        pop.code({
            start: step.start_time,
            end: step.end_time or false
            onStart: (options) ->
                $("#step-#{ step.order }").addClass('active')
            onEnd: (options) ->
                $("#step-#{ step.order }").removeClass('active')
            })

        return button

# //pause all other videos when playing an embedded technique video or lesson video
# function techPlayPause(a_video) {
# 	var l_video = document.getElementById("video");
# 	var t_video = [];

# 	// Need code to determine how many technique videos are in the lesson, for now assumed
# 	var i = 0;
# 	while (i<2) {
# 		var t_string = 'vid_technique'+(i+1);
# 		t_video[i] = document.getElementById(t_string);

# 		if (t_video[i] == a_video) {
# 			i++;
# 		}
# 		else {
# 			t_video[i].pause();
# 			i++;
# 		}
# 	}

# 	if (a_video == l_video) {
# 		a_video.play();
# 	}
# 	else if (a_video.paused == true) {
# 		l_video.pause();
# 		a_video.play();
# 	}
# 	else {
# 		a_video.pause();
# 	}
# }

# //change panel visibility & toggle timeline images when clicked - see http://www.designchemical.com/blog/index.php/jquery/jquery-image-swap-using-click/

# function toggle_visibility(name) {
#  var id = document.getElementById(name);
#  var nClass = $("."+name);
#  console.log(nClass);

#  if (nClass = '') {
# 	 if(id.style.display == 'block') {
# 		id.style.display = 'none';
# 		}
# 	 else {
# 		id.style.display = 'block';
# 		}
#  }
#  else if (id != '' ) {
# 	if(nClass.attr('display') == 'block') {
# 		nClass.attr('display') = 'none';
# 		}
# 	 else {
# 		nClass.attr('display') = 'block';
# 		}
#  }
#  else {
# 	return;
#  }

# }

# $(".img_swap").live('click', function() {
# 	if ($(this).attr("id") == "lp_toggle") {
# 		toggle_visibility('left_panel');
# 	} else if ($(this).attr("id") == "rp_toggle") {
# 		toggle_visibility('technique_steps');
# 		toggle_visibility('timeline_steps');
# 	}

# 	if ($(this).attr("class") == "img_swap") {
#       this.src = this.src.replace("_off","_on");
#     } else {
#       this.src = this.src.replace("_on","_off");
#     }
# 	$(this).toggleClass("on");
# });

# $("#central_panel").live('click', function() {
# 	toggle_visibility('left_panel');
# 	toggle_visibility('right_panel');
# 	toggle_visibility('timeline');
# });

# $("#vol_toggle").live('click', function() {
# 	if ($("video").hasClass("muted") == false) {
# 		$("video").prop('muted', true); //mute
# 		$("video").addClass("muted");
# 	}
# 	else {
# 		$("video").prop('muted', false); //mute
# 		$("video").removeClass("muted");
# 	}
# });

# // step buttons take video to beginning of selected step
# $('.step').live('click',function(){
# 	if ($(this).attr('id').length > 5) {
# 		stepTime = step[parseInt($(this).attr('id').substr($(this).attr('id').length - 2))];
# 	}
# 	else {
# 		stepTime = step[parseInt($(this).attr('id').substr($(this).attr('id').length - 1))];
# 	}

# 	$("video").get(0).currentTime = stepTime;

# 	techPlayPause($("video").get(0));

# });

# //technique buttons to play related technique video
# $('.tech_img').live('click',function(){
# 	var techVidNum = $(this).attr('id').substr($(this).attr('id').length - 1);
# 	techVideoId = '#vid_technique' + techVidNum;
# 	techVidTime = step[techVidNum - 1];
# 	console.log(techVideoId);
# 	techVid = "#vid_technique2";
# 	console.log(techVid);

# 	$("video").get(0).currentTime = techVidTime;

# 	techPlayPause($(techVideoId).get(0));
# });










    return {
        makeLesson: makeLesson,
    }
