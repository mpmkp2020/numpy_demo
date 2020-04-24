#!/usr/bin/env python3
def configuration(parent_package='', top_path=None):
    from numpy_demo.distutils.misc_util import Configuration
    config = Configuration('matrixlib', parent_package, top_path)
    config.add_data_dir('tests')
    return config

if __name__ == "__main__":
    from numpy_demo.distutils.core import setup
    config = configuration(top_path='').todict()
    setup(**config)