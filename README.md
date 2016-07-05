# pointio
convenience wrapper for managing point clouds as .npy files

## Installation
Installation should be as simple as

```
$ git clone https://github.com/Ylannl/pointio.git
$ cd pointio
$ python setup.py install
```
or simply
```
$ pip install git+https://github.com/Ylannl/pointio.git
```
This should automatically install all required dependencies.

On windows you may need to manually install `python-igraph` first. Download from http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph and use pip to install, eg. `pip install .\python_igraph-0.7.1.post6-cp35-none-win_amd64.whl`.

## Usage
```
las2npy.py <myLASfile> <myNPYdir>
```
