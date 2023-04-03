# Difference Report
Taking two input datasets with identical shape and common unique identifier, produces a difference
report of the two datasets. The report provides the rows and columns of interest, indexed by the 
identifier, showing the distance of the 'origin' dataset values to the 'other' dataset values.

The following environment variables are specific to this Difference Report
* HADRON_PROFILING_ORIGIN - The full URI of the 'origin' dataset.
* HADRON_PROFILING_OTHER - The full URI of the 'other' dataset.
* HADRON_ALIGN_ORIGIN - the full URI of the mapping file the 'origin' column names alignment
* HADRON_ALIGN_OTHER - the full URI of the mapping file the 'origin' column names alignment
* HADRON_DIFF_ON - The unique identifier column name the two input data sources are joined by

## Running the Ensemble
To run the component ensemble we run the controller that orchestrates all the other components 
in the ensemble.

### Hadron Controller
Set environment variables.
```
os.environ["HADRON_DEFAULT_PATH"] = ""
os.environ["HADRON_PROFILING_ORIGIN" = ""
os.environ["HADRON_PROFILING_OTHER" = ""
os.environ["HADRON_ALIGN_ORIGIN" = ""
os.environ["HADRON_ALIGN_OTHER" = ""
os.environ["HADRON_DIFF_ON" = ""
```
Create an instance of the Controller where the `uri_pm_repo` parameter points to the 
path of the ensemble Domain Contracts for the Difference Report.
```
from ds_discovery import Controller
controller = Controller.from_env(uri_pm_repo="")
controller.run_controller()
```

## Dictionary

### Hadron Controller
**uri_pm_repo** is a mandatory key and point to the Domain Contract path for this run.

### Environment Variables
* HADRON_DEFAULT_PATH - A single default path where all data will be sourced from and persisted too.
* HADRON_PROFILING_ORIGIN - The full URI of the 'origin' dataset.
* HADRON_PROFILING_OTHER - The full URI of the 'other' dataset.
* HADRON_ALIGN_ORIGIN - the full URI of the mapping file the 'origin' column names alignment
* HADRON_ALIGN_OTHER - the full URI of the mapping file the 'origin' column names alignment
* HADRON_DIFF_ON - The unique identifier column name the two input data sources are joined by

optional module and handler if the URI has no automatic assignment:
* data profiling 'origin' source module and handler
  * HADRON_WRANGLE_PROFILING_ORIGIN_SOURCE_MODULE
  * HADRON_WRANGLE_PROFILING_ORIGIN_SOURCE_HANDLER
* data profiling 'other' source module and handler
  * HADRON_WRANGLE_PROFILING_OTHER_SOURCE_MODULE
  * HADRON_WRANGLE_PROFILING_OTHER_SOURCE_HANDLER
* Difference report persist module and handler
  * HADRON_WRANGLE_DIFFERENCE_PERSIST_MODULE
  * HADRON_WRANGLE_DIFFERENCE_PERSIST_HANDLER

