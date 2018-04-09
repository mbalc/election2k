# Elections website

### Build:

To build the website do the following:
- `sh ./initData.sh` to (fetch official data files from original website)
- `python src/parseData.py` (parse these files into one usable by the main script)
- (optional) set `src/config.py` according to your needs

and finally:

- `python src/generate.py` (create all webpages)


