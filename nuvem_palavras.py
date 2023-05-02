#Escreva um programa Python que leia um arquivo de texto e gere uma nuvem de palavras com as palavras mais frequentes.
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

with open("texto.txt", "r") as f:
    texto = f.read()

palavras = texto.lower().replace(".", "").replace(",", "").split()

contagem = Counter(palavras)

wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate_from_frequencies(contagem)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig("nuvem_palavras.png")