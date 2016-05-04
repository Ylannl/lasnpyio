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

from setuptools import setup, find_packages

setup(
    name = "pointio",
    version = "0.1",
    packages = find_packages(),
    install_requires = ["numpy>=1.9.1", "laspy"],
    scripts = ['util/las2npy.py', 'util/npy2las.py', 'util/npy2pcd.py', 'util/pcd2npy.py', 'util/ply2npy.py']
)
