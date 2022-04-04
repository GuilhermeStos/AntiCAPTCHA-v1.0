# import cv2, os, pickle
# import numpy as np
# from imutils import paths
# from sklearn.preprocessing import LabelBinarizer
# from sklearn.model_selection import train_test_split
# from keras.models import Sequential
# from keras.layers.convolutional import Conv2D, MaxPooling2D
# from keras.layers.core import Flatten, Dense
# from helpers import resize_to_fit

# data = []
# labels = []
# base_folder = "dbLetters"

# images = paths.list_images(base_folder)

# for file in images:
#     label = file.split(os.path.sep)[-2]
#     img = cv2.imread(file)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Padronizar a imagem em 20x20
#     img = resize_to_fit(img, 20, 20)

#     # Adicionar uma dimensão para o Keras ler a imagem
#     img = np.expand_dims(img, axis=2)

#     # Adicionar as listas de data e labels
#     labels.append(label)
#     data.append(img)

# # Padronizando os dados e criando listas Numpy
# data = np.array(data, dtype='float') / 255
# labels = np.array(labels)

# # Separação em dados de treino (75%) e teste (25%)
# (X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

# # Converter com one-hot encoding
# lb = LabelBinarizer().fit(Y_train)
# Y_train = lb.transform(Y_train)
# Y_test = lb.transform(Y_test)

# # Salvar o LabelBinarizer com o Pickle
# with open('src/model/label_model.dat', 'wb') as pickle_file:
#     pickle.dump(lb, pickle_file)

# # Criar e treinar o modelo
# model = Sequential()

# # Criar camadas da rede neural
# # 1st layer
# model.add(Conv2D(20, (5, 5), padding='same', input_shape=(20, 20, 1), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# # 2nd layer
# model.add(Conv2D(50, (5, 5), padding='same', activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# # 3rd layer
# model.add(Flatten())
# model.add(Dense(500, activation='relu'))

# # Output layer
# model.add(Dense(26, activation='softmax'))

# # Compilar camadas
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Treinar o modelo
# model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=26, epochs=10, verbose=1)

# # Salvar o modelo
# model.save("src/model/trained_model.hdf5")
