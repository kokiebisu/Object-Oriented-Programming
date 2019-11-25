import pandas as pd
import abc
import enum
import datetime


class BrandEnum(enum.Enum):
    """
    This enum specifies the different distinct brand types.
    """
    LULULIME = 0,
    PINEAPPLEREPUBLIC = 1,
    NIKA = 2


class ShirtMen(abc.ABC):
    """
    ShirtMen defines the interface for one of the products the
    abstract factory pettern is responsible to create.
    """

    def __init__(self, style: str, size: str, colour: str, textile: str, **kwargs) -> None:
        self.style = style
        self.size = size  # S, M, L, XL, XXL
        self.colour = colour
        self.textile = textile

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Style: {self.style} \nSize: {self.size} \nColor: {self.colour} \nTextile: {self.textile}"


class ShirtWomen(abc.ABC):
    """
    ShirtWomen defines the interface for one of the products the
    abstract factory pattern is responsible to create.
    """

    def __init__(self, style: str, size: str, colour: str, textile: str, **kwargs) -> None:
        """
        Initializes the object
        :param style: a string
        :param size: a string
        :param colour: a string
        :param textile: a string
        :param kwargs: keyword arguments
        """
        self.style = style
        self.size = size  # XS, S, M, L, XL, XXL
        self.colour = colour
        self.textile = textile

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Style: {self.style} \nSize: {self.size} \nColor: {self.colour} \nTextile: {self.textile}"


class SockPairUnisex(abc.ABC):
    """
    SockPairUnisex defines the interface for one of the products the
    abstract factory pettern is responsible to create.
    """

    def __init__(self, style: str, size: str, colour: str, textile: str, **kwargs) -> None:
        """
        Initializes the object
        :param style: a string
        :param size: a string
        :param colour: a string
        :param textile: a string
        :param kwargs: keyword arguments
        """
        self.style = style
        self.size = size  # S, M, L
        self.colour = colour
        self.textile = textile

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Style: {self.style} \nSize: {self.size} \nColor: {self.colour} \nTextile: {self.textile}"


class BrandFactory(abc.ABC):
    """
    The base factory class. All clothes expect this factory class to
    generate clothes. The BrandFactory class defines an interface
    to create clothes based on different brands.
    """
    @abc.abstractmethod
    def create_shirt_men(self) -> ShirtMen:
        pass

    @abc.abstractmethod
    def create_shirt_women(self) -> ShirtWomen:
        pass

    @abc.abstractmethod
    def create_socks_unisex(self) -> SockPairUnisex:
        pass


class LuluLimeFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenLuluLime,
    ShirtWomenLuluLime, SockPairUnisexLuluLime
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        Creates a ShirtMenLuluLime object
        :return: a ShirtMen
        """
        return ShirtMenLuluLime(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        Creates a ShirtWomenLuluLime object
        :return: a ShirtWomen
        """
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        Creates a SockPairUnisexLuluLime object
        :return: a SockPairUnisex
        """
        return SockPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenPineappleRepublic,
    ShirtWomenPineappleRepublic, SockPairUnisexPineappleRepublic
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        Creates a ShirtMenPineappleRepublic instance
        :return: a ShirtMen
        """
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        Creates a ShirtWomenPineappleRepublic instance
        :return: a ShirtWomen
        """
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        Creates a SockPairUnisexPineappleRepublic instance
        :return: a SockPairUnisex
        """
        return SockPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It
    returns a product family consisting of ShirtMenNika,
    ShirtWomenNika, SockPairUnisexNika
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        """
        Creates a ShirtMenNika instance
        :return: a ShirtMen
        """
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        """
        Creates a ShirtWomenNika instance
        :return: a ShirtWomen
        """
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        """
        Creates a SockPairUnisexNika instance
        :return: a SockPairUnisex
        """
        return SockPairUnisexNika(**kwargs)


