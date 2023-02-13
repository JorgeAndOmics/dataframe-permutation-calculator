
# Dataframe Permutation Calculator

This Python script performs a permutation analysis on a dataset extracted from a Pandas DataFrame, using a specified target variable. The permutation analysis generates permuted statistics and calculates the p-value for the observed statistic. The results are visualized using box plots, histograms, and p-value plots. The script also exports the results to a CSV file.

## Requirements

-   Python 3.x
-   Pandas
-   NumPy
-   Matplotlib

## Usage

The script takes the following command line arguments:

    usage: script.py [-h] [--significance SIGNIFICANCE] [--num_permutations NUM_PERMUTATIONS] input_file target
    
    Perform permutation analysis on a dataset.
    
    positional arguments:
      input_file            The input file containing the dataset.
      target                The target variable.
    
    optional arguments:
      -h, --help            show this help message and exit
      --significance SIGNIFICANCE
                            The significance level. Default is 0.05.
      --num_permutations NUM_PERMUTATIONS
                            The number of permutations. Default is 1000.

To run the script, type the following command:

    python script.py input_file target [--significance SIGNIFICANCE] [--num_permutations NUM_PERMUTATIONS]

For example:

    python script.py data.csv feature1 --significance 0.01 --num_permutations 5000 

## Output

The script generates the following output:

-   Observed statistic: the observed statistic for the target variable
-   P-value: the p-value for the observed statistic
-   Box plot of permuted statistics: a box plot of the permuted statistics
-   Histogram of permuted statistics: a histogram of the permuted statistics
-   P-value plot of permuted statistics: a plot of the permuted statistics and the observed statistic, with the 95% confidence interval indicated by dashed lines
-   results_target.csv: a CSV file containing the permuted statistics

## License

This script is licensed under the MIT License. 
