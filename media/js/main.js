require({
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "ember": "lib/ember-1.0.pre",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
        "bootstrap": "lib/bootstrap",
        "colorbox": "lib/jquery.colorbox-min",
        "chosen": "lib/chosen.jquery.min",
        "liveValidation": "lib/jquery.validationEngine",
        "liveValidationEn": "lib/jquery.validationEngine-en",
        "popcorn": "lib/popcorn-complete",
    },
    shim:{
        ember: {
            exports: "Ember",
            deps: ['jquery', 'handlebars']
        },
        _: {
            exports: "_",
        },
        bootstrap: {
            deps: ['jquery']
        },
        colorbox: {
            deps: ['jquery']
        },
        chosen: {
            deps: ['jquery']
        },
        liveValidation: {
            deps: ['jquery', "liveValidationEn"]
        },
        popcorn: {
            exports: "Popcorn",
            deps: ['jquery']
        }

    },
        urlArgs: "bust=" +  (new Date()).getTime(),
},
        ["jquery", "ember", "_", "bootstrap", "colorbox", "chosen", "cs!main", "cs!validation", "cs!lessons"], function($, Em, _){
            $(function(){
                if (typeof pagelogic !== "undefined") pagelogic()
            });
        });
