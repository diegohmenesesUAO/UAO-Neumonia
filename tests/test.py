import unittest
import numpy as np
from PIL import Image
import pydicom
import cv2
import os

# Funciones a probar
def read_dicom_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    img = pydicom.dcmread(path)  # Usar pydicom.dcmread en lugar de dicom.read_file
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    return img_RGB, img2show

def read_jpg_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"No se pudo leer el archivo: {path}")
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    return img2, img2show

def preprocess(array):
    array = cv2.resize(array, (512, 512))
    array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4))
    array = clahe.apply(array)
    array = array / 255
    array = np.expand_dims(array, axis=-1)
    array = np.expand_dims(array, axis=0)
    return array

# Pruebas unitarias
class TestUtils(unittest.TestCase):
    # Prueba para verificar si la función read_dicom_file devuelve un array numpy y una imagen PIL
    def test_read_dicom_file(self):
        dicom_path = 'test_data/ejemplo.dcm'  # Ruta a un archivo DICOM de prueba
        if not os.path.exists(dicom_path):
            self.skipTest(f"El archivo de prueba DICOM no existe: {dicom_path}")
        image, image_show = read_dicom_file(dicom_path)
        self.assertIsInstance(image, np.ndarray)
        self.assertIsInstance(image_show, Image.Image)
    
    # Prueba para verificar si la función read_jpg_file devuelve un array numpy y una imagen PIL
    def test_read_jpg_file(self):
        jpg_path = 'test_data/ejemplo.jpg'  # Ruta a un archivo JPG de prueba
        if not os.path.exists(jpg_path):
            self.skipTest(f"El archivo de prueba JPG no existe: {jpg_path}")
        image, image_show = read_jpg_file(jpg_path)
        self.assertIsInstance(image, np.ndarray)
        self.assertIsInstance(image_show, Image.Image)

    # Prueba para verificar si la función preprocess devuelve un array con las dimensiones esperadas
    def test_preprocess(self):
        sample_image = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
        processed_image = preprocess(sample_image)
        self.assertEqual(processed_image.shape, (1, 512, 512, 1))

if __name__ == '__main__':
    unittest.main()
