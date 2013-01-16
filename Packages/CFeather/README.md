[CFeather][homepage] is a package to provide C support for [Sublime Text 2][st2].

I created it because I'm not keen on Sublime's stock C package for the following reasons:

* It's conflated with supporting C++ at the same time.
* Its scope taxonomy doesn't [KISS][kiss].

CFeather is targeted at [ISO C90 aka ANSI C89][lang]. For convenience, some non-standard constructs are recognised:

* `(i|u)(8|16|32|64)`, `f(32|64)`, `byte`, `bool` and anything with a `_t` suffix as type names.
* `//` as the start of a line comment.
* A subset of [Doxygen][doxy]-formatting in comments (You must opt in to this via your colour scheme. [See here][doxy-col]).

For CFeather to be picked up by Sublime, you must first add the aforementioned stock package ("C++") to the `ignored_packages` array in your settings file.

This package is available direct from its GitHub homepage, and also via [Sublime Package Control][spc]. If you wish to distribute it otherwise, please contact me first.

---

Here's a screenshot. Remember that CFeather isn't about specific colours, but rather which colours are picked from your active colour scheme. The colour scheme it's paired with below is one I created, [Sundried][sd].

![Screenshot](https://github.com/frou/Sundried/raw/master/screenshot.png)

[homepage]: https://github.com/frou/CFeather
[st2]: http://www.sublimetext.com/
[kiss]: http://en.wikipedia.org/wiki/KISS_principle
[lang]: http://en.wikipedia.org/wiki/C_(programming_language)#ANSI_C_and_ISO_C
[doxy]: http://www.stack.nl/~dimitri/doxygen/
[doxy-col]: https://github.com/frou/CFeather/issues/1#issuecomment-10380609
[spc]: http://wbond.net/sublime_packages/package_control
[sd]: https://github.com/frou/Sundried
