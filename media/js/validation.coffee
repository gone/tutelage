require ["jquery", "liveValidation"], ($) ->
    $(document).ready () ->
        $("form").validationEngine(
            focusFirstField : false
            showPrompt:true
        )
        $('input[type="submit"]').addClass('disabled')
        $("input").bind "keyup", (event) ->
            form = $(this).parents("form")
            form.data('jqv')['showPrompt'] = false
            isValid = form.validationEngine('validate')
            if isValid == null
                return #this thing isn't thread safe, so typing fast makes it confused
            form.data('jqv')['showPrompt'] = true
            if isValid
                form.find('input[type="submit"]').removeClass('disabled')
            else
                form.find('input[type="submit"]').addClass('disabled')
