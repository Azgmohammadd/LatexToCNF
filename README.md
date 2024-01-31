<div align="center">
<pre>
██╗      █████╗ ████████╗███████╗██╗  ██╗████████╗ ██████╗  ██████╗███╗   ██╗███████╗
██║     ██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝██╔═══██╗██╔════╝████╗  ██║██╔════╝
██║     ███████║   ██║   █████╗   ╚███╔╝    ██║   ██║   ██║██║     ██╔██╗ ██║█████╗  
██║     ██╔══██║   ██║   ██╔══╝   ██╔██╗    ██║   ██║   ██║██║     ██║╚██╗██║██╔══╝  
███████╗██║  ██║   ██║   ███████╗██╔╝ ██╗   ██║   ╚██████╔╝╚██████╗██║ ╚████║██║     
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═══╝╚═╝     
                                                                                                           
-------------------------------------------------------------------------------------
python cli to convert latex input to CNF(Conjuctive Normal Form).
</pre>

[![PyPI](https://img.shields.io/pypi/v/LatexToCNF.svg)](https://pypi.org/project/LatexToCNF/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

## Installation

pip install this repo.
(Note: Incompatible with Python 2.x)

```sh
pip3 install LatexToCNF
```

## Usage example

### To get help with commandline arguments

```sh
LatexToCNF --help
```

### Using Command-line Arguments

```sh
LatexToCNF -f "/path/to/folder/myinput.tex"
(or)
LatexToCNF -f "/path/to/folder/myinput.txt"
```

(or)

```sh
LatexToCNf --filepath "/path/to/folder/myinput.tex"
(or)
LatexToCNF --filepath "/path/to/folder/myinput.txt"
```

## Sample input file
### myinput.tex
```tex
\neg \neg p
\neg p \wedge q \rightarrow p \wedge (r \rightarrow q)
r \rightarrow (s \rightarrow (t \wedge s \rightarrow r))
```

### myinput.text
```txt
\neg \neg p
\neg p \wedge q \rightarrow p \wedge (r \rightarrow q)
r \rightarrow (s \rightarrow (t \wedge s \rightarrow r))
```

### output
```sh
line-1: p
line-2: [['p', '\\vee', ['\\neg', 'q']], '\\vee', ['p', '\\wedge', [['\\neg', 'r'], '\\vee', 'q']]]
line-3: [['\\neg', 'r'], '\\vee', [['\\neg', 's'], '\\vee', [[['\\neg', 't'], '\\vee', ['\\neg', 's']], '\\vee', 'r']]]
```

## Meta

Azgmohammadd – azgmohammadd@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/azgmohammadd](https://github.com/azgmohammadd/)

## Contributing

1. Fork it (<https://github.com/azgmohammadd/azgmohammadd/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Createing this README.md is based on 
https://github.com/zahash/quaeso/blob/main/README.md

so thanks zahash for your great repo.
 -->
