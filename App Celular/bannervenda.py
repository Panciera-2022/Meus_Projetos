from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Canvas, Rectangle


class BannerVenda(GridLayout):
    def __int__(self, **kwargs):
        super().__init__()

        cliente = kwargs["cliente"]
        foto_cliente = kwargs["foto_cliente"]
        produto = kwargs["produto"]
        foto_produto = kwargs["foto_produto"]
        data = kwargs["data"]
        unidade = kwargs["unidade"]
        quantidade = kwargs["quantidade"]
        preco = kwargs["preco"]

        esquerda = FloatLayout()
        esquerda_imagem = Image(pos_hint={"right": 1, "top": 0.95}, size_hint=(1, 0.75),
                                source=f"icones/fotos_clientes/{foto_cliente}")
        esquerda_label = Label(text=cliente, size_hint=(1, 0.2), pos_hint={"right": 1, "top": 0.2})
        esquerda.add_widget(esquerda_imagem)
        esquerda.add_widget(esquerda_label)

        meio = FloatLayout()

        direita = FloatLayout()

        self.add_widget(esquerda)

        self.add_widget(meio)

        self.add_widget(direita)
