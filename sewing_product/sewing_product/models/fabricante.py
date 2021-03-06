# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    codigo_alternativo_1 = fields.Many2one('product.template', 'Product')
    #codigo_alternativo_1 = fields.Char(string="Código alternativo 1:", required=False, )
    codigo_alternativo_2 = fields.Many2one('product.template', 'Product')

    fabricante = fields.Selection(string="Fabricante de máquina:", selection=[
                                                   ('dka', 'DURKOP Adler'),
                                                   ('af', 'Alfa'),
                                                   ('altin', 'ALTIN'),
                                                   ('ANKPH', 'Anker-Phoenix'),
                                                   ('ATTFOR', 'Attilio Forte'),
                                                   ('baoma', 'BAOMA'),
                                                   ('BRTTO', 'Baratto'),
                                                   ('BRDAN', 'Barudan'),
                                                   ('beaver', 'BEAVER'),
                                                   ('bernina', 'BERNINA'),
                                                   ('bonis', 'BONIS'),
                                                   ('bro', 'Brother'),
                                                   ('bc', 'Blindstitch -- Columbia'),
                                                   ('bm', 'Blindstitch -- Miscellaneous'),
                                                   ('USBLD', 'Blindstitch -- U.S.'),
                                                   ('bha', 'Brother Home Appliances'),
                                                   ('cra', 'CRA'),
                                                   ('chandler', 'CHANDLER'),
                                                   ('ciucani', 'CIUCANI'),
                                                   ('clinton', 'CLINTON'),
                                                   ('colli', 'COLLI'),
                                                   ('compo', 'COMPO'),
                                                   ('consew', 'CONSEW'),
                                                   ('CRNLY', 'Cornelly'),
                                                   ('dexter', 'DEXTER'),
                                                   ('diamant', 'DIAMANT FR'),
                                                   ('durkopp', 'DURKOPP'),
                                                   ('eastman', 'Eastman'),
                                                   ('eldridge', 'Eldridge'),
                                                   ('eltac', 'ELTAC'),
                                                   ('excalibur', 'Excalibur'),
                                                   ('fischbein', 'Fischbein'),
                                                   ('fomax', 'FOMAX'),
                                                   ('fortuna', 'FORTUNA'),
                                                   ('free', 'Free & New Home'),
                                                   ('global', 'GLOBAL'),
                                                   ('gross', 'Gross-Marco'),
                                                   ('gury', 'GURY'),
                                                   ('garudan', 'Garudan'),
                                                   ('gemsy', 'GEMSY'),
                                                   ('happy', 'Happy'),
                                                   ('hashima', 'Hashima'),
                                                   ('highlead', 'HighLead'),
                                                   ('hoog', 'HOOG'),
                                                   ('ideal', 'IDEAL'),
                                                   ('ivomaq', 'IVOMAQ'),
                                                   ('janome', 'Janome'),
                                                   ('juki', 'JUKI'),
                                                   ('kansai', 'KANSAI'),
                                                   ('kingtex', 'Kingtex'),
                                                   ('km machines', 'KM Machines'),
                                                   ('landis', 'LANDIS'),
                                                   ('lewis', 'LEWIS'),
                                                   ('maier', 'MAIER'),
                                                   ('maimin', 'MAIMIN'),
                                                   ('man-sew', 'Man-Sew'),
                                                   ('mauser', 'MAUSER'),
                                                   ('meca', 'MECA'),
                                                   ('meistergram', 'Meistergram'),
                                                   ('melco', 'MELCO'),
                                                   ('merrow', 'MERROW'),
                                                   ('metropolitan', 'Metropolitan'),
                                                   ('mitsubishi', 'Mitsubishi'),
                                                   ('machine meto', 'Machine Meto'),
                                                   ('nakajima', 'Nakajima'),
                                                   ('nechi', 'NECHI'),
                                                   ('newlong', 'NEWLONG'),
                                                   ('omac', 'OMAC'),
                                                   ('peerless', 'Peerless'),
                                                   ('pegasus', 'Pegasus'),
                                                   ('pfaff', 'PFAFF'),
                                                   ('porter', 'PORTER'),
                                                   ('reece', 'REECE'),
                                                   ('refrey', 'REFREY'),
                                                   ('renown', 'RENOWN'),
                                                   ('rimold', 'Rimold'),
                                                   ('rotozip', 'ROTO ZIP'),
                                                   ('resta', 'RESTA'),
                                                   ('seiko', 'SEIKO'),
                                                   ('singer', 'SINGER'),
                                                   ('siruba', 'SIRUBA'),
                                                   ('sotco', 'SOTCO'),
                                                   ('stager', 'STAGER'),
                                                   ('sunstar', 'SUNSTAR'),
                                                   ('sprena', 'SUPRENA'),
                                                   ('taiko', 'TAIKO'),
                                                   ('tajma', 'TAJMA'),
                                                   ('titan', 'TITAN'),
                                                   ('toyota', 'TOYOTA'),
                                                   ('treauser', 'TREASURE'),
                                                   ('typical', 'Typical'),
                                                   ('unicorn', 'UNICORN'),
                                                   ('union special', 'Union Special'),
                                                   ('united shoe machine', 'United Shoe Machine'),
                                                   ('vibemac', 'Vibemac'),
                                                   ('white & franklin', 'White & Franklin'),
                                                   ('willcox & gibbs', 'Willcox & Gibbs'),
                                                   ('wolf', 'WOLF'),
                                                   ('yakumo', 'YAKUMO'),
                                                   ('yamato', 'YAMATO'),
                                                   ('yulun', 'YULUN'),
                                                   ('w&w', 'W&W'),
                                                   ], required=False, )

    marca_sw = fields.Selection(string="Marca:", selection=[('3m', '3M'),
                                                            ('a.s.s', 'A.S.S.'),
                                                            ('able', 'Able'),
                                                            ('ace', 'Ace'),
                                                            ('ace-hi', 'Ace-Hi'),
                                                            ('acme', 'Acme'),
                                                            ('albatross', 'Albatross'),
                                                            ('alex needlelights', 'Alex Needlelights'),
                                                            ('allen', 'Allen'),
                                                            ('american beauty', 'American Beauty'),
                                                            ('arrow', 'Arrow'),
                                                            ('barudan', 'BARUDAN'),
                                                            ('bostitch', 'BOSTITCH'),
                                                            ('buffalo', 'BUFFALO'),
                                                            ('bates', 'Bates'),
                                                            ('beka', 'Beka'),
                                                            ('black & decker', 'Black & Decker'),
                                                            ('bosch', 'Bosch'),
                                                            ('brother', 'Brother'),
                                                            ('brother home appliances', 'Brother Home Appliances'),
                                                            ('bussmann', 'Bussmann'),
                                                            ('c-thru', 'C-Thru'),
                                                            ('c.s. osbourne', 'C.S. Osbourne'),
                                                            ('camie', 'Camie'),
                                                            ('carousell', 'Carousell'),
                                                            ('cerliani', 'Cerliani'),
                                                            ('chefs choice', 'Chefs Choice'),
                                                            ('claire', 'Claire'),
                                                            ('clarke', 'Clarke'),
                                                            ('clauss', 'Clauss'),
                                                            ('clinton', 'Clinton'),
                                                            ('clover needlecraft', 'Clover Needlecraft'),
                                                            ('cooperTools -- crescent', 'CooperTools -- Crescent'),
                                                            ('coopertools -- lufkin', 'CooperTools -- Lufkin'),
                                                            ('cooperTools -- nicholson', 'CooperTools -- Nicholson'),
                                                            ('cooperTools -- plumb', 'CooperTools -- Plumb'),
                                                            ('cooperTools -- weller', 'CooperTools -- Weller'),
                                                            ('cooperTools -- wiss', 'CooperTools -- Wiss'),
                                                            ('divbrn', 'DIVBRN'),
                                                            ('dutton', 'DUTTON'),
                                                            ('dyno', 'DYNO'),
                                                            ('daiko', 'Daiko'),
                                                            ('dennison', 'Dennison'),
                                                            ('dexter', 'Dexter'),
                                                            ('dixon', 'Dixon'),
                                                            ('dragonfly', 'Dragonfly'),
                                                            ('dremel', 'Dremel'),
                                                            ('durkopp adler', 'Durkopp Adler'),
                                                            ('e-z motor', 'E-Z Motor'),
                                                            ('e.c. mitchell', 'E.C. Mitchell'),
                                                            ('enduro motors & parts', 'ENDURO MOTORS & PARTS'),
                                                            ('eagle electric', 'Eagle Electric'),
                                                            ('eastman', 'Eastman'),
                                                            ('electro-rail', 'Electro-Rail'),
                                                            ('engel', 'Engel'),
                                                            ('fischbein', 'FISCHBEIN'),
                                                            ('fairgate', 'Fairgate'),
                                                            ('feedrail', 'Feedrail'),
                                                            ('fiskars', 'Fiskars'),
                                                            ('fostoria', 'Fostoria'),
                                                            ('gearwrench', 'GEARWRENCH'),
                                                            ('goldstar', 'GOLDSTAR'),
                                                            ('gury', 'GURY'),
                                                            ('gatesGeneral electric', 'GatesGeneral Electric'),
                                                            ('general tools', 'General Tools'),
                                                            ('gingher', 'Gingher'),
                                                            ('global parts', 'Global Parts'),
                                                            ('gold seal', 'Gold Seal'),
                                                            ('groz-beckert', 'Groz-Beckert'),
                                                            ('harris', 'HARRIS'),
                                                            ('heritage', 'HERITAGE'),
                                                            ('ho hsing', 'HO HSING'),
                                                            ('hot steam', 'HOT STEAM'),
                                                            ('happy', 'Happy'),
                                                            ('hashima', 'Hashima'),
                                                            ('highlead', 'Highlead'),
                                                            ('hirose', 'Hirose'),
                                                            ('hyde', 'Hyde'),
                                                            ('jacobson', 'Jacobson'),
                                                            ('jukikm', 'JukiKM'),
                                                            ('kai', 'Kai'),
                                                            ('kansai', 'Kansai'),
                                                            ('kingtex', 'Kingtex'),
                                                            ('krebs', 'Krebs'),
                                                            ('lance', 'LANCE'),
                                                            ('lion', 'LION'),
                                                            ('laserlyte', 'Laserlyte'),
                                                            ('maier', 'Maier'),
                                                            ('maimin', 'Maimin'),
                                                            ('marks/mundial', 'Marks/Mundial'),
                                                            ('melco', 'Melco'),
                                                            ('merrow', 'Merrow'),
                                                            ('meto', 'Meto'),
                                                            ('mitsubishi', 'Mitsubishi'),
                                                            ('net pins', 'NET PINS'),
                                                            ('nippo', 'Nippo'),
                                                            ('nissin', 'Nissin'),
                                                            ('norton', 'Norton'),
                                                            ('olfa', 'Olfa'),
                                                            ('open data', 'Open Data'),
                                                            ('orange', 'Orange'),
                                                            ('pacific steam', 'PACIFIC STEAM'),
                                                            ('plastikote', 'PLASTIKOTE'),
                                                            ('pegasus', 'Pegasus'),
                                                            ('pfaff', 'Pfaff'),
                                                            ('physicians care', 'Physicians Care'),
                                                            ('porter', 'Porter'),
                                                            ('prym ditz', 'Prym Ditz'),
                                                            ('queen light', 'QUEEN LIGHT'),
                                                            ('recoil air hoses', 'RECOIL AIR HOSES'),
                                                            ('racing', 'Racing'),
                                                            ('reece', 'Reece'),
                                                            ('rel-sew', 'Rel-Sew'),
                                                            ('rimoldi', 'Rimoldi'),
                                                            ('roto zip', 'Roto Zip'),
                                                            ('silverstar', 'SILVERSTAR'),
                                                            ('skil', 'SKIL'),
                                                            ('snf', 'SNF'),
                                                            ('soabar', 'SOABAR'),
                                                            ('starline', 'STARLINE'),
                                                            ('supreme', 'SUPREME'),
                                                            ('sabre tagging guns', 'Sabre Tagging Guns'),
                                                            ('sabun', 'Sabun'),
                                                            ('sapporo', 'Sapporo'),
                                                            ('segye', 'Segye'),
                                                            ('seiko', 'Seiko'),
                                                            ('shurtape', 'Shurtape'),
                                                            ('singer', 'Singer'),
                                                            ('siruba', 'Siruba'),
                                                            ('sprayway', 'Sprayway'),
                                                            ('strobel', 'Strobel'),
                                                            ('sunstar', 'Sunstar'),
                                                            ('superior', 'Superior'),
                                                            ('tajuma', 'TAJIMA'),
                                                            ('templex', 'Templex'),
                                                            ('towa', 'Towa'),
                                                            ('trippleware / PMC', 'Trippleware / PMC'),
                                                            ('utica', 'UTICA'),
                                                            ('union special', 'Union Special'),
                                                            ('vibemac', 'VIBEMAC'),
                                                            ('weiler', 'WEILER'),
                                                            ('westcott', 'WESTCOTT'),
                                                            ('whiting & davis', 'Whiting & Davis'),
                                                            ('wilson', 'Wilson'),
                                                            ('wolf', 'Wolf'),
                                                            ('wolff', 'Wolff'),
                                                            ('xcelite', 'XCELITE'),
                                                            ('yamato', 'Yamato'),
                                                            ('z-laser', 'Z-Laser'),
                                                            ('zero max', 'Zero Max'),
                                                            ], required=False, )







