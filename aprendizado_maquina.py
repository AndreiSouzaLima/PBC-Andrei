#Escreva um programa Python que implemente um algoritmo de aprendizado de máquina, como regressão linear ou classificação de dados.
from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

print("Coeficiente de determinação (R²):", model.score(x, y))

x_test = np.array([6]).reshape(-1, 1)
y_pred = model.predict(x_test)
print("Valor previsto para x=6:", y_pred[0][0])