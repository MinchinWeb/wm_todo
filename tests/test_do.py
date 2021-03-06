# TODO.TXT-CLI-python test script
# Copyright (C) 2011-2012  Sigmavirus24, Jeff Stein
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# TLDR: This is licensed under the GPLv3. See LICENSE for more details.

import random
import unittest

import base
import todo

class DoTest(base.BaseTest):

    def test_do(self):
        todo.cli.addm_todo("\n".join(self._test_lines_no_pri(self.num)))
        ran = random.Random()

        for i in range(self.num, 0, -1):
            j = ran.randint(1, i)
            todo.cli.do_todo(str(j))
            #todo.do_todo(str(i))

        self.assertNumLines(0)

if __name__ == "__main__":
    unittest.main()
