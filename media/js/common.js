requirejs.config({
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
        "jqueryui": "lib/jquery-ui-1.9.2.custom.min",
        "bootstrap": "lib/bootstrap",
        "colorbox": "lib/jquery.colorbox-min",
        "chosen": "lib/chosen.jquery.min",
        "liveValidation": "lib/jquery.validationEngine",
        "liveValidationEn": "lib/jquery.validationEngine-en",
        "popcorn": "lib/popcorn-complete",
        "formset":'lib/jquery.formset',
    },
    shim: {
        _: {
            exports: "_"
        },
        bootstrap: {
            deps: ['jquery']
        },
        jqueryui: {
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
        },
        formset: {
            deps: ['jquery']
        },
        fileupload: {
            deps: ['jquery']
        }
    },
    waitSeconds: 30,
    urlArgs: "bust=" +  (new Date()).getTime(),
})
