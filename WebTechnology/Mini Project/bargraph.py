import base64
import io
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('fide_historical.csv')
values = 10
df = df.head(values)
grouped = df.groupby('country')['rating'].sum()

fig, ax = plt.subplots()
ax.bar(grouped.index, grouped.values)

ax.set_title('Bar Graph')
ax.set_xlabel('Country')
ax.set_ylabel('Rank')

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)

image_data = base64.b64encode(buffer.getvalue()).decode()
html = f'data:image/png;base64,{image_data}'
