.. dallasparser documentation master file, created by
	 sphinx-quickstart on Mon Jan 27 10:27:22 2020.
	 You can adapt this file completely to your liking, but it should at least
	 contain the root `toctree` directive.

Overview
========

This is a Python package for parsing HTML pages retrieved from the Texas Dallas
County Felony and Misdemeanor Courts Case Information. Since
the county website strictly monitors server activity, this package is meant to be used
only after the user has collected HTML files for their use. Put differently, I will
not be sharing any code that can be used to collect these raw HTML files.

Output
------
The `dallasparser` package will generate a maximum of 15 `.xlsx` files for each data
table found from the county website:

+---------------------------+---------------------------------+
| Table Name                | Output                          |
+===========================+=================================+
| Appeals                   | `appeals.xlsx`                  |
+---------------------------+---------------------------------+
| Bonds                     | `bonds.xlsx`                    |
+---------------------------+---------------------------------+
| Bond COMMENTS             | `bond_comments.xlsx`            |
+---------------------------+---------------------------------+
| Charges                   | `charges.xlsx`                  |
+---------------------------+---------------------------------+
| Competency Data           | `competency_data.xlsx`          |
+---------------------------+---------------------------------+
| Dispositions              | `dispositions.xlsx`             |
+---------------------------+---------------------------------+
| General Comments          | `general_comments.xlsx`         |
+---------------------------+---------------------------------+
| General Comments WS Date  | `general_comments_ws_date.xlsx` |
+---------------------------+---------------------------------+
| Judicial Information      | `judicial_information.xlsx`     |
+---------------------------+---------------------------------+
| Motions                   | `motions.xlsx`                  |
+---------------------------+---------------------------------+
| Names                     | `names.xlsx`                    |
+---------------------------+---------------------------------+
| Payments                  | `payments.xlsx`                 |
+---------------------------+---------------------------------+
| Probation Revocation      | `probation_revocation.xlsx`     |
+---------------------------+---------------------------------+
| Reduced/Enhanced Charges  | `reduced_enhanced_charges.xlsx` |
+---------------------------+---------------------------------+
| Sets and Passes           | `sets_and_passes.xlsx`          |
+---------------------------+---------------------------------+

Installation
------------
**Source**::

	$ git clone https://github.com/jaycatsby/tx_dallas_court_parser.git
	$ cd tx_dallas_court_parser
	$ python setup.py install

**PyPI**::

	$ pip install dallasparser

Usage
-----
**A. CLI**::

	$ dallasparser [-h] [-i INPUT] [-o OUTPUT]

	optional arguments:
		-h, --help            show this help message and exit
		-i INPUT, --input INPUT
													absolute path of HTML folder
		-o OUTPUT, --output OUTPUT
													absolute path of XLSX output files

**B. Module**::

	from dallasparser.parser import TXDallasParser
	parser = TXDallasParser(html_path, xlsx_path)
	parser.run()


Scripts
=======
.. toctree::
	:maxdepth: 3

	cli
	parser
	regex
	utils


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
