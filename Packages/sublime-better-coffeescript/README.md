

# Jump to Section

* [Latest Change Log](https://github.com/aponxi/sublime-better-coffeescript/blob/master/changelogs/0.6.md)
* [Installation](#installation)
* [Updating](#updating)
* [Commands/Shortcuts](#commandsshortcuts)
* [Snippets](#snippets)
* [Building](#building)
* [Settings](#settings)
* [Special Thanks](#special-thanks)

# Overview

## Description

CoffeeScript plugin was originally created by Xavura. As I began writing a lot of code in CoffeeScript I felt the need for side-by-side view for compiled CoffeeScript. Since Xavura's repo haven't been updated for over a year, and my sent pull requests were unresponsive I decided to branch out my own version. The biggest change in my branch is the Watch Mode which updates the compiled JavaScript view whenever you modify the CoffeeScript thus enabling you to view your progress side-by-side.

I use this plugin everyday so whenever I am not developing I am in testing stage. I'll make sure every request or bug will be patched since I'm a frequent user.

## Contributing

- Please use [aponxi/issues page](https://github.com/aponxi/sublime-better-coffeescript/issues) to make requests or report bugs.
- It would be best to keep the wiki on [this repository's wiki](https://github.com/aponxi/sublime-better-coffeescript/wiki) as well.

# Installation

## via Package Control

> This is the recommended installation method.

If you have Sublime Package Control, you know what to do. If not, well: it's a package manager for Sublime Text 2; it's awesome and you can [read about it here](http://wbond.net/sublime_packages/package_control).

To install Package Control, open the Python Console (`ctrl+'` or ``cmd+` ``) and paste the following into it:

    import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'

After installing the package and restarting the editor:

* Open the Command Pallete (`ctrl+shift+P` or `cmd+shift+P`).
* Type "Install Package" and hit return.
* Type "sublime-better-coffeescript" and hit return.

## via Source Control

> If you plan to contribute, then you should install via this method. Otherwise it is recommended that you install the package via Package Control, see above.

Sublime stores packages in the following locations:

	Nix: ~/.config/sublime-text-2/packages
	Mac: ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
	Win: %APPDATA%\Sublime Text 2\Packages

### As a repository within the packages directory

Open a Terminal/Console and run the following commands, replacing `PACKAGE_PATH` with the path corresponding to your OS above.

	cd PACKAGE_PATH
	git clone https://github.com/aponxi/sublime-better-coffeescript.git "sublime-better-coffeescript"

### As a repository outside of the packages directory

If you use Github for Mac/Windows which store repositories in a specific location, or if you just don't want a repository in your packages directory, then instead you can use a link.

If you don't yet have the repository, then grab it via your GUI program or via the command line:

	cd WHEREVER_YOU_WANT
	git clone https://github.com/aponxi/sublime-better-coffeescript.git

Once that is done, we will create the link:

#### Windows:

	cd PACKAGE_PATH
	mklink /D sublime-better-coffeescript ABSOLUTE_PATH_TO_REPOSITORY

#### Nix/Mac:

	cd PACKAGE_PATH
	ln -s ABSOLUTE_PATH_TO_REPOSITORY sublime-better-coffeescript

#### A note on Package Control

When Package Control tries to update your packages, if you have a repository in your packages directory then it will try to pull down and merge any changes. If you don't want this to happen and would rather handle everything yourself, then you can add the following to your settings (Preferences » Package Settings » Package Control » Settings - User):

	"auto_upgrade_ignore": ["sublime-better-coffeescript"]

# Updating

If you are using Package Control, updating will be automatic and you don't have to worry about it.

If using Source Control:

	cd PACKAGE_PATH/CoffeeScript
	git fetch origin
	git merge origin/master

# Commands/Shortcuts

You can access the commands either using the command palette (`ctrl+shift+P` or `cmd+shift+P`) or via shortcuts.

	alt+shift+t - Run a Cake task
	alt+shift+r - Run some CoffeeScript (puts/print is available for output)
	alt+shift+s - Run a syntax check
	alt+shift+c - Compile a file
	alt+shift+d - Display compiled JavaScript
	alt+shift+l - Display lexer tokens
	alt+shift+n - Display parser nodes
	alt+shift+w - Toggle watch mode
	alt+shift+p - Toggle output panel


Context menu has `Compile Output` that compiles the current CoffeeScript and outputs the javascript code that is run, in a panel.

**Note:** Some of the commands use the Status Bar for output, so you'll probably want to enable it (Tools » Show Status Bar).



# Snippets

- Use `TAB` to run a snippet after typing the trigger.
- Use `TAB` and `shift+TAB` to cycle forward/backward through fields.
- Use `ESC` to exit snippet mode.

### Snippet Triggers

**Comprehension**

	Array:  forin
	Object: forof
	Range:  fori (inclusive)
	Range:  forx (exclusive)

**Statements**

	If:        if
	Else:      el
	If Else:   ifel
	Else If:   elif
	Switch:    swi
	Ternary:   ter
	Try Catch: try
	Unless:    unl

**Classes**

	Class - cla

**Other**

	Function:      -
	Function:      = (bound)
	Interpolation: #

# Building

> When using the build system, it is assumed that your `.sublime-project` file lives in your project's base directory (due to limitations with the build system).

Hitting `F7` (Tools » Build) will run the Cake task 'sbuild'.

If you're not quite sure what the point of this is then read on.

Let's say before distributing your project that you would like to combine all of your `.js` files into one and then minify them them using UglifyJS or something.

That's what this is for! You would create a `Cakefile` and inside it you would write a task:

	task 'sbuild', 'Prepare project for distribution.', ->
		# ...

# Settings

Go to `Preferences > Package Settings > CoffeeScript > Settings - User` to change settings.

```Javascript
{
	/*
		The directory containing your coffee binary. Usually
		/usr/local/bin.
	*/
	"binDir": "/usr/local/bin"

	/*
		Compile without the top-level function wrapper (coffee -b).
	*/

,	"noWrapper": true

	/*
		Enable or disable refresh the compiled Output on Save.
		Only available for watch mode.
	*/
,	"watchOnSave": true
	/*
		Enable refreshing compiled JS when CoffeeScript is modified.

		Put false to disable
		Put a number of seconds to delay the refresh
	*/
,	"watchOnModified": 0.5
	/*
		Enable Compiling on save. It will compile into the same folder.
	*/
,	"compileOnSave": true
	/*
		Enable outputting the results of the compiled coffeescript in a panel
	*/
,	"showOutputOnSave": false



}
```

# Special Thanks

* [agibsonsw](https://github.com/agibsonsw) for his help in writing WatchMode
* [Xavura](https://github.com/Xavura) for writing the base of this plugin
