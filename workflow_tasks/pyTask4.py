# Databricks notebook source
# dbutils.widgets.removeAll()
dbutils.widgets.text("waittimeout", "0", "WaitTimout(s)")
dbutils.widgets.text("notebook", "./pyTask2", "notebook")

# COMMAND ----------

import time
import json

try:
  seconds = int(dbutils.widgets.get("waittimeout"))
  notebook = dbutils.widgets.get("notebook")
  print(f"Sleeping for {seconds} seconds...")
  time.sleep(seconds)
except Exception as e:
  out = {
    "status" : "failed",
    "error" : str(e),
    "notebook" : notebook
  }
  dbutils.notebook.exit(json.dumps(out))

# COMMAND ----------


out = json.dumps({
  "status" : "succeeded",
  "notebook" : notebook})

dbutils.notebook.exit(out)

