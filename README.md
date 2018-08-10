# Altcoin Deflation Calculator
Creates plotly charts to show altcoin deflation over time

<p align="center">
    <img src="https://raw.githubusercontent.com/JBaczuk/altcoin_deflation_calculator/master/example.png" alt="Example Chart">
</p>

## Usage
```
git clone https://github.com/JBaczuk/altcoin_deflation_calculator.git
cd altcoin_deflation_calculator
./generate_plot.sh
```

You can adjust the distribution parameters at the top of `plot.py`:

```
initial_block_reward = 4285
block_interval_secs = 60 * 1
halving_interval_blocks = 2100000
init_year = 2018
premine = 3000000000
halving_count = 15 # how many halvings to show on the graph
```
