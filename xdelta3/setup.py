# xdelta 3 - delta compression tools and library
# Copyright (C) 2004 and onward.  Joshua P. MacDonald
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#
from distutils.core import setup, Extension

xdelta3_ext = Extension('xdelta3',
                        ['xdelta3.c'],
                        define_macros = [('PYTHON_MODULE',1),
                                         ('XD3_POSIX',1),
                                         ('REGRESSION_TEST',1),
                                         ('XD3_DEBUG',1),
                                         ('EXTCOMP',1),
                                         ('VCDIFF_TOOLS',1),
                                         ('XD3_USE_LARGEFILE64',1)])

setup(name='xdelta3',
      version='pre',
      ext_modules=[xdelta3_ext])
