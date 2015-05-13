# This file is part of pointio.

# pointio is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pointio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pointio.  If not, see <http://www.gnu.org/licenses/>.

# Copyright 2015 Ravi Peters

import os
try:
	import pcl
except ImportError:
	print "Cannot read pcd files without pcl module"
	raise

def write_pcd(dir, datadict, keys=[], binary=True):
	if not os.path.exists(dir):
	    os.makedirs(dir)

	for key,val in datadict.items():
		if key in keys or len(keys)==0:
			fname = os.path.join(dir,key)
			pcl.save( fname, pcl.PointCloud(val), binary=binary )

def read_pcd(dir, keys=[]):
	assert os.path.exists(dir)

	if len(keys)==0:
		keys = inspect_npy(dir)

	datadict = {}	
	for key in keys:
		fname = os.path.join(dir,key+'.pcd')
		if os.path.exists(fname):
			datadict[key] = pcl.load(fname).as_array()
	return datadict

def inspect_pcd(dir):
	from glob import glob
	dir = os.path.join(dir,'*.pcd')
	return [os.path.split(f)[-1][:-4] for f in glob(dir)]