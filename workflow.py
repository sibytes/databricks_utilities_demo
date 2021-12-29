# Databricks notebook source
import discover_modules
discover_modules.go(spark)

# COMMAND ----------

from utilities import (
  Notebook, 
  execute_notebooks
)

# build a list of notebooks to run
task_root = "./workflow_tasks/"
notebooks = [
  Notebook(f"{task_root}pyTask1", 3600, {"waittimeout": 15}, 0, True),
  Notebook(f"{task_root}pyTask2", 3600, {"waittimeout": 10}, 0, True),
  Notebook(f"{task_root}pyTask3", 3600, {"waittimeout": 8},  0, True),
  Notebook(f"{task_root}pyTask4", 3600, {"waittimeout": 6},  0, True),
  Notebook(f"{task_root}pyTask5", 3600, {"waittimeout": 4},  0, True),
  Notebook(f"{task_root}pyTask6", 3600, {"waittimeout": 0},  0, True)
]

# execute the notebooks in parallel
results = execute_notebooks(notebooks, 4, dbutils)

# show the notebook returns
from pprint import pprint
pprint(results)

