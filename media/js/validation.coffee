require ["jquery", "liveValidation"], ($) ->
    is_valid = (form) ->
        if form.length == 0
            return true
        form.data('jqv')['showPrompt'] = false
        isValid = form.validationEngine('validate')
        if isValid == null
            return #this thing isn't thread safe, so typing fast makes it confused
        form.data('jqv')['showPrompt'] = true
        if isValid
            form.find('input[type="submit"]').removeClass('disabled')
        else
            form.find('input[type="submit"]').addClass('disabled')

    $(document).ready () ->
        forms = $("form")
        forms.validationEngine(
            focusFirstField : false
            showPrompt:true
            scroll:false
        )

        forms.each (idx, form) ->
            is_valid($(form))

        $("input").bind "keyup", (event) ->
            form = $(this).parents("form")
            is_valid(form)