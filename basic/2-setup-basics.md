# Installing Python

You can use a website like [repl.it](https://repl.it/languages/python3), but I highly recommend installing Python. It doesn't matter which operating system you use because Python runs
great on Windows, Mac OSX, Linux and many other operating systems.

Let's get started!

## Downloading and installing Python

### Windows

Installing Python on Windows is a lot like installing any other program.

Go to [the official Python website](https://www.python.org/).

### Mac OSX

At the time of writing this, Macs don't come with a Python 3 and you
need to install it yourself. [Homebrew](https://brew.sh/index_de.html) is the easiest way to do that.

```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
```

Set Python3 as OSX default.

Edit `~/.bash_profile`:

```bash
alias python='python3'
alias pip='pip3'
```

Reload shell:

```bash
source ~/.bash_profile
```

### Linux

You already have Python 3, **there's no need to install anything**.

## Running Python

```bash
python -V
pip -V
```

## Shell script execution

```bash
#!/usr/bin/env python3
```
