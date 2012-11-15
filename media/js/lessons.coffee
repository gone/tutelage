require ["jquery", "popcorn"], ($, Popcorn) ->

    #set ingredient
    #set tool

    makeLesson = (selector, data) ->
        pop = Popcorn(selector)
        for step in steps
            pop.footnote({
               start: step.start_time,
               text: step.text,
               target: "footnote"
            });