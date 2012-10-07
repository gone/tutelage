require ["jquery", "liveValidation"], ($) ->
    $(document).ready () ->
        $("form").validationEngine();
