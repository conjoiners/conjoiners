var conjoiners = require('conjoiners');

function Test() {
};

var c = new Test();
conjoiners.implant(c,
                   '/Users/pb/code/conjoiners/conjoiners/examples/hits_simple/conf.json',
                   'server');

var doit = function() {
    if (c.count == undefined) {
        c.count = 0;
    } else {
        c.count++;
    }

    console.log("current count: " + c.count);
    setTimeout(doit, 1);
}

setTimeout(doit, 1500);
