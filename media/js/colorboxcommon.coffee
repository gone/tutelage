define ["jquery", "colorbox", "cs!validation"], ($) ->
    return {
        setupColorbox : (selector, href) ->
            form = $(selector).find("form")
            form.validationEngine('hide')
            if href?
                link = href
                inline = false
            else
                link = selector
                inline = true
            $.colorbox
                inline: inline
                href: link
                onComplete:() ->
                    $(selector).find('input[type="text"]').filter(":first").focus()
                onCleanup: () ->
                    form.validationEngine('hide')
        }