class ShirtMenLuluLime(ShirtMen):
    """
    ShirtMenLuluLime is a type of ShirtMen branded by LuluLime
    """

    def __init__(self, sport: str, pockets: int, **kwargs) -> None:
        """
        Initializes the ShirtMenLuluLime object
        :param sport: a string
        :param pockets: an int
        :param kwargs: keyword arguments
        """
        self.sport = sport  # yoga or running
        self.pockets = pockets
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: LuluLime \nGarment Produced: ShirtMen \n{super().__str__()} \nSport: {self.sport} \nPockets: {self.pockets}"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic is a type of ShirtMen branded by PineappleRepublic
    """

    def __init__(self, ironing: bool, button: int, **kwargs) -> None:
        """
        Initializes the ShirtMenPineappleRepublic object
        :param ironing: a bool
        :param button: an int
        :param kwargs: keyword arguments
        """
        self.ironing = ironing
        self.button = button
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: PineappleRepublic \nGarment Produced: ShirtMen \n{super().__str__()} \nIroning: {self.ironing} \nButton: {self.button}"


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika is a type of ShirtMen branded by Nike
    """

    def __init__(self, garment: str, **kwargs) -> None:
        """
        Initializes the ShirtMenNika object
        :param garment: a string
        :param kwargs: keyword arguments
        """
        self.garment = garment  # indoor or outdoor sports
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return:
        """
        return f"Brand: Nika \nGarment Produced: ShirtMen \n{super().__str__()} \nGarment: {self.garment}"


class ShirtWomenLuluLime(ShirtWomen):
    """
    ShirtWomenLuluLime is a type of ShirtWomen branded by Lululime
    """

    def __init__(self, garment: str, pockets: int, **kwargs) -> None:
        """
        Initializes the ShirtWomenLuluLime object
        :param garment: a string
        :param pockets: an int
        :param kwargs: keyword arguments
        """
        self.garment = garment  # yoga or running
        self.pockets = pockets
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: LuluLime \nGarment Produced: ShirtWomen \n{super().__str__()} \nGarment: {self.garment} \nPockets: {self.pockets}"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic is a type of ShirtWomen branded by PineappleRepublic
    """

    def __init__(self, ironing: bool, button: int, **kwargs):
        """
        Initializes the ShirtWomenPineappleRepublic object
        :param ironing: a bool
        :param button: an int
        :param kwargs: keyword arguments
        """
        self.ironing = ironing
        self.button = button
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: PineappleRepublic \nGarment Produced: ShirtWomen \n{super().__str__()} \nIroning: {self.ironing} \nButton: {self.button}"


class ShirtWomenNika(ShirtWomen):
    """
    ShirtWomenNika is a type of ShirtWomen branded by Nika
    """

    def __init__(self, garment_: str, **kwargs) -> None:
        """
        Initializes the ShirtWomenNika object
        :param garment: a string
        :param kwargs: keyword arguments
        """
        self._garment = garment_  # indoor or outdoor sports
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: Nika \nGarment Produced: ShirtWomen \n{super().__str__()} \n Garment: {self._garment}"


class SockPairUnisexLuluLime(SockPairUnisex):
    """
    SockPairUnisexLuluLime is a type of SockPairUnisex branded by Lululime
    """

    def __init__(self, silver: bool, stripe: str, **kwargs) -> None:
        """
        Initializes the SockPairUnisexLuluLime object
        :param silver: a bool
        :param stripe: a string
        :param kwargs: keyword arguments
        """
        self.silver = silver
        self.stripe = stripe
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: LuluLime \nGarment Produced: SockPairUnisex \n{super().__str__()} \nSilver: {self.silver} " \
               f"\nStripe: {self.stripe}"


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SockPairUnisexPineappleRepublic is a type of SockPairUnisex branded by PineappleRepublic
    """

    def __init__(self, dry_cleaning: bool, **kwargs) -> None:
        """
        Initializes the SockPairUnisexPineappleRepublic object
        :param dry_cleaning: a bool
        :param kwargs: keyword arguments
        """
        self.dry_cleaning = dry_cleaning
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return:
        """
        return f"Brand: PineappleRepublic \nGarment Produced: SockPairUnisex \n{super().__str__()} " \
               f"\nDry Cleaning: {self.dry_cleaning}"


