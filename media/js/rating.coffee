define ["jquery"], ($) ->
    rateLesson = (event) ->
            star = $(this)
            lesson_id = star.data("lessonid")
            rating = star.prevAll().length + 1
            #TODO: tie this into django's resolve method somehow
            url = "/rate-lesson/#{lesson_id}/#{rating}/"
            $.post(url).success () ->
                star.prevAll().add(star).each (index, value) ->
                    s = $(value)
                    path = s.attr("src")
                    s.attr("src", path.replace("off", "on"))
                star.nextAll().each (index, value) ->
                    s = $(value)
                    path = s.attr("src")
                    s.attr("src", path.replace("on", "off"))



    $(".ratingstar").click(rateLesson)
