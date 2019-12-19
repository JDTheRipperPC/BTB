# -*- coding: utf-8 -*-

"""Top level where all the challenges are imported."""

from btb.benchmark.challenges.bohachevsky import Bohachevsky
from btb.benchmark.challenges.branin import Branin
from btb.benchmark.challenges.census import CensusRFC, CensusSGDC
from btb.benchmark.challenges.rosenbrock import Rosenbrock

__all__ = ('Bohachevsky', 'Branin', 'CensusRFC', 'CensusSGDC', 'Rosenbrock', )