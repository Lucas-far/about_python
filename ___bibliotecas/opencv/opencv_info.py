

import cv2
from random import choice


class OpenCv:

    @staticmethod
    def install():
        print('pip install opencv-python')

    @staticmethod
    def import_opencv():
        print('import cv2')

    @staticmethod
    def import_image():
        return cv2.imread('pycharm.png', 0)  # par2 = -1/0/1

    @staticmethod
    def show_image():
        cv2.imshow('Pycharm', OpenCv.import_image())
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def show_image_resized():
        image_var = cv2.resize(OpenCv.import_image(), (400, 200))  # largura, altura
        cv2.imshow('Pycharm', image_var)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def show_image_rotated():
        # ROTATE_90_CLOCKWISE    ROTATE_90_COUNTERCLOCKWISE
        image_var = cv2.rotate(OpenCv.import_image(), cv2.cv2.ROTATE_180)
        cv2.imshow('Pycharm', image_var)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def save_image_as():
        cv2.imwrite('pycharm2.jpg', OpenCv.import_image())

    @staticmethod
    def image_info():
        img = cv2.imread('pycharm.png', -1)
        img2 = OpenCv.import_image()
        img3 = cv2.resize(img, (400, 200))
        print(f'Imagem normal         || (dividido) || Altura={img.shape[0]} Largura={img.shape[1]} Canais={img.shape[2]}')
        print(f'Imagem preto e branco || (dividido) || Altura={img2.shape[0]} Largura={img2.shape[1]}')
        print(f'Imagem redimensionada || (global)   || {img3.shape}')

    @staticmethod
    def image_change_pixel_at_random():
        # Valores baseados na proporçãod a imagem alvo na função
        img_height = [*range(0, 395)]
        img_width = [*range(0, 640)]
        inks = [*range(0, 256)]

        img = cv2.imread('pycharm.png', -1)

        index = 0
        while index < 10_000:  # 10.000 = quantidade de coordenadas que terão seu pixel modificado
            img[choice(img_height)][choice(img_width)] = [choice(inks), choice(inks), choice(inks)]
            index += 1

        cv2.imshow('Pycharm editado', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def next():
        pass
        # img = cv2.imread('pycharm.png', -1)
        # img2 = cv2.imread('brave.png', -1)
        # piece = img2[0:50, 0:45]
        # img[0:100, 0:94] = piece
        # # img = cv2.imread('brave.png', -1)
        # # print(img.shape)  # (51, 45, 3)
        #
        # cv2.imshow('Pycharm editado', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == '__main__':
    opencv = OpenCv()

    # Configurando uma imagem para exibição
    pycharm_logo = opencv.import_image()

    # TODO: Exibindo a imagem
    # opencv.show_image(tab_label='Logo', image_var=pycharm_logo)

    # TODO: Exibindo a imagem com tamanho customizado
    # opencv.show_image_resized()

    # TODO: Exibir imagem com rotação
    # opencv.show_image_rotated()

    # TODO: Salvar imagem, de preferência caso ela tenha sido modificada (pode salvar em outro formato)
    # opencv.save_image_as()

    # TODO: Mostrar informações da imagem, como: Altura, largura, canais
    # opencv.image_info()

    # TODO: Pega partes da cor de uma imagem e modifica-as aleatoriamente
    # opencv.image_change_pixel_at_random()
