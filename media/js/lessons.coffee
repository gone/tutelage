define ["jquery", "popcorn"], ($, Popcorn) ->
    makeLesson = (selector, data) ->
        pop = Popcorn(selector)
        for step in data.steps
            pop.footnote({
                start: step.start_time,
                end: step.end_time or false
                text: step.text,
                target: "step"
            });
            tool_text = [tool.name + " " + tool.size + " " + tool.type + "<br>" for tool in step.tools]
            ingredient_text = [ingredient.number + " " + ingredient.measurement + ingredient.name + " " + ingredient.prep +  "<br>" for ingredient in step.ingredients]
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

    return {
        makeLesson: makeLesson,
    }