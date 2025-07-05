import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Dominio de la función
x = np.linspace(0, 5, 1000)
X = -50*(x -3)**2
# Evaluar sigmoide de TensorFlow
x_tf = tf.convert_to_tensor(X, dtype=tf.float32)
sigmoid_tf = 2*tf.sigmoid(x_tf)
print(max(sigmoid_tf.numpy()))

# Graficar
plt.figure(1)
plt.plot(x, sigmoid_tf.numpy(), color='blue')
plt.title('Condición de Nacimiento', fontsize=16)
plt.xlabel('N', fontsize=14)
plt.ylabel(r'$\sigma(Muerta, N)$', fontsize=14)
plt.grid(True)

# Dominio de la función
x2 = np.linspace(0, 5, 1000)
X2 = -50*(x2 -3)*(x-2)
# Evaluar sigmoide de TensorFlow
x_tf2 = tf.convert_to_tensor(X2, dtype=tf.float32)
sigmoid_tf2 = tf.sigmoid(x_tf2)
print(max(sigmoid_tf2.numpy()))


# Graficar
plt.figure(2)
plt.plot(x2, sigmoid_tf2.numpy(), color='blue')
plt.title('Condición de Supervivencia', fontsize=16)
plt.xlabel('N', fontsize=14)
plt.ylabel(r'$\sigma(Viva, N)$', fontsize=14)
plt.grid(True)
# plt.show()

# Dominio de la función
x3 = np.linspace(-10, 10, 1000)

# Evaluar sigmoide de TensorFlow
x_tf3 = tf.convert_to_tensor(x3, dtype=tf.float32)
sigmoid_tf3 = tf.sigmoid(x_tf3)
print(max(sigmoid_tf3.numpy()))


# Graficar
plt.figure(3)
plt.plot(x3, sigmoid_tf3.numpy(), color='blue')
plt.title('Función Sigmoide', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel(r'$\sigma(x)$', fontsize=14)
plt.grid(True)
plt.show()