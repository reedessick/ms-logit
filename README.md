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
prob = (1 + \exp(\sum(features*coefficients)))^{-1}
```
