This repo contains a simple, example workflow that can generate fake data and fit a (linear) logistic regression to it.

---

The required software can be installed via

```
pip install . --prefix ./opt/ # install the software
source ./env.sh               # set up the environment to point to the software
```

and the workflow can be run via

```
./make-fake-data && ./infer && ./corner
```

---

Specifically, our model for the probability of success is

```math
p(\vec{f}) = \left(1 + \exp\left(\sum_i c_i f_i\right) \right)^{-1}
```

where `f_i` are the features (observed properties of each patient) and `c_i` are coefficients describing how important each feature is in determining the probability of improvement.
Whether any individual patient improves is then randomly assigned based on the probability computed with their features and the true coefficients.

  * `make-fake-data` sets up a simple data-set according to this model
    - it writes the features of patients, whether they improved to `data.csv.gz`
    - it also writes the true coefficients to `coeffs.csv.gz`
  * `infer` sets up this model (including the prior for the coefficients) and then samples from the posterior
    - it writes the posterior samples to `samples.hdf`
  * `corner` makes a plot of the posterior distribution (over coeffients) and labels it with the true coeffients
    - it writes `corner.png`
