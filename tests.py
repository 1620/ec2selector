# Copyright (c) 2011, RED Interactive Agency
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

import unittest
from ec2selector import EC2Selector

class EC2SelectorTest (unittest.TestCase):
    
    def test_basic(self):
        '''Test select() returns anything at all by always picking option 0.'''
        s = EC2Selector(input_function=lambda(prompt): '0')
        assert s.select()

    def test_alestic_ubuntu(self):
        '''Test select() returns one alestic ubuntu-10 image on US East.'''
        s = EC2Selector()
        alestic_filters = {
            'name_contains': 'ubuntu-10', 
            'owner_id':'063491364108', # corresponds to 'alestic'
            'image_type': 'machine', 
            'virtualization_type':'paravirtual'
        }
        assert s.select(region_id='us-east-1', filters=dict(alestic_filters,
            **{'architecture': 'x86_64', }))
        assert s.select(region_id='us-east-1', filters=dict(alestic_filters,
            **{'architecture': 'i386', }))

if __name__ == '__main__':
    unittest.main()

# To run tests: python tests.py    