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
    P_H_given_E = (P_E_given_H * P_H) / P_E  # Posterior Probability
```

#### The second step is Fuzzy Logic:
<img src="fuzzyGit.jpg" alt="alt text" width="300">

```python
    muLow = 1 - P_H_given_E  # Low Threat
    muHigh = P_H_given_E  # High Threat

    print("\nStep Two:\nLow Threat (μLow):", muLow)
    print("High Threat (μHigh):", muHigh)
```

#### The third step is Activation: 
<img src="actgit.jpg" alt="alt text" width="300">

```python
    if 3600 <= time_in_seconds < 5400:
        f_t = 2
    elif time_in_seconds >= 5400:
        f_t = 1
    else:
        f_t = 0

    print("\nStep Three:\nTime (t):", time_in_seconds, "seconds")
    print("Threshold Function f(t):", f_t)

    if f_t == 2:
        print("Glutamate is strongly activated.")
        if time_in_seconds < 3600:
            print("Program stops as t < 3600.")
            return
    elif f_t == 1:
        print("Moderate activation: Extra Synaptic GABA is activated.")
        if time_in_seconds < 3600:
            print("Program stops as t < 3600.")
            return
    else:
        print("No significant activation.")
        if time_in_seconds < 3600:
            print("Program stops as t < 3600.")
            return
```
#### The fourth step is Bayes Inference again: 
