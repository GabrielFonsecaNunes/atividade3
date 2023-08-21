# Bibliotecas
import cv2 as cv

# Conversão Espaços de Cores
flags = [i for i in dir(cv) if i.startswith('COLOR_')]

# Imprimindo espaços de cores
print(flags)