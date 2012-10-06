$(document).ready () ->
    $(".login-btn").click () ->
        $.colorbox
            inline: true
            href: "#login"
    $(".signup-btn").click () ->
        $.colorbox
            inline: true
            href: "#signup"
    $(".forgot-pass-btn").click () ->
        $.colorbox
            inline: true
            href: "#forgot-password"
    $(".cancel-btn").click () ->
        $.colorbox.close()
