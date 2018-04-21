# Elections website ![Shippable](https://img.shields.io/shippable/5444c5ecb904a4b21567b0ff.svg)

### Preview:

An active [build of the webpage is available here](https://mbalc.github.io/election2k/index.html)

### Build:

##### Requirements
Building the project requires python3 to be installed and on the path.
Also, following packages should installed and available from python
interpreter:
- xlrd, xlwt
- numpy
- django

If that's not the case, you can:
- `sh ./setupPy.sh` to create a venv on path `../gen` relatively to dir
frm which you run the script and install required packages there

...and next time you can just `source ../gen/bin/activate` to have
these installed packages available from `python` shell again

##### Building website
To build the website do the following:
- `sh ./initData.sh` to (fetch official data files from original website)
- `python src/parse_data.py` (parse these files into one usable by the main script)
- (optional) set `src/config.py` according to your needs

and finally:

- `python src/generate.py` (create all webpages)


