from __future__ import division
import plotly
from plotly.graph_objs import Scatter, Layout, Figure

initial_block_reward = 5000 
block_interval_secs = 60 * 1
halving_interval_blocks = 2100000
init_year = 2018

def calculate_coin_count(blocks):
    bitcoin_coin_count = []
    block_rewards = calculate_block_rewards(blocks)
    for i, block in enumerate(blocks):
        if len(bitcoin_coin_count) == 0:
            bitcoin_coin_count.append(0)
        else:
            bitcoin_coin_count.append((block_rewards[i-1] * halving_interval_blocks) + bitcoin_coin_count[i-1])
    return bitcoin_coin_count

def calculate_block_rewards(blocks):
    block_rewards = []
    for i, block in enumerate(blocks):
        if len(block_rewards) == 0:
            block_rewards.append(initial_block_reward)
        else:
            block_rewards.append(block_rewards[i-1]/2)
    return block_rewards

def calculate_years(blocks):
    seconds_per_year = 31540000
    years = []
    for i, block in enumerate(blocks):
        if len(years) == 0:
            years.append(init_year)
        else:
            years.append(init_year + ((blocks[i] * block_interval_secs)/seconds_per_year)) 
    return years 

blocks = range(0, halving_interval_blocks * 13, halving_interval_blocks)
print "blocks", blocks
print "block reward", calculate_block_rewards(blocks)
print "coin count", calculate_coin_count(blocks)
print "years", calculate_years(blocks)

bitcoin_coins = Scatter(
    x=blocks,
    y=calculate_coin_count(blocks),
    name='bitcoin_coins'
)
block_reward = Scatter(
    x=calculate_years(blocks),
    y=calculate_block_rewards(blocks),
    name='block_reward',
    xaxis='x2',
    yaxis='y2'
) 

data = [bitcoin_coins, block_reward]

layout = Layout(
    title='Bitcoin Distribution Schedule',
    xaxis=dict(
        title='Blocks',
        titlefont=dict(
            color='rgb(148,103,189)'
        ),
        tickfont=dict(
            color='rgb(148,103,189)'
        ),
        domain=[0, .45]
    ),
    xaxis2=dict(
        title='Year',
        titlefont=dict(
            color='rgb(148,103,189)'
        ),
        tickfont=dict(
            color='rgb(148,103,189)'
        ),
        domain=[.55,1]
    ),
    yaxis2=dict(
        title='Block Reward',
        titlefont=dict(
            color='rgb(253, 127, 40)'
        ),
        tickfont=dict(
            color='rgb(253, 127, 40)'
        ),
	anchor='x2',
	overlaying='y',
	side='right'
    )
)

fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='index.html')
