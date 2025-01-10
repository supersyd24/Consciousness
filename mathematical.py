def main():
    # Step One: Bayesian Inference One
    P_H = 0.78  # Prior Probability (Environment is dangerous)
    P_E_given_H = 0.81  # Likelihood that threat is real based on external stimuli
    P_E_given_not_H = 0.79  # Likelihood that threat is not real

    P_E = P_E_given_H * P_H + P_E_given_not_H * (1 - P_H)  # Marginal Probability
    P_H_given_E = (P_E_given_H * P_H) / P_E  # Posterior Probability

    print("Step One:\nPrior Probability (P(H)):", P_H)
    print("Likelihood (P(E|H)):", P_E_given_H)
    print("Marginal Probability (P(E)):", P_E)
    print("Posterior Probability (P(H|E)):", P_H_given_E)

    # Step Two: Fuzzy Logic
    muLow = 1 - P_H_given_E  # Low Threat
    muHigh = P_H_given_E  # High Threat

    print("\nStep Two:\nLow Threat (μLow):", muLow)
    print("High Threat (μHigh):", muHigh)

    if muHigh > muLow:
        print("Glutamate is activated.")
    else:
        print("Rest state is maintained.")

    # Step Three: Activation with Threshold
    time_in_seconds = 6284
    if time_in_seconds < 3600:
        print("\nStep Three:\nTime (t):", time_in_seconds, "seconds")
        print("Program stops as t < 3600.")
        return

    # Threshold function f(t) implemented inline
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

    # Step Four: Bayesian Inference Two
    P_H = muHigh  # Updated Prior Probability
    P_E_given_H = 0.56  # Likelihood that life is in danger
    P_E_given_not_H = muLow  # Likelihood that life is not in danger

    P_E = P_E_given_H * P_H + P_E_given_not_H * (1 - P_H)  # Marginal Probability
    P_H_given_E = (P_E_given_H * P_H) / P_E  # Posterior Probability

    print("\nStep Four:\nUpdated Prior Probability (P(H)):", P_H)
    print("Likelihood (P(E|H)):", P_E_given_H)
    print("Marginal Probability (P(E)):", P_E)
    print("Posterior Probability (P(H|E)):", P_H_given_E)

    # Step Five: Proof
    proof_condition = P_H_given_E > 0.80
    if proof_condition:
        print("\nStep Five:\nCondition (P(H|E) > 0.80) is TRUE.")
        print("(p ∧ r) ∨ q holds true.")
    else:
        print("\nStep Five:\nCondition (P(H|E) > 0.80) is FALSE.")


if __name__ == "__main__":
    main()