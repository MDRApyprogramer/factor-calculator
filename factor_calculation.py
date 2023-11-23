#imports
from rich.console import Console
from rich.prompt import Prompt

console = Console()
prompt = Prompt()

console.rule('[bold yellow]hello')
console.rule('[bold blue]wellcome to program')

add_list = {} # add list the valu e for add to class

class CallculationOperation:
    '''give a dict , for key value give product name'''
    def __init__(self, *args : dict):
        self.args = {}
        for i in args[1:]:
            self.args.update(i)

    def callculation_pay(self):
        information_of_all_products = []
        price_of_all_products = []
        product = list(self.args.keys())
        list_product_price = list(self.args.values())
        for i in list_product_price : # a = [product price, Discount, product number]
            price_product = i[0] - (i[0] * i[1])
            price = (i[2] * price_product)
            information = {'product name' : product[list_product_price.index(i)], 'price before discount' : i[0],'Discount' : i[1] , 'Price_after discount' : price_product, 'Number' : i[2], 'Total price' : price}
            price_of_all_products.append(price)
            information_of_all_products.append(information)
        num = 0
        for i in price_of_all_products:
            num += i
        return f'{information_of_all_products}, \n {num}'

command = 'close'
while command == 'close':
    console.print('1.calculate | 2.exit')
    command = input('what do you going to did ? ')
    print('loading')
    if command not in ['calculate', 'exit', '1', '2']:
        console.print("I don't understand what you mean. Please ask for something that I can implement",  style='underline red')
        command = prompt.ask('what do you going to did ? ', choices=['calculate', 'exit'])
        print('loading')

    if command == 'exit':
        console.rule('[bold red]goodbye')
        exit()

    while command in ['calculate','1']:
        try :
            product = console.input('please give , [bold green underline]product name[/] : ')
            number =  int(console.input('please give , [bold green underline]product number[/] : '))
            price = int(console.input('please give , [bold green underline]product price[/] : '))
            Discount = console.input('please give , [bold green underline]Discount[/] : ')
            print('loading')

            if len(Discount) == 2 :
                Discount = (float(f'0.{Discount}'))

            elif len(Discount) == 1 :
                Discount = (float(f'0.0{Discount}'))

            elif len(Discount) >= 2 :
                Discount = (float(f'{Discount[:-2]}.{Discount[:2]}'))

            
        except ValueError:
            console.print('please give number and pay in numberly', style='underline red')
        except :
            console.print('Sorry, the app encountered a problem', style='red on white')
        
        else :
            add_list.update({product : [price, Discount, number]})
            command = prompt.ask('do you going to continue ? ', choices=['y', 'N'])
            print('loading')

            if command == 'N':
                calculation = callculation_operation('a', add_list)
                print(calculation.callculation_pay())
                add_list = {}
                print('----------------')
                command = 'close'
            elif command == 'y':
                command = 'calculate'
                
