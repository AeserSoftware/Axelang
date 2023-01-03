Axelang Language
=======
Axelang(Axe) is a Python-like programming language. In this project by Aeser, we have fixed some aspects we belived lacking in python. Scroll to the bottom to find the core idea.

The project contains:

- Regular expression based lexer
- Top-down recursive descent parser
- AST-walking interpreter
- REPL of the code

Axe doesn't require any third-party libraries.

What the language looks like:



    func map(arr, fn):
        r = []
        for val in arr:
            r = r + [fn(val)]
        r

    func factorial(n):
        if n <= 1:
            1
        else:
            n * factorial(n - 1)

    print(map(1...10, factorial))


You can find more examples in ``tests`` directory.

#### To run: python3 -m axe file.abr

## Extra Commands In AxeCLI
```
$ axe create pip
$ axe install pip
$ axe start # creates ABR file
$ axe start -n # create your own abr file
```
## AxCOS
AxCOS is the new operation check for AxCLI and Axe. Check status and version info here. A XenoID can also be found here which you can claim at the website. 
```
$ cos ver # check versions
$ cos ver -cli # Cli Version
$ cos op # Operational Status
$ cos generate xeno # XenoID
```
## Why so mixed with python?
You may have noticed that a lot of this code and modules work with python and sometimes only with python and not Axe becuase of the core idea of the project:
> The core idea of Axe is for not to replace Python but to work alongside it as an extention to patch certain parts that don't live up to modern-day workflows. This might mean creating Axe and it might mean creating python packages.
## Whats Next
Axe is a project with no limits.
We want to, after the basic ecosystem is set, improve Axe so that .abr files can work with or include Python.
## Versions Roadmap
Done = *
This = `
Next = ^

1*,1.5*,2*,2.5*,3*, 3.5`, 4^
