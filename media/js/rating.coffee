define ["jquery"], ($) ->
    rateLesson = (event) ->
            star = $(this)
            starContainer = star.parent()
            lesson_id = star.data("lessonid")
            rating = starContainer.prevAll().length + 1
            #TODO: tie this into django's url resolve method
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


    mouseOver = () ->
        container = $(this)
        container.parent().prevAll().children().add(container).addClass('goldstar')
        container.parent().nextAll().children().addClass('whitestar')



    mouseOut = () ->
        $(this).find('img').removeClass('whitestar').removeClass('goldstar')


    shrinkGrow = (height, width) ->
        return (event) ->
            $(this).animate({
                'height': height
                'width': width
            },{
                duration: 100,
            });


    $(".ratingstar").click(rateLesson)
    $(".starcontainer").on('mouseover', '.ratingstar', mouseOver)
    $(".ratingblock").parent().on('mouseout',  mouseOut)
