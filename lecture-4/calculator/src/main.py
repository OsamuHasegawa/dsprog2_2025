import flet as ft
import math


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, on_click, expand=1):
        super().__init__()
        self.text = text
        self.data = text
        self.expand = expand
        self.on_click = on_click


class DigitButton(CalcButton):
    def __init__(self, text, on_click, expand=1):
        super().__init__(text, on_click, expand)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, on_click):
        super().__init__(text, on_click)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text, on_click):
        super().__init__(text, on_click)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK


class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=24)

        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20

        self.content = ft.Column(
            controls=[
                ft.Row([self.result], alignment="end"),
                ft.Row(
                    [
                        ExtraActionButton("AC", self.click),
                        ExtraActionButton("√", self.click),
                        ExtraActionButton("x²", self.click),
                        ExtraActionButton("sin", self.click),
                        ExtraActionButton("cos", self.click),
                    ]
                ),
                ft.Row(
                    [
                        DigitButton("7", self.click),
                        DigitButton("8", self.click),
                        DigitButton("9", self.click),
                        ActionButton("/", self.click),
                    ]
                ),
                ft.Row(
                    [
                        DigitButton("4", self.click),
                        DigitButton("5", self.click),
                        DigitButton("6", self.click),
                        ActionButton("*", self.click),
                    ]
                ),
                ft.Row(
                    [
                        DigitButton("1", self.click),
                        DigitButton("2", self.click),
                        DigitButton("3", self.click),
                        ActionButton("-", self.click),
                    ]
                ),
                ft.Row(
                    [
                        DigitButton("0", self.click, expand=2),
                        DigitButton(".", self.click),
                        ActionButton("+", self.click),
                    ]
                ),
                ft.Row([ActionButton("=", self.click)]),
            ]
        )

    def reset(self):
        self.operator = "+"
        self.operand = 0
        self.new = True

    def click(self, e):
        d = e.control.data

        if d == "AC":
            self.result.value = "0"
            self.reset()

        elif d.isdigit() or d == ".":
            if self.new:
                self.result.value = d
                self.new = False
            else:
                self.result.value += d

        elif d in "+-*/":
            self.operand = float(self.result.value)
            self.operator = d
            self.new = True

        elif d == "=":
            a = self.operand
            b = float(self.result.value)
            if self.operator == "+":
                self.result.value = str(a + b)
            elif self.operator == "-":
                self.result.value = str(a - b)
            elif self.operator == "*":
                self.result.value = str(a * b)
            elif self.operator == "/":
                self.result.value = "Error" if b == 0 else str(a / b)
            self.reset()

        elif d == "√":
            v = float(self.result.value)
            self.result.value = "Error" if v < 0 else str(math.sqrt(v))
            self.reset()

        elif d == "x²":
            v = float(self.result.value)
            self.result.value = str(v * v)
            self.reset()

        elif d == "sin":
            v = float(self.result.value)
            self.result.value = str(math.sin(math.radians(v)))
            self.reset()

        elif d == "cos":
            v = float(self.result.value)
            self.result.value = str(math.cos(math.radians(v)))
            self.reset()

        self.update()


def main(page: ft.Page):
    page.title = "Scientific Calculator"
    page.add(CalculatorApp())


ft.app(main)