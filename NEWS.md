
# `statspark`

## Coming up: ver 0.0.2

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

## ver 0.0.1 (GitHub)

* Added the following functions:
    + `count_null`: return an SQL query that counts the number of NULLs in selected columns in a table
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


## ver 0.0.1 (PyPI)

* Created a repository
* Uploaded to PyPI
* Wrote a README.md and setup.py
* Wrote functions in statspark/r_inspired.py
