define ["jquery", "popcorn"], ($, Popcorn) ->
    makeLesson = (selector, data) ->
        pop = Popcorn(selector)
        for step in data.steps
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: step.text,
                target: "footnote"
            });
    return {
        makeLesson: makeLesson,
    }