class SockPairUnisexNika(SockPairUnisex):
    """
    SockPairUnisexNika is a type of SockPairUnisex branded by Nika
    """

    def __init__(self, articulated: bool, length: str, **kwargs) -> None:
        """
        Initializes the SockPairUnisexNika object
        :param articulated: a bool
        :param length: a string
        :param kwargs: keyword arguments
        """
        self.articulated = articulated
        self.length = length
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the object
        :return: a string
        """
        return f"Brand: Nika \nGarment Produced: SockPairUnisex \n{super().__str__()} " \
               f"\nArticulated: {self.articulated} \nLength: {self.length}"


class ClothesPopulator:
    """
    Responsible for retrieving the right factory for the specified clothes
    """

    def __init__(self):
        """
        Initializes the ClothesPopulator object
        """
        self.brand_factory_mapper = {
            BrandEnum.LULULIME: LuluLimeFactory,
            BrandEnum.PINEAPPLEREPUBLIC: PineappleRepublicFactory,
            BrandEnum.NIKA: NikaFactory
        }

    def get_factory(self, brand_type: BrandEnum) -> BrandFactory:
        """
        Gets the factory class from the given brand type
        :return: a Factory object
        """
        factory_class = self.brand_factory_mapper.get(brand_type, None)
        return factory_class()


class OrderProcessor:
    """
    Responsible for processing the Excel spreadsheet.
    It is instantiated by the GarmentMaker class.
    """

    def __init__(self) -> None:
        """
        Initializes the OrderProcessor object
        """
        self.data = None
        self.populator = ClothesPopulator()
        self.brands = {
            "Lululime": BrandEnum.LULULIME,
            "PineappleRepublic": BrandEnum.PINEAPPLEREPUBLIC,
            "Nika": BrandEnum.NIKA
        }
        self.item_list = []

    def open_order_sheet(self, file_name: str) -> None:
        """
        Reads the excel file from the given filepath and
        extracts the orders from the spreadsheet, one row at a time
        """
        dataframe = pd.read_excel(file_name)
        self.data = dataframe

    def process_next_order(self) -> None:
        """
        Responsible for identifying the correct factory to use for each order.
        It stores the order details and the associated factory in an object of type Order and returns it
        :return: an Order object
        """

        i = 0
        while i < len(self.data.index):
            data = self.data.iloc[i]
            detail_dict = {'Date': data['Date'], 'Order Number': data['Order Number'], 'Brand': data['Brand'],
                           'Garment': data['Garment'], 'Count': data['Count'], 'Style name': data['Style name'],
                           'Size': data['Size'], 'Colour': data['Colour'], 'Textile': data['Textile'],
                           'Sport': data['Sport'], 'Hidden Zipper Pockets': data['Hidden Zipper Pockets'],
                           'Dry Cleaning': data['Dry Cleaning'], 'Indoor/Outdoor': data['Indoor/Outdoor'],
                           'Requires Ironing': data['Requires Ironing'], 'Buttons': data['Buttons'],
                           'Articulated': data['Articulated'], 'Length': data['Length'], 'Silver': data['Silver'],
                           'Stripe': data['Stripe']}
            brand_factory = self.populator.get_factory(
                self.brands[detail_dict['Brand']])
            yield Order(factory=brand_factory, details=detail_dict)
            i += 1


class Order:
    """
    Class that holds the associated factory and the details of the order
    """

    def __init__(self, factory: BrandFactory, details: dict) -> None:
        """
        Initializes the Order object
        :param factory: a BrandFactory object
        :param details: a dict
        """
        self._factory = factory
        self._details = details

    @property
    def details(self):
        return self._details

    @property
    def factory(self):
        return self._factory


class GarmentMaker:
    """
    Drives the program
    """

    def __init__(self):
        """
        Initializes three arraylist instance variables shirtsMen, shirts
        """
        self.clothes_populator = ClothesPopulator()
        self.processor = OrderProcessor()
        self.shirts_men = []
        self.shirts_women = []
        self.sock_unisex = []

    @staticmethod
    def shirt_men_maker(shirt_men_order: Order):
        """
        Creates a ShirtMen object from the given order
        :param shirt_men_order: an Order object
        :return: a ShirtMen object
        """
        factory = shirt_men_order.factory
        return factory.create_shirt_men(style=shirt_men_order.details['Style name'],
                                        size=shirt_men_order.details['Size'],
                                        colour=shirt_men_order.details['Colour'],
                                        textile=shirt_men_order.details['Textile'],
                                        sport=shirt_men_order.details['Sport'],
                                        pockets=shirt_men_order.details['Hidden Zipper Pockets'],
                                        ironing=shirt_men_order.details['Requires Ironing'],
                                        button=shirt_men_order.details['Buttons'],
                                        garment=shirt_men_order.details['Indoor/Outdoor'],
                                        )

    @staticmethod
    def shirt_women_maker(shirt_women_order: Order):
        """
        Creates a ShirtWomen object from the given order
        :param shirt_women_order: an Order object
        :return: a ShirtWomen object
        """
        factory = shirt_women_order.factory
        return factory.create_shirt_women(style=shirt_women_order.details['Style name'],
                                          size=shirt_women_order.details['Size'],
                                          colour=shirt_women_order.details['Colour'],
                                          textile=shirt_women_order.details['Textile'],
                                          sport=shirt_women_order.details['Sport'],
                                          pockets=shirt_women_order.details['Hidden Zipper Pockets'],
                                          ironing=shirt_women_order.details['Requires Ironing'],
                                          button=shirt_women_order.details['Buttons'],
                                          garment=shirt_women_order.details['Indoor/Outdoor'],
                                          )

    @staticmethod
    def socks_unisex_maker(socks_unisex_order: Order):
        """
        Creates a SocksUnisex object from the given order
        :param socks_unisex_order: an Order object
        :return: a SocksUnisex object
        """
        factory = socks_unisex_order.factory
        return factory.create_socks_unisex(style=socks_unisex_order.details['Style name'],
                                           size=socks_unisex_order.details['Size'],
                                           colour=socks_unisex_order.details['Colour'],
                                           textile=socks_unisex_order.details['Textile'],
                                           silver=socks_unisex_order.details['Silver'],
                                           stripe=socks_unisex_order.details['Stripe'],
                                           dry_cleaning=socks_unisex_order.details['Dry Cleaning'],
                                           articulated=socks_unisex_order.details['Articulated'],
                                           length=socks_unisex_order.details['Length'],
                                           )

    def operate_order(self, order_list: list):
        """
        Responsible for checking the order list and generating the respective items.
        It stores the items into respective lists.
        :param order_list: a list
        """
        for order in order_list:
            garment_type = order.details['Garment']
            if garment_type == 'ShirtMen':
                for i in range(order.details['Count']):
                    self.shirts_men.append(GarmentMaker.shirt_men_maker(order))
            elif garment_type == 'ShirtWomen':
                for i in range(order.details['Count']):
                    self.shirts_women.append(GarmentMaker.shirt_women_maker(order))
            elif garment_type == 'SockPairUnisex':
                for i in range(order.details['Count']):
                    self.sock_unisex.append(GarmentMaker.socks_unisex_maker(order))

    def main(self):
        """
        Drives the program
        """
        try:
            filename = input("Which excel file do you want to extract from? ")
            self.processor.open_order_sheet(f"./{filename}.xlsx")
        except FileNotFoundError:
            print("File was not found")
        else:
            order_list = []
            for next_order in self.processor.process_next_order():
                order_list.append(next_order)
            self.operate_order(order_list)
            self.create_report()

    @staticmethod
    def display_result(garment_list: list) -> None:
        """
        Prints out the list in the format of a report
        :param garment_list: a list
        """
        brand = ""
        for item in garment_list:
            if brand != item.__class__.__name__:
                print(f"-------- Order: {item.__class__.__name__} --------\n")
                brand = item.__class__.__name__
            print(f"{item}\n")
        print("\n")

    def create_report(self):
        """
        Creates a daily report of the product that was made
        :return:
        """
        print(f"OOP Designs Inc. Factory Report - {datetime.datetime.now():%d-%m-%Y %H:%M:%S}\n\n")
        GarmentMaker.display_result(self.shirts_men)
        GarmentMaker.display_result(self.shirts_women)
        GarmentMaker.display_result(self.sock_unisex)


if __name__ == '__main__':
    garment = GarmentMaker()
    garment.main()
