# Databricks notebook source
import sys
from pprint import pprint

pprint(sys.path)

# COMMAND ----------

import discover_modules
discover_modules.go(spark)

# COMMAND ----------

from utilities import add
add(2, 2)

# COMMAND ----------

# You can now import Python modules from the supplemental_files repo.
from mytest import Test, run_tests
import unittest

run_tests()

