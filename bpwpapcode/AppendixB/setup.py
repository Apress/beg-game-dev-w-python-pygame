from distutils.core import setup
import py2exe

setup(
    #version = "1.0",
    #description = "Ant State machine from Chapter7",
    #name = "antsstatemachine",
    windows = [{"script":"antsstatemachine.py"}],
    data_files = [ (".", ["ant.png", "leaf.png", "spider.png"]) ]
    )
