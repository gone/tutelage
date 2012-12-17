requirejs.config({
    paths: {
        "text": "require/text",
        "cs": "require/cs",
        "handlebars" : "lib/handlebars-1.0.0.beta.6",
        "_": "lib/underscore-min",
        "jquery": "require/require-jquery",
        "bootstrap": "lib/bootstrap",
        "colorbox": "lib/jquery.colorbox-min",
        "chosen": "lib/chosen.jquery.min",
        "liveValidation": "lib/jquery.validationEngine",
        "liveValidationEn": "lib/jquery.validationEngine-en",
        "popcorn": "lib/popcorn-complete",
        "formset":'lib/jquery.formset',
        "datepicker":'lib/bootstrap-datepicker',
    },
    shim: {
        _: {
            exports: "_"
        },
        bootstrap: {
            deps: ['jquery']
        },
        datepicker: {
            deps: ['jquery', 'bootstrap']
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
        urlArgs: "bust=" +  (new Date()).getTime(),
})
