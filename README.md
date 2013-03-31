# conjoiners - multi-platform / multi-language reactive programming library

conjoiners is a library aiming to enable reactive programming for
existing (or new) systems written in different languages and running
on different platforms. conjoiners is minimally invasive in its
programming model, but complex behind the scenes.

Idea and first implementations are done by me, Pavlo Baron (pavlobaron).

## Why reactive programming?

[Reactive programming](http://en.wikipedia.org/wiki/Reactive_programming)
is very powerful. It reduces programming complexity of systems with
complex data flows and many different inhomogenous parts of the whole
system needing cooperation and orchestration. The very main advantage
of reactive programming is implicit manifestation of new data and data
changes in every part of the system dealing with this data. You don't
ask for new values of data, these values are already there where you
need them. When you design your system the way this data is just used
in calculations without being cached anywhere in your programs, every
time the computation based on this data is done, the newest values
will automatically be visible to this computation.

Reactive programming has many possible use cases - from typical
business applications to high-load, high-performance systems with
gazillions of events flying in on every end. You can build on it for
near-realtime data analysis, statistics, generally event
processing. And all this completely abstracting away unnecessary
communication and data exchange details.

## Why conjoiners?

conjoiners is a relatively small library in every language. It doesn't
provide any programming modell except one single call to it to implant
some code into new or existing objects (or how ever you call them in
your programming language). From here, conjoiners will take care of
automatic manifestation of newest values of data your program is
interested it.

The main advantage is that conjoiners allow to link together
technologies typically using some sort of middleware, interfaces,
sockets and whatnot to cooperate and to exchange data. But it's not
being done through explicit API calls, but completely behind the
scenes. At the time point X there is a value of Y that equals to
Z. All conjoiners will get this value as fast as the selected
connection way allows them to exchange the data. In your program, you
just pick the current value and work with it.

I've started working on conjoiners being heavily impressed by some
talks I've attended at the TechMesh conference in London back in 2012
as well by chats around these talks. And also by the
[Elm programming language](http://elm-lang.org). I don't want to
reduce conjoiners to the functional reactive programming only
though. Whatever language, whatever platform can run programs using
the corresponding conjoiners library and exchange data
transparently. And when I say "any technology", I don't only mean
typical business programs, but also databases and similar
systems. Because how cool would it be to just get informed in a Python
script about data changes done through a piece of Java code in a
database? And this completely without asking for it, just having the
values one is interested in. I think it's cool.

## Why this name?

conjoiners and all corresponding terms I use are directly derived from
[Reynolds' Revelation Space](http://en.wikipedia.org/wiki/Factions_in_Revelation_Space). Conjoiners
are are using mental communication sending so called
transenlightenments to each other. In order to do so, they get an
implant, and from here this will "talk" to other conjoiners without
being explicitly used or triggered by the carrier person.

The original conjoiner - Galiana - is responsible for creating first
conjoiners through experiments. I would recommend reading the books
and stories if you want to dig deeper into this naming - or just stay
with this brief overview.

## How does it work?

You import (or however you call it in your language) the small
conjoiners library where you need it. Then, you implant it into one or
several objects (or however you call them). After this, they will
automatically talk to other conjoiners found in the configuration
file, exchange new values etc.

conjoiners is non-invasive in terms of its programming model, but sure
brings some new dependencies. Right now, the only transport is
[ZeroMQ](http://www.zeromq.org). 0MQ is fantastic as glue between
technologies, building on top of further lower level protocols
itself. But you don't see anything from 0MQ in your code. You only
need to have it installed and accessable / bound in your
application. The rest will be done by the conjoiners library.

But how about an example? Here is some conjoiner'ized code written in Python:

    class Test(object):
        pass

    cj1 = Test()
    cj2 = Test()
    conjoiners.implant(cj1, "./test_conf.json", "test")
    self.cj1.test_value = "test_value"

and here is another conjoiner implemented in JavaScript on node.js:

    function Test() {
    };

    var cj2 = new Test();
    conjoiners.implant(cj2, "../test/test_conf.json", "test2");
    console.log(cj2.test_value);

The Python part will set a value in a conjoiner. Its implant will send
a transenlightenment over to the Node.js piece. And when this value is
accessed there, after some time it will be what the Python conjoiner
has set. Do you see any communication, API calls or such?

Conjoiners share one nest configuration, which describes the group of
conjoiners that know each other as well as communictaion protocol details.

## Current state of work

I've been working on the idea for several months. Right now, by the
time of this first appearancd on GitHub, I come up with two supported
platforms:

*    [conjoiners-python](https://github.com/conjoiners/conjoiners-python)
*    [conjoiners-node.js](https://github.com/conjoiners/conjoiners-node.js)

I picked these two primarilly for two reasons: it's both very popular
platforms with lots of existing libraries and running solutions. And
the language are dynamic, allowing me to use monkey patching in order
to hide conjoiners behind a simple implant-call.

I am already working on conjoiners for Java, which probably will work
through runtime bytecode manipulation instead of using observers and
similar invasive mechanisms. And I'm trying to wrap my mind around how
to implement conjoiners in Erlang. Of course, conjoiners shouldn't
stop there, but these are at lease my own first choices.

## Missing parts

Of course, so much is still missing. Tests, some real world usage and
experience, examples, especially how to use conjoiners in inhonogenous
environments.

But there is much more: I'm thinking of implementing Galiana as Puppet
module / Chef cookbook. This way, it would be possible to describe the
nest confiruation abstractly and to implant communication details when
deploying to an environment.

Also, further transports as well as abstraction of transport at all is
something to be implemented next. RabbitMQ could be used. But also
RESTful interfaces, Websockets and so on. This way, conjoiners can go
to the browser or the mobile app.

Security is something that I didn't yet consider at all, but of course
I'm thinking about it. I think, it would be more interesting in first
place to test and optimize performance, stability and reliability.

## Contribution

To clarify this: I would love to make conjoiners a community project
to bring reactive programming anywhere you want it to be, to make it
work. That's why I've created a separate GitHub organisation and am
welcoming anybody who would like to contribute with advices and
implementations, fixes etc. Just contact me about that.
