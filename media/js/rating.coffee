define ["jquery"], ($) ->
    rateLesson = (event) ->
            star = $(this)
            starContainer = star.parent()
            lesson_id = star.data("lessonid")
            rating = starContainer.prevAll().length + 1
            #TODO: tie this into django's resolve method somehow
            url = "/rate-lesson/#{lesson_id}/#{rating}/"
            $.post(url).success () ->
                starContainer.prevAll().add(starContainer).each (index, value) ->
                    s = $(value).children()
                    path = s.attr("src")
                    s.attr("src", path.replace("off", "on"))
                star.nextAll().each (index, value) ->
                    s = $(value).children()
                    path = s.attr("src")
                    s.attr("src", path.replace("on", "off"))


    shrinkGrow = (height, width) ->
        return (event) ->
            $(this).animate({
                'height': height
                'width': width
            },{
                duration: 100,
            });


    $(".ratingstar").click(rateLesson)
    $(".starcontainer").on('mouseover', '.ratingstar', shrinkGrow(30, 29))
    $(".starcontainer").on('mouseout', '.ratingstar', shrinkGrow(26, 25))
