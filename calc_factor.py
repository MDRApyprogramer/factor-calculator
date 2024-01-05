# imports
from rich.console import Console
from rich.prompt import Prompt

console = Console()
prompt = Prompt()


class CalculationOperation:
    def __init__(self):
        self.products: dict = {}

    def update(self, value: dict):
        """enter a dict param to updating product list"""
        try:
            self.products.update(value)
            # Top line :  value should be a dictionary -> {product name : [product price, product off, product number]}
        except ValueError:
            print(f"CalculationOperation: ValueError: please enter dict data type, your data type is {type(value)}")

    def calc_pay(self):
        products_info = []
        all_price = []
        for name in list(self.products.keys()):  # product name
            values = self.products.get(name)  # [price, off, number]
            price_product, off_product, number_product = values[0], values[1], values[2]
            info = {  # one product information save in dictionary
                'product name': name,
                'price before off': price_product,
                'off': off_product,
                'Price after off': (price_product - (price_product * off_product)),
                'Number': number_product,
                'Total price': (number_product * (price_product - (price_product * off_product)))
            }
            all_price.append(info.get('Total price'))  # info>Total price
            a = info.copy()
            products_info.append(a)
        total_price = 0  # total price all products
        for i in all_price:
            total_price += i
        return f'{products_info}, \n {total_price}'


while True:
    products = CalculationOperation()
    command = prompt.ask('What do you want me to do ?', choices=['calculate', 'exit', '1', '2'])

    if command == 'exit' or command == '2':
        exit()

    elif command == 'calculate' or command == '1':
        while True:
            try:
                product = console.input('please enter , [bold green underline]product name[/] : ')
                number = console.input('please enter , [bold green underline]product number[/] : ')
                price = console.input('please enter , [bold green underline]product price[/] : ')
                off = console.input('please enter , [bold green underline]off[/] : ')
                print('loading')

                number = int(number)  # convert number to integer
                price = int(price)  # convert price to integer

                # convert off to the float
                if len(off) == 2:
                    off = (float(f'0.{off}'))

                elif len(off) == 1:
                    off = (float(f'0.0{off}'))

                elif len(off) > 2:
                    off = (float(f'{off[:-2]}.{off[-2]}'))

            except ValueError:
                console.print('Please enter the number and payment in number', style='underline red')

                # console.print('Sorry, the app encountered a problem', style='red on white')

            else:
                products.update({product: [price, off, number]})
                command = prompt.ask('do you going to continue ? ', choices=['y', 'N'])

                if command == 'N':
                    print(products.calc_pay())
                    break

                elif command == 'y':
                    pass  # for run program again

