require ["jquery", "chosen", "cs!validation"], ($) ->
    $(document).ready () ->
        setupColorbox = (selector, href) ->
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

        $(".login-btn").click () ->
            setupColorbox("#login")

        $(".signup-btn").click () ->
            setupColorbox("#signup")
		
		$(".create-lesson-help-btn").click () ->
            setupColorbox("#lesson-help")
		
        $(".forgot-pass-btn").click () ->
            setupColorbox("#forgot-password")

        $(".changepass-btn").click () ->
            setupColorbox("#change-password")

        $(".cancel-btn").click () ->
            $.colorbox.close()

        $(".miniprofile-btn").click (e) ->
            href = $(this).attr("href")
            setupColorbox(this, href)
            return false

        $(".chzn").chosen()
        $('.carousel').carousel(
          interval: false
        )

        $window = $(window)
        $window.scroll () ->
            if $window.scrollTop() > $('header .navbar').position().top
                $('header').addClass("fixed-top")
            else
                $('header').removeClass("fixed-top")
