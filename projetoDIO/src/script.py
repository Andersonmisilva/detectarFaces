import cv2
import os

def detect_faces(image_path):
    # Obtém o caminho completo para a imagem
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.abspath(os.path.join(current_dir, "..", "inputs", image_path))

    # Verifica se o caminho está correto
    print(f"Caminho da imagem: {image_path}")

    # Carrega a imagem em escala de cinza
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Utiliza um classificador pré-treinado para detecção de faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("Nenhuma face detectada.")
        return

    # Desenha retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exibe a imagem com as faces destacadas
    cv2.imshow('Faces Detectadas', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Nome da imagem
    image_name = "image1.jpg"

    # Chama a função para detectar faces na imagem
    detect_faces(image_name)
