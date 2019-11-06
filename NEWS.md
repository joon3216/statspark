
# `statspark`

## Coming up: ver 0.0.5

* Add tests for functions
* Define `Model` object to incorporate the training set and the formula. This will get rid of `train` argument in the following functions:
    + `produce_roc_table(mod, train)`
    + `count_cases(mod, data, train, ...)`
    + `model_by_lrt(mod, train, ...)`
    + `model_by_vif(mod, train, ...)`
    + `terbin_model(mod, train)`
* Generalize functions to work with `sm.GLM` of any family and features of any df, as well as `sm.OLS`:
    + `anova`
    + `drop1`
    + `model_by_lrt`
    + `plot_rl`

## ver 0.0.4 (PyPI)

* Added the following constant:
    + `statspark.qgf.sql_type`: `sql_type` that you are working on. Currently, only 'bigquery' and 'postgres' are supported.
* Added the following functions:
    + `count_distinct`: return an SQL query that counts the number of distinct values in each selected columns of a table
    + `is_unique`: return an SQL query that verifies whether all values at each record in a column, or a combination of columns, are unique within the column/combination.
    + `random_word`: generate a random sequence of characters
    + `request_each`: return an SQL query that performs a computation request at each (specified) column
    + `transpose`: return an SQL query that transposes a 1-by-k table

## ver 0.0.3

* Added the following function:
    + `fusion_estimates`: see [here](https://joon3216.github.io/research_materials/2018/non_separable_penalty) for details
* Edited the return value of `count_null`:
    + semicolon at the end is removed.
* Edited the return value of `gauss_seidel`:
    + `y` deleted, `lambd` added, `niters` changed its name to `iteration`


## ver 0.0.2

* Added the following functions:
    + `count_null`: return an SQL query that counts the number of NULLs in each selected columns of a table
    + `csum_N_pois`: return a DFT-based pmf
    + `dpmf`: generate a (finite-support) pmf
    + `impute_em`: impute missing values by the EM algorithm assuming normality of observations
    + `npmap(...)`: `np.array(list(map(...)))`
    + `plot_lm`: draw linear regression plots
    + `plot_qq`: draw a Normal Q-Q plot
    + `plot_rf`: draw a Residuals vs. Fitted plot
    + `plot_rlev`: draw a Residuals vs. Leverage plot
    + `plot_sl`: draw a Scale-Location plot
    + `rpmf`: sample from a desired (finite-support) pmf
    + `simulate_nan(X, nan_rate)` (not made available): randomly replace some values of X with `np.nan`


## ver 0.0.1

* Created a repository
* Uploaded to PyPI
* Wrote a README.md and setup.py
* Wrote functions in statspark/r_inspired.py
