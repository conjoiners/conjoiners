'use strict';

var conjoiners = require('conjoiners');

var c = {
  count: 0
};

conjoiners.implant(c, 'conf.json', 'server').then(function() {
    var doIt = function() {
        c.count += 1;
        console.log("current count: " + c.count);
        setTimeout(doIt, 1);
    };
    doIt();
}).done();