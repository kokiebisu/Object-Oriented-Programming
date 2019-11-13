import pandas as pd
import abc
import enum


class BrandEnum(enum.Enum):
    """
    This enum specifies the different distinct brand types.
    """
    LULULIME = 0,
    PINEAPPLEREPUBLIC = 1,
    NIKA = 2


class SizeEnum(enum.Enum):
    """
    This enum specifies the different distinct size types.
    """
    XS = 0,
    S = 1,
    M = 2,
    L = 3,
    XL = 4,
    XXL = 5


class GarmentPurposeEnum(enum.Enum):
    """
    This enum specifies the different distinct garment purpose types.
    """
    YOGA = 0,
    RUNNING = 1,
    INDOOR = 2,
    OUTDOOR = 3


class SockLengthEnum(enum.Enum):
    """
    This enum specifies the different distinct sock length types.
    """
    ANKLE = 0,
    CALF = 1,
    KNEE = 2

### Abstract Clothes ###


class ShirtMen(abc.ABC):
    """
    ShirtMen defines the interface for one of the products the
    abstract factory pettern is responsible to create.
    """

    def __init__(self, style: str, size: SizeEnum, colour: str, textile: str) -> None:
        self.style = style
        self.size = size  # S, M, L, XL, XXL
        self.colour = colour
        self.textile = textile


class ShirtWomen(abc.ABC):
    """
    ShirtWomen defines the interface for one of the products the
    abstract factory pettern is responsible to create.
    """

    def __init__(self, style: str, size: SizeEnum, colour: str, textile: str) -> None:
        self.style = style
        self.size = size  # XS, S, M, L, XL, XXL
        self.colour = colour
        self.textile = textile


class SockPairUnisex(abc.ABC):
    """
    SockPairUnisex defines the interface for one of the products the
    abstract factory pettern is responsible to create.
    """

    def __init__(self, style: str, size: SizeEnum, colour: str, textile: str) -> None:
        self.style = style
        self.size = size  # S, M, L
        self.colour = colour
        self.textile = textile

### Factory ###


class BrandFactory(abc.ABC):
    """
    The base factory class. All clothes expect this factory class to
    generate clothes. The CharacterFactory class defines an interface
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
        Creates a SockPairUnisezNika instance
        :return: a SockPairUnisex
        """
        return SockPairUnisexNika(**kwargs)

### Shirt Men ###


class ShirtMenLuluLime(ShirtMen):
    """
    ShirtMenLuluLime is a type of ShirtMen branded by LuluLime
    """

    def __init__(self, garment_designed_for: GarmentPurposeEnum, pockets: int, **kwargs) -> None:
        """
        Initializes the ShirtMenLuluLime instance
        """
        self.garment_designed_for = garment_designed_for  # yoga or running
        self.pockets = pockets
        super.__init__(**kwargs)


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic is a type of ShirtMen branded by PineappleRepublic
    """

    def __init__(self, ironing: bool, button: int, **kwargs) -> None:
        self.ironing = ironing
        self.button = button
        super.__init__(**kwargs)


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika is a type of ShirtMen branded by Nike
    """

    def __init__(self, garment: GarmentPurposeEnum, **kwargs) -> None:
        self.garment = garment  # indoor or outdoor sports
        super.__init__(**kwargs)

### Shirt Women ###


class ShirtWomenLuluLime(ShirtWomen):
    """
    ShirtWomenLuluLime is a type of ShirtWomen branded by Lululime
    """

    def __init__(self, garment: str, pockets: int, **kwargs) -> None:
        self.garment = garment  # yoga or running
        self.pockets = pockets
        super.__init__(**kwargs)


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic is a type of ShirtWomen branded by PineappleRepublic
    """

    def __init__(self, ironing: bool, button: int, **kwargs):
        self.ironing = ironing
        self.button = button
        super.__init__(**kwargs)


class ShirtWomenNika(ShirtWomen):
    """
    ShirtWomenNika is a type of ShirtWomen branded by Nika
    """

    def __init__(self, garment: GarmentPurposeEnum, **kwargs) -> None:
        self.garment = garment  # indoor or outdoor sports
        super.__init__(**kwargs)

### SockPairUnisex ###


class SockPairUnisexLuluLime(SockPairUnisex):
    """
    SockPairUnisexLuluLime is a type of SockPairUnisex branded by Lululime
    """

    def __init__(self, garment_contains_odour: bool, color_of_stripe: str, **kwargs) -> None:
        self.garment_contains_odour = garment_contains_odour
        self.color_of_stripe = color_of_stripe
        super.__init__(**kwargs)


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SockPairUnisexPineappleRepublic is a type of SockPairUnisex branded by PineappleRepublic
    """

    def __init__(self, require_dry_cleaning: bool, **kwargs) -> None:
        self.require_dry_cleaning = require_dry_cleaning
        super.__init__(**kwargs)


