### Bitcoin Arbitrage

Collecting, preparing and analysing historical trade data for Bitcoin on Bitstamp and Coinbase to determine arbitrage opportunities.


## Technologies

Built using Python 3.7 with the following libraries:

-[Pandas](https://github.com/pandas-dev/pandas) to make calculating statistics a breeze, and to add charts and tables for visual data.

## Installation Guide

Check Pandas installed by running this command in your terminal:

```pip list```

Pandas is included in the Anaconda package as standard.

## Usage

To use the analysis, clone the repository and open Jupyter Lab from the cloned repo location.

Open the notebook:

```crypto_arbitrage.ipynb```

To change the dates of analysis, modify the dates in the following places:

```date_from_early = datetime.date(2018,1,1)
date_to_early = datetime.date(2018,1,31)```

```date_from_late = datetime.date(2018,3,1)
date_to_late = datetime.date(2018,3,31)```

```early_date = datetime.date(2018,1,10)```

```middle_date = datetime.date(2018,2,2)```

```late_date = datetime.date(2018,3,7)```

Re-run the notebook to update all charts and dataframes.

Note, the comments explaining some of the observed differences across the original dates will note update as the dates change.

## Contributors

This app was built by [Toni Mercer](https://www.linkedin.com/in/toni-mercer/) using the Starter Code from the UW FinTech Bootcamp course. 

---

## License

MIT





