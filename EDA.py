#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as p

# Read the CSV files
df_v2 = pd.read_csv('v2.csv')
df_v3 = pd.read_csv('v3.csv')

# Remove the 'profit_and_loss' column
df_v2 = df_v2.drop('profit_and_loss', axis=1)
df_v3 = df_v3.drop('profit_and_loss', axis=1)

# Check if both DataFrames are the same
print(df_v2.equals(df_v3))  # True

# Filter Amethyst data
df_amethyst = df_v2.loc[df_v2['product'] == 'AMETHYSTS']
df_amethyst['timestamp_100'] = df_amethyst['timestamp'] / 100

#Create a spread column
df_amethyst['spread'] = df_amethyst['ask_price_1'] - df_amethyst['bid_price_1']

#Only select the first 100
df_amethyst = df_amethyst.head(100)

# Plot bid_price_1
buffer = 0.05  # 5% buffer for the y-axis limits
min_price = df_amethyst['bid_price_1'].min()
max_price = df_amethyst['bid_price_1'].max()

#%%
plt.figure(figsize=(10, 5))
plt.plot(df_amethyst['timestamp_100'], df_amethyst['bid_price_1'], label='Bid Price 1')
#Plot bid_price_2
plt.plot(df_amethyst['timestamp_100'], df_amethyst['bid_price_2'], label='Bid Price 2')
#Plot bid_price_3
plt.plot(df_amethyst['timestamp_100'], df_amethyst['bid_price_3'], label='Bid Price 3')
plt.xlabel('Timestamp (in 100s)')
plt.ylabel('Bid Price')
plt.title('Bid Price over Time for Amethyst')
plt.ylim(min_price, max_price)
plt.legend()
plt.grid(True)
plt.show()
# %%
df_starfruit = df_v2.loc[df_v2['product'] == 'STARFRUIT']
# %%
#Get the volatility of the STARFRUIT product
star_fruit_volatility = df_starfruit['ask_price_1'].pct_change()
star_fruit_volatility = star_fruit_volatility.dropna()
star_fruit_volatility = star_fruit_volatility.std()
print(f'STARFRUIT Volatility: {star_fruit_volatility}')
# %%
#Plot starfruit ask price
plt.figure(figsize=(10, 5))
plt.plot(df_starfruit['timestamp'], df_starfruit['ask_price_1'], label='Ask Price 1')
# %%
