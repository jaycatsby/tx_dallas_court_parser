TX Dallas County Felony and Misdemeanor Courts Parser
=====================================================
![Dallas Screenshot](/images/sample_screenshot.png)

This is a Python package for parsing HTML pages retrieved from the [Texas Dallas
County Felony and Misdemeanor Courts Case Information](https://www.dallascounty.org/criminalBackgroundSearch/searchByCase). Since
the county website strictly monitors server activity, this package is meant to be used
only after the user has collected HTML files for their use. Put differently, I will
not be sharing any code that can be used to collect these raw HTML files.

Output
------
The `dallasparser` package will generate a maximum of 11 `.xlsx` files for each data
table found from the county website:

| Table Name                | Output                          |
|:--------------------------|:--------------------------------|
| Appeals                   | `appeals.xlsx`                  |
| Bonds                     | `bonds.xlsx`                    |
| Charges                   | `charges.xlsx`                  |
| Dispositions              | `dispositions.xlsx`             |
| General Comments          | `general_comments.xlsx`         |
| General Comments WS Date  | `general_comments_ws_date.xlsx` |
| Judicial Information      | `judicial_information.xlsx`     |
| Motions                   | `motions.xlsx`                  |
| Names                     | `names.xlsx`                    |
| Reduced/Enhanced Charges  | `reduced_enhanced_charges.xlsx` |
| Sets and Passes           | `sets_and_passes.xlsx`          |

Installation
------------
**Source**
```bash
$ git clone https://github.com/jaycatsby/tx_dallas_court_parser.git
$ cd tx_dallas_court_parser
$ python setup.py install
```

**PyPI**
```bash
$ pip install dallasparser
```

Usage
-----
**A. CLI**
```bash
$ dallasparser [-h] [-i INPUT] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        absolute path of HTML folder
  -o OUTPUT, --output OUTPUT
                        absolute path of XLSX output files
```

**B. Module**
```python
from dallasparser.parser import TXDallasParser
parser = TXDallasParser(html_path, xlsx_path)
parser.run()
```

Contributions
-------------
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:
>While creating a PR, please update the *Contributor(s)* section below as well.

Contributor(s)
--------------
[Jay C.](https://github.com/jaycatsby)
