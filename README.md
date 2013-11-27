# Flask, Foundation and requirejs

This is a template to start your own project using Flask, foundation and requirejs. 

## Requirements

You'll need to have the following items installed before continuing.

  * [Node.js](http://nodejs.org): Use the installer provided on the NodeJS website.
  * [Grunt](http://gruntjs.com/): Run `[sudo] npm install -g grunt-cli`
  * [Bower](http://bower.io): Run `[sudo] npm install -g bower`
  * [Python](http://www.python.org/)

## Quickstart

```bash
git clone git@github.com:wcdolphin/foundation-requirejs.git
npm install && bower install && pip install -r requirements.txt
```

While you're working on your project, run:

`grunt`

And you're set!

Before deploying, be sure to include a production ready web server, such as Twisted in your requirements.txt.


## Directory Strucutre

  * `scss/_settings.scss`: Foundation configuration settings go in here
  * `scss/app.scss`: Application styles go here
