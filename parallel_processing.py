# source https://campus.datacamp.com/courses/introduction-to-data-engineering/data-engineering-toolbox?ex=8

import pandas as pd
from multiprocessing import Pool

# Function to apply a function over multiple cores
@print_timing 
def parallel_apply(apply_func, groups, nb_cores):
  with Pool(nb_cores) as p:
    results = p.map(apply_func, groups) 
    return pd.concat(results)
  
  # Parallel apply using 4 cores
  # note, the function take_man_age() must be defined above. athlete_Events is a df with age and 
 parallel_apply(take_mean_age, athlete_Events.groupby('Year', 4) 
                
# In the previous exercise, you saw how to split up a task and use the low-level python multiprocessing.Pool API to do calculations on several processing units.
# It's essential to understand this on a lower level, but in reality, you'll never use this kind of APIs. A more convenient way to parallelize an apply over several groups is using the dask framework and its abstraction of the pandas DataFrame, for example.
# The pandas DataFrame, athlete_events, is available in your workspace.
import dask.dataframe as dd

# Set the number of partitions
athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4)
