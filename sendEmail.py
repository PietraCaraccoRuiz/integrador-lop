import pyautogui
import time

print("Posicione o mouse onde deseja capturar a posição...")
time.sleep(5)  # Você tem 5 segundos para posicionar o mouse

x, y = pyautogui.position()
print(f"Posição do mouse: x={x}, y={y}")