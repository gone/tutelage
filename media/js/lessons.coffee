define ["jquery", "popcorn"], ($, Popcorn) ->
    makeIngredientText = (ingredient) ->
        return "<span class='ingredient'> #{ingredient.number} #{ingredient.measurement} #{ingredient.name} #{ingredient.prep} </span>"

    makeToolText = (tool) ->
        return "<span class='tool'> #{tool.name} #{tool.size} #{tool.type} </span>"

    makeLesson = (selector, data) ->
        pop = Popcorn(selector)
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

    return {
        makeLesson: makeLesson,
    }