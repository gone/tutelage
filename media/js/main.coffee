require ["jquery", "cs!colorboxcommon", "chosen", "cs!validation"], ($, cc) ->
    $(document).ready () ->

        $(".login-btn").click () ->
            cc.setupColorbox("#login")

        $(".signup-btn").click () ->
            cc.setupColorbox("#signup")

		$(".create-lesson-help-btn").click () ->
            cc.setupColorbox("#lesson-help")

        $(".forgot-pass-btn").click () ->
            cc.setupColorbox("#forgot-password")

        $(".changepass-btn").click () ->
            cc.setupColorbox("#change-password")

        $(".cancel-btn").click () ->
            $.colorbox.close()

        $(".miniprofile-btn").click (e) ->
            href = $(this).attr("href")
            cc.setupColorbox(this, href)
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
