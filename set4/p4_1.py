def warehouse_process(dictionary: dict, transaction: tuple):
    """Função que recebe ou exporta mercadorias"""

    transaction_type, commodity, unity = transaction

    if transaction_type == 'receive':
        dictionary[commodity] = dictionary.get(commodity, 0) + unity

    elif transaction_type == 'ship':
        dictionary[commodity] = dictionary.get(commodity, 0)
        dictionary[commodity] = dictionary[commodity] - unity

        if dictionary[commodity] < 0:
            dictionary[commodity] = 0
            print('not enough')
    
class Warehouse:
    """Classe para representar um comércio."""

    def __init__(self):
        self.dictionary = { }
    
    def process(self, transaction: tuple):
        """Função que recebe ou exporta mercadorias"""

        transaction_type, commodity, unity = transaction

        if transaction_type == 'receive':
            self.dictionary[commodity] = self.dictionary.get(commodity, 0) + unity

        elif transaction_type == 'ship':
            self.dictionary[commodity] = self.dictionary.get(commodity, 0)
            self.dictionary[commodity] = self.dictionary[commodity] - unity

            if self.dictionary[commodity] < 0:
                self.dictionary[commodity] = 0
                print('not enough')

    def lookup(self, commodity: str):
        """Função que exibe a quantidade de uma mercadoria"""

        return self.dictionary.get(commodity, 0)