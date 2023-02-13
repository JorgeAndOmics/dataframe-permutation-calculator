import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def permutation_analysis(df, target, significance=0.05, num_permutations=1000):
    """
    Perform permutation analysis on a dataset extracted from a Pandas DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the dataset to be analyzed.
        target (str or int): The target variable.
        significance (float): The significance level. Default value is 0.05.
        num_permutations (int): The number of permutations. Default value is 1000.

    Returns:
        p_value (float): The p-value.
        permuted_stats (numpy.ndarray): The permuted statistics.
    """

    # Get the observed statistic
    observed_stat = df[target].mean()  # You can change this to any other statistic of interest.

    # Generate permuted statistics
    permuted_stats = np.empty(num_permutations)
    for i in range(num_permutations):
        permuted_df = df[target].sample(frac=1, replace=False).reset_index(drop=True)
        permuted_stat = permuted_df.mean()  # You can change this to any other statistic of interest.
        permuted_stats[i] = permuted_stat

    # Calculate the p-value
    p_value = np.sum(permuted_stats >= observed_stat) / num_permutations

    return p_value, permuted_stats


def plot_results(p_value, permuted_stats):
    """
    Visualize the results of the permutation analysis using box plots, histograms, and p-value plots.

    Args:
        p_value (float): The p-value.
        permuted_stats (numpy.ndarray): The permuted statistics.

    Returns:
        None
    """

    # Plot the box plot
    fig, ax = plt.subplots()
    ax.boxplot(permuted_stats)
    ax.axhline(y=observed_stat, color='r', linestyle='-')
    ax.set_xlabel('Permuted statistics')
    ax.set_ylabel('Statistic of interest')
    ax.set_title('Box plot of permuted statistics')
    plt.show()

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.hist(permuted_stats, bins=30)
    ax.axvline(x=observed_stat, color='r', linestyle='-')
    ax.set_xlabel('Statistic of interest')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of permuted statistics')
    plt.show()

    # Plot the p-value plot
    fig, ax = plt.subplots()
    ax.plot(np.arange(len(permuted_stats)), permuted_stats)
    ax.axhline(y=observed_stat, color='r', linestyle='-')
    ax.axhline(y=observed_stat + np.std(permuted_stats), color='r', linestyle='--')
    ax.axhline(y=observed_stat - np.std(permuted_stats), color='r', linestyle='--')
    ax.set_xlabel('Permutation index')
    ax.set_ylabel('Statistic of interest')
    ax.set_title('P-value plot of permuted statistics')
    plt.show()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Perform permutation analysis on a dataset.')
    parser.add_argument('input_file', type=str, help='The input file containing the dataset.')
    parser.add_argument('target', type=str, help='The target variable.')
    parser.add_argument('--significance', type=float, default=0.05, help='The significance level.')
    parser.add_argument('--num_permutations', type=int, default=1000, help='The number of permutations.')
    args = parser.parse_args()

    # Load the input file into a pandas DataFrame
    df = pd.read_csv(args.input_file)

    # Perform the permutation analysis
    p_value, permuted_stats = permutation_analysis(df, args.target, args.significance, args.num_permutations)

    # Print the results
    observed_stat = df[args.target].mean()
    print(f'Observed statistic: {observed_stat:.2f}')
    print(f'P-value: {p_value:.4f}')

    # Visualize the results
    plot_results(p_value, permuted_stats)

    # Export the results to a CSV file
    output_file = f'results_{args.target}.csv'
    df_stats = pd.DataFrame({'Permuted stats': permuted_stats})
    df_stats.to_csv(output_file, index=False)

if __name__ == '__main__':
    main()

