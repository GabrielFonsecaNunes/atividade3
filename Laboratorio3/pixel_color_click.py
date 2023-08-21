import cv2
import numpy as np

# Inicializa a câmera
cap = cv2.VideoCapture(0)

# Define o evento de clique do mouse
def on_mouse_click(event, x, y, flags, param):
    
    def bgr_to_hsv(bgr):
        """
        Converte um valor de cor BGR para HSV.
        Args:
            b: Valor da cor azul.
            g: Valor da cor verde.
            r: Valor da cor vermelha.
        Returns:
            Uma tupla contendo os valores de cor HSV.
        """
        # Converte os valores RGB para valores entre 0 e 1. Para cada cor em  B G R divide por 255 e retorna em ordem
        bgr_normalize = tuple(map(lambda color: color / 255, bgr))

        b = bgr_normalize[0]
        g = bgr_normalize[1]
        r = bgr_normalize[2]

        m = max(bgr_normalize)
        n = min(bgr_normalize)
        # Diferença entre maximo e minimo (r, g, b)
        s = m - n
        # Maximo de r g b
        v = m

        if s == 0:
            # Se a saturação for zero, a cor é cinza, então o valor é o mesmo que o valor de luminosidade.
            h = 0
        else:
            # Calcula o valor de matiz.
            if m == r:
                h = (g - b) / s
            elif m == g:
                h = 2 + (b - r) / s
            else:
                h = 4 + (r - g) / s
            h *= 60
            if h < 0:
                h += 360
        return [h, s, v]

    # Verifica se o evento é de clique
    if event == cv2.EVENT_LBUTTONDOWN:
        # Obtém o valor da cor do pixel clicado
        pixel_color_bgr = list(frame[x, y])
        pixel_color_rgb = [color for color in reversed(pixel_color_bgr)]
        pixel_color_rgb_hex = [f"{color:02x}" for color in reversed(pixel_color_bgr)]
        pixel_color_hsv = bgr_to_hsv(bgr= pixel_color_bgr)
        print(f"[x, y]: [{x}, {y}]")
        print(f"[R G B]: {pixel_color_rgb}")
        print(f"[B G R]: {pixel_color_bgr}")
        print(f"[H S V]: {pixel_color_hsv}")
        print(f"RGB_HEX: # {''.join(pixel_color_rgb_hex)}")

# Registra o evento de clique do mouse
cv2.namedWindow("Clique no pixel")
cv2.setMouseCallback("Clique no pixel", on_mouse_click)

# Loop principal
while True:
    # Captura um frame da câmera
    ret, frame = cap.read()

    # Exibe o frame na tela
    cv2.imshow("Clique no pixel", frame)

    # Verifica se a tecla ESC foi pressionada
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Fecha a câmera
cap.release()

# Fecha todas as janelas abertas
cv2.destroyAllWindows()
