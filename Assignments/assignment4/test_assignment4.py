from unittest.mock import patch
from unittest import TestCase
from assignment4 import GarmentMaker, BrandEnum, LuluLimeFactory

class TestGarmentFactory(TestCase):
    # @patch('garment_abstract_factory.get_file_input',
    #        return_value='invalidfile')
    def test_wrong_file_input(self):
        self.garment = GarmentMaker()
        with self.assertRaises(FileNotFoundError):
            self.garment.processor.open_order_sheet("./a5.xlsx")
    # def test_item_generator_lululime(self):
    #     self.item_generator = garment_abstract_factory.ItemGenerator()
    #     lululime_factory = self.item_generator.retrieve_factory(BrandEnum.LULULIME)
    #     self.assertTrue(isinstance(lululime_factory, LuluLimeFactory))
    # def test_item_generator_pineapple_republic(self):
    #     self.item_generator = garment_abstract_factory.ItemGenerator()
    #     factory = self.item_generator.retrieve_factory(
    #         garment_abstract_factory.ItemBrandEnum.PINEAPPLEREPUBLIC)
    #     self.assertTrue(isinstance(factory, garment_abstract_factory
    #                                .PineappleRepublicFactory))
    # def test_item_generator_nika(self):
    #     self.item_generator = garment_abstract_factory.ItemGenerator()
    #     factory = self.item_generator.retrieve_factory(garment_abstract_factory
    #                                                    .ItemBrandEnum.NIKA)
    #     self.assertTrue(isinstance(factory, garment_abstract_factory
    #                                .NikaFactory))

    def test_correct_processing(self):
        self.garment = GarmentMaker()
        self.garment.processor.open_order_sheet(f"../a4.xlsx")
        self.read_data = self.garment.processor.data.iloc[0]
        order_info = {'Date': self.read_data['Date'],
                      'Order Number': self.read_data['Order Number'],
                      'Brand': self.read_data['Brand'],
                      'Garment': self.read_data['Garment'],
                      'Count': self.read_data['Count'],
                      'Style name': self.read_data['Style name'],
                      'Size': self.read_data['Size'],
                      'Colour': self.read_data['Colour'],
                      'Textile': self.read_data['Textile'],
                      'Sport': self.read_data['Sport'],
                      'Hidden Zipper Pockets': self.read_data[
                          'Hidden Zipper Pockets']}
        expected_info = {'Date': 'Friday November 16 2019',
                         'Order Number': 1,
                         'Brand': 'Lululime',
                         'Garment': 'ShirtMen',
                         'Count': 300,
                         'Style name': 'Bowen',
                         'Size': 'M',
                         'Colour': 'Grey',
                         'Textile': 'Merino wool',
                         'Sport': 'Yoga',
                         'Hidden Zipper Pockets': 1}
        self.assertEqual(order_info, expected_info)