class SockPairUnisexNika(SockPairUnisex):
    """
    SockPairUnisexNika is a type of SockPairUnisex branded by Nika
    """

    def __init__(self, sock_is_articulated: bool, sock_length: SockLengthEnum, **kwargs) -> None:
        self.sock_is_articulated = sock_is_articulated
        self.sock_length = sock_length  # ankle, calf, knee
        super.__init__(**kwargs)


class ClothesPopulator:
    """
    Responsible for retrieving the right factory for the specified clothes
    """

    def __init__(self):
        self.brand_factory_mapper = {
            BrandEnum.LULULIME: LuluLimeFactory,
            BrandEnum.PINEAPPLEREPUBLIC: PineappleRepublicFactory,
            BrandEnum.NIKA: NikaFactory
        }

    def get_factory(self, brand_type: BrandEnum) -> BrandFactory:
        """
        :return: Factory object
        """
        factory_class = self.brand_factory_mapper.get(brand_type, None)
        return factory_class()


class OrderProcessor:
    """
    Responsible for processing the Excel spreadsheet. 
    It is instantiated by the GarmentMaker class.
    """

    def __init__(self) -> None:
        self.data = None
        self.populator = ClothesPopulator()
        self.brands = {
            "Lululime": BrandEnum.LULULIME,
            "PineappleRepublic": BrandEnum.PINEAPPLEREPUBLIC,
            "Nika": BrandEnum.NIKA
        }
        self.garments = {
            "ShirtMen": ShirtMen,
            "ShirtWomen": ShirtWomen,
            "SockPairUnisex": SockPairUnisex
        }
        self.item_list = []

    def open_order_sheet(self, file_name: str) -> None:
        """
        Reads the excel file from the given filepath and 
        extracts the orders from the spreadsheet, one row at a time
        """
        dataframe = pd.read_excel(file_name)
        self.data = dataframe

    def process_next_order(self) -> Order:
        """
        Responsible for identifying the correct factory to use for each order.
        It stores the order details and the associated factory in an object of type Order and returns it
        :return: an Order object
        """
        i = 0
        while i < 10:
            data = self.data.iloc[i]
            detail_dict = {}
            detail_dict['Date'] = data['Date']
            detail_dict['Order Number'] = data['Order Number']
            detail_dict['Brand'] = data['Brand']
            detail_dict['Garment'] = data['Garment']
            detail_dict['Count'] = data['Count']
            detail_dict['Style name'] = data['Style name']
            detail_dict['Size'] = data['Size']
            detail_dict['Colour'] = data['Colour']
            detail_dict['Textile'] = data['Textile']
            detail_dict['Sport'] = data['Sport']
            detail_dict['Hidden Zipper Pockets'] = data['Hidden Zipper Pockets']
            detail_dict['Dry Cleaning'] = data['Dry Cleaning']
            detail_dict['Indoor/Outdoor'] = data['Indoor/Outdoor']
            detail_dict['Requires Ironing'] = data['Requires Ironing']
            detail_dict['Buttons'] = data['Buttons']
            detail_dict['Articulated'] = data['Articulated']
            detail_dict['Length'] = data['Length']
            detail_dict['Silver'] = data['Silver']
            detail_dict['Stripe'] = data['Stripe']
            brand_factory = self.populator.get_factory(
                self.brands[detail_dict['Brand']])
            yield Order(factory=brand_factory, details=detail_dict)
            i += 1


class Order:
    """
    Class that holds the associated factory and the details of the order
    """

    def __init__(self, factory: BrandFactory, details: dict) -> None:
        self._factory = factory
        self._details = details

    def __str__(self):
        """
        A String representation of the object
        """
        print(f"Factory is {type(self._factory)}")


class GarmentMaker:
    """
    Drives the program
    """

    def __init__(self):
        self.processor = OrderProcessor()
        self.shirtmen_list = []
        self.shirtwomen_list = []
        self.sockunisex_list = []

    def main(self):
        """
        Drives the program
        """
        self.order.open_order_sheet("./COMP_3522_A4_orders.xlsx")
        order_list = []
        for next_order in order.process_next_order():
            garment = next_order._details['Garment']
            if (garment == 'ShirtMen'):
                self.shirtmen_list.append(next_order)
                print("added to shirtmen")
            elif (garment == 'ShirtWomen'):
                self.shirtwomen_list.append(next_order)
                print("added to shirtwomen")
            elif (garment == 'SockPairUnisex'):
                self.sockunisex_list.append(next_order)
                print("added to sockpairunisex")
            else:
                print("failed")

        # send everything at the end of each working day

        # prompt user for name of file

        # receive order object from orderprocessor
        # invoce either three make object

        # produce a report summarizing the day's work
        # brand
        # garment produced


if __name__ == '__main__':
    garment = GarmentMaker()
    garment.main()
