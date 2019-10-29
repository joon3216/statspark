
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


# ver 0.0.1 (current version)

* Created a repository
* Uploaded to PyPI
* Wrote a README.md and setup.py
* Wrote functions in statspark/r_inspired.py