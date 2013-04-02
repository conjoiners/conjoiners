var conjoiners = require('conjoiners');

function Test() {
};

var c = new Test();
c.count = 0;

var doit = function(o) {
    console.log("current count: " + c.count++);
    setTimeout(doit, 1);
}

conjoiners.implant(c,
                   '/Users/pb/code/conjoiners/conjoiners/examples/hits_simple/conf.json',
                   'server',
                   doit);
