# Elections website

### Build:

Building the project requires following packages to be installed and available from python 
interpreter:
- xlrd, xlwt
- numpy
- django

Once I find time to figure out how to conveniently share pip envs I'll include this info as 
a piece of some code.

To build the website do the following:
- `sh ./initData.sh` to (fetch official data files from original website)
- `python src/parseData.py` (parse these files into one usable by the main script)
- (optional) set `src/config.py` according to your needs

and finally:

- `python src/generate.py` (create all webpages)


