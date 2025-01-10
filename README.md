# Consciousness
## Mathematical Framework for Modeling Consciousness

This code uses my Mathematical Framework for Modeling Consciousness and puts it into code. 
You can find my Mathematical Framework for Modeling Consciousness [here](https://heartfelt-fairy-92af03.netlify.app/research)

### Steps

#### The first step is Bayes Inference:
![Bayes' Theorem](https://latex.codecogs.com/png.latex?P(H|E)%20=%20\frac{P(E|H)%20\cdot%20P(H)}{P(E)})

```python
 P_H = 0.78  # Prior Probability (Environment is dangerous)
    P_E_given_H = 0.81  # Likelihood that threat is real based on external stimuli
    P_E_given_not_H = 0.79  # Likelihood that threat is not real

    P_E = P_E_given_H * P_H + P_E_given_not_H * (1 - P_H)  # Marginal Probability
    P_H_given_E = (P_E_given_H * P_H) / P_E  # Posterior Probability```

#### The second step is Fuzzy Logic:
<img src="fuzzyGit.jpg" alt="alt text" width="300">

#### The third step is Activation: 
<img src="actgit.jpg" alt="alt text" width="300">

