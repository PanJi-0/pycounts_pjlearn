# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_pjlearn")

# populate package namespace
from pycounts_pjlearn.pycounts_pjlearn import count_words
from pycounts_pjlearn.plotting import plot_words