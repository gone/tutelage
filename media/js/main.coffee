require ["jquery", "cs!validation"], ($) ->
    $(document).ready () ->
        setupColorbox = (selector) ->
            form = $(selector).find("form")
            form.validationEngine('hide')

            $.colorbox
                inline: true
                href: selector
                onComplete:() ->
                    $(selector).find('input[type="text"]').filter(":first").focus()


        $(".login-btn").click () ->
            setupColorbox("#login")

        $(".signup-btn").click () ->
            setupColorbox("#signup")

        $(".forgot-pass-btn").click () ->
            setupColorbox("#forgot-password")

        $(".cancel-btn").click () ->
            $.colorbox.close()
