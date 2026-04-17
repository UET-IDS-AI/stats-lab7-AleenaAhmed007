"""
AI_stats_lab.py

Lab: Uniform Random Variable Analysis
"""

import numpy as np


def uniform_analysis(a, n_samples=10000):
    """
    Returns:
    (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )
    """
    # X ~ Uniform(0, a)
    # : mean = a/2, variance = a^2/12
    theoretical_mean = a / 2
    theoretical_variance = (a ** 2) / 12

    # Sample statistics
    samples = np.random.uniform(0, a, n_samples)
    sample_mean = np.mean(samples)
    sample_variance = np.var(samples)

    # Errors
    mean_error = abs(sample_mean - theoretical_mean)
    variance_error = abs(sample_variance - theoretical_variance)

    # Z = 2X + 1
    # E[Z] = 2*E[X] + 1 = 2*(a/2) + 1 = a + 1
    # Var[Z] = 4*Var[X] = 4*(a^2/12) = a^2/3
    transformed_mean = 2 * theoretical_mean + 1
    transformed_variance = 4 * theoretical_variance

    return (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )


if __name__ == "__main__":
    print("Implement uniform_analysis(a, n_samples=10000)")