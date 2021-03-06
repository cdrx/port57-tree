
def strip(c):
    l = ["very ", "light ", "luminous ", "vivid ", "dark ", "deep ", "pale ", "deep ", "medium ", "strong ", "paleish ", "moderate ", "brilliant ", "luminous", ]
    for x in l:
        c = c.lower().replace(x, "")
    return c

# from colours import strip, FLAT_COLOURS, COLOURS
# from colour.models import Colour
#
# for n, r, g, b in FLAT_COLOURS:
#     try:
#         from colour.models import Colour
#         Colour.objects.get(name=strip(n).lower().strip())
#     except Colour.DoesNotExist:
#        Colour.objects.create(name=strip(n).lower().strip(), r=r, g=g, b=b)
#
# for r, g, b, n in COLOURS:
#     try:
#         from colour.models import Colour
#         Colour.objects.get(name=strip(n).lower().strip())
#     except Colour.DoesNotExist:
#        Colour.objects.create(name=strip(n).lower().strip(), r=r, g=g, b=b)

FLAT_COLOURS = [
    ("maroon", 0x80,  0x00,  0x00),
    ("green", 0x00,  0x80,  0x00),
    ("olive", 0x80,  0x80,  0x00),
    ("navy", 0x00,  0x00,  0x80),
    ("purple", 0x80,  0x00,  0x80),
    ("teal", 0x00,  0x80,  0x80),
    ("gray", 0x80,  0x80,  0x80),
    ("silver", 0xC0,  0xC0,  0xC0),
    ("red", 0xFF,  0x00,  0x00),
    ("lime", 0x00,  0xFF,  0x00),
    ("yellow", 0xFF,  0xFF,  0x00),
    ("blue", 0x00,  0x00,  0xFF),
    ("fuchsia", 0xFF,  0x00,  0xFF),
    ("aqua", 0x00,  0xFF,  0xFF),
    ("white", 0xFF,  0xFF,  0xFF),
    ("alice blue", 0xF0,  0xF8,  0xFF),
    ("antique white", 0xFA,  0xEB,  0xD7),
    ("aquamarine", 0x7F,  0xFF,  0xD4),
    ("azure", 0xF0,  0xFF,  0xFF),
    ("beige", 0xF5,  0xF5,  0xDC),
    ("blue violet", 0x8A,  0x2B,  0xE2),
    ("brown", 0xA5,  0x2A,  0x2A),
    ("burlywood", 0xDE,  0xB8,  0x87),
    ("cadet blue", 0x5F,  0x9E,  0xA0),
    ("chartreuse", 0x7F,  0xFF,  0x00),
    ("chocolate", 0xD2,  0x69,  0x1E),
    ("coral", 0xFF,  0x7F,  0x50),
    ("cornflower blue", 0x64,  0x95,  0xED),
    ("cornsilk", 0xFF,  0xF8,  0xDC),
    ("crimson", 0xDC,  0x14,  0x3C),
    ("dark blue", 0x00,  0x00,  0x8B),
    ("dark cyan", 0x00,  0x8B,  0x8B),
    ("dark golden rod", 0xB8,  0x86,  0x0B),
    ("dark gray", 0xA9,  0xA9,  0xA9),
    ("dark green", 0x00,  0x64,  0x00),
    ("dark khaki", 0xBD,  0xB7,  0x6B),
    ("dark magenta", 0x8B,  0x00,  0x8B),
    ("dark olive green", 0x55,  0x6B,  0x2F),
    ("dark orange", 0xFF,  0x8C,  0x00),
    ("dark orchid", 0x99,  0x32,  0xCC),
    ("dark red", 0x8B,  0x00,  0x00),
    ("dark salmon", 0xE9,  0x96,  0x7A),
    ("dark sea green", 0x8F,  0xBC,  0x8F),
    ("dark slate blue", 0x48,  0x3D,  0x8B),
    ("dark slategray", 0x2F,  0x4F,  0x4F),
    ("dark turquoise", 0x00,  0xCE,  0xD1),
    ("dark violet", 0x94,  0x00,  0xD3),
    ("deep pink", 0xFF,  0x14,  0x93),
    ("deep sky blue", 0x00,  0xBF,  0xFF),
    ("dim gray", 0x69,  0x69,  0x69),
    ("dodger blue", 0x1E,  0x90,  0xFF),
    ("firebrick", 0xB2,  0x22,  0x22),
    ("floral white", 0xFF,  0xFA,  0xF0),
    ("forest green", 0x22,  0x8B,  0x22),
    ("gainsboro", 0xDC,  0xDC,  0xDC),
    ("ghost white", 0xF8,  0xF8,  0xFF),
    ("gold", 0xFF,  0xD7,  0x00),
    ("golden rod", 0xDA,  0xA5,  0x20),
    ("green yellow", 0xAD,  0xFF,  0x2F),
    ("honeydew", 0xF0,  0xFF,  0xF0),
    ("hot pink", 0xFF,  0x69,  0xB4),
    ("indian red", 0xCD,  0x5C,  0x5C),
    ("indigo", 0x4B,  0x00,  0x82),
    ("ivory", 0xFF,  0xFF,  0xF0),
    ("khaki", 0xF0,  0xE6,  0x8C),
    ("lavender", 0xE6,  0xE6,  0xFA),
    ("lavender blush", 0xFF,  0xF0,  0xF5),
    ("lawn green", 0x7C,  0xFC,  0x00),
    ("lemon chiffon", 0xFF,  0xFA,  0xCD),
    ("light blue", 0xAD,  0xD8,  0xE6),
    ("light coral", 0xF0,  0x80,  0x80),
    ("light cyan", 0xE0,  0xFF,  0xFF),
    ("light golden rod yellow", 0xFA,  0xFA,  0xD2),
    ("light green", 0x90,  0xEE,  0x90),
    ("light grey", 0xD3,  0xD3,  0xD3),
    ("light pink", 0xFF,  0xB6,  0xC1),
    ("light salmon", 0xFF,  0xA0,  0x7A),
    ("light sea green", 0x20,  0xB2,  0xAA),
    ("light sky blue", 0x87,  0xCE,  0xFA),
    ("light slate gray", 0x77,  0x88,  0x99),
    ("light steel blue", 0xB0,  0xC4,  0xDE),
    ("light yellow", 0xFF,  0xFF,  0xE0),
    ("limegreen", 0x32,  0xCD,  0x32),
    ("linen", 0xFA,  0xF0,  0xE6),
    ("medium aquamarine", 0x66,  0xCD,  0xAA),
    ("medium blue", 0x00,  0x00,  0xCD),
    ("medium orchid", 0xBA,  0x55,  0xD3),
    ("medium purple", 0x93,  0x70,  0xD0),
    ("medium seagreen", 0x3C,  0xB3,  0x71),
    ("medium slateblue", 0x7B,  0x68,  0xEE),
    ("medium springgreen", 0x00,  0xFA,  0x9A),
    ("medium turquoise", 0x48,  0xD1,  0xCC),
    ("medium violet red", 0xC7,  0x15,  0x85),
    ("midnight blue", 0x19,  0x19,  0x70),
    ("mintc ream", 0xF5,  0xFF,  0xFA),
    ("misty rose", 0xFF,  0xE4,  0xE1),
    ("moccasin", 0xFF,  0xE4,  0xB5),
    ("navajo white", 0xFF,  0xDE,  0xAD),
    ("oldlace", 0xFD,  0xF5,  0xE6),
    ("olive drab", 0x6B,  0x8E,  0x23),
    ("orange", 0xFF,  0xA5,  0x00),
    ("orangered", 0xFF,  0x45,  0x00),
    ("orchid", 0xDA,  0x70,  0xD6),
    ("pale golde nrod", 0xEE,  0xE8,  0xAA),
    ("pale green", 0x98,  0xFB,  0x98),
    ("pale turquoise", 0xAF,  0xEE,  0xEE),
    ("pale violet red", 0xDB,  0x70,  0x93),
    ("papayawhip", 0xFF,  0xEF,  0xD5),
    ("peach puff", 0xFF,  0xDA,  0xB9),
    ("peru", 0xCD,  0x85,  0x3F),
    ("pink", 0xFF,  0xC0,  0xCB),
    ("plum", 0xDD,  0xA0,  0xDD),
    ("powder blue", 0xB0,  0xE0,  0xE6),
    ("rosy brown", 0xBC,  0x8F,  0x8F),
    ("royal blue", 0x41,  0x69,  0xE1),
    ("saddle brown", 0x8B,  0x45,  0x13),
    ("salmon", 0xFA,  0x80,  0x72),
    ("sandy brown", 0xF4,  0xA4,  0x60),
    ("sea green", 0x2E,  0x8B,  0x57),
    ("seashell", 0xFF,  0xF5,  0xEE),
    ("sienna", 0xA0,  0x52,  0x2D),
    ("sky blue", 0x87,  0xCE,  0xEB),
    ("slate blue", 0x6A,  0x5A,  0xCD),
    ("slate gray", 0x70,  0x80,  0x90),
    ("snow", 0xFF,  0xFA,  0xFA),
    ("springgreen", 0x00,  0xFF,  0x7F),
    ("steel blue", 0x46,  0x82,  0xB4),
    ("tan", 0xD2,  0xB4,  0x8C),
    ("thistle", 0xD8,  0xBF,  0xD8),
    ("tomato", 0xFF,  0x63,  0x47),
    ("turquoise", 0x40,  0xE0,  0xD0),
    ("violet", 0xEE,  0x82,  0xEE),
    ("wheat", 0xF5,  0xDE,  0xB3),
    ("whitesmoke", 0xF5,  0xF5,  0xF5),
]

COLOURS = [
    ['255', '246', '246', 'Pinkish white'],
    ['255', '226', '226', 'Very pale pink'],
    ['255', '194', '194', 'Pale pink'],
    ['255', '158', '158', 'Light pink'],
    ['255', '101', '101', 'Light brilliant red'],
    ['255', '0', '0', 'Luminous vivid red'],
    ['231', '218', '218', 'Pinkish gray'],
    ['231', '184', '184', 'Pale, grayish pink'],
    ['231', '139', '139', 'Pink'],
    ['231', '81', '81', 'Brilliant red'],
    ['231', '0', '0', 'Vivid red'],
    ['168', '156', '156', 'Reddish gray'],
    ['168', '125', '125', 'Grayish red'],
    ['168', '74', '74', 'Moderate red'],
    ['168', '0', '0', 'Strong red'],
    ['89', '83', '83', 'Reddish brownish gray'],
    ['89', '66', '66', 'Dark grayish reddish brown'],
    ['89', '39', '39', 'Reddish brown'],
    ['89', '0', '0', 'Deep reddish brown'],
    ['29', '26', '26', 'Reddish brownish black'],
    ['29', '17', '17', 'Very reddish brown'],
    ['29', '0', '0', 'Very deep reddish brown'],
    ['255', '201', '194', 'Pale scarlet'],
    ['255', '170', '158', 'Very light scarlet'],
    ['255', '120', '101', 'Light brilliant scarlet'],
    ['255', '32', '0', 'Luminous vivid scarlet'],
    ['231', '150', '139', 'Light scarlet'],
    ['231', '100', '81', 'Brilliant scarlet'],
    ['231', '29', '0', 'Vivid scarlet'],
    ['168', '85', '74', 'Moderate scarlet'],
    ['168', '21', '0', 'Strong scarlet'],
    ['89', '45', '39', 'Dark scarlet'],
    ['89', '11', '0', 'Deep scarlet'],
    ['255', '233', '226', 'Very pale vermilion'],
    ['255', '209', '194', 'Pale vermilion'],
    ['255', '182', '158', 'Very light vermilion'],
    ['255', '139', '101', 'Light brilliant vermilion'],
    ['255', '64', '0', 'Luminous vivid vermilion'],
    ['231', '196', '184', 'Pale, light grayish vermilion'],
    ['231', '162', '139', 'Light vermilion'],
    ['231', '119', '81', 'Brilliant vermilion'],
    ['231', '58', '0', 'Vivid vermilion'],
    ['168', '136', '125', 'Grayish vermilion'],
    ['168', '97', '74', 'Moderate vermilion'],
    ['168', '42', '0', 'Strong vermilion'],
    ['89', '72', '66', 'Dark grayish vermilion'],
    ['89', '52', '39', 'Dark vermilion'],
    ['89', '22', '0', 'Deep vermilion'],
    ['255', '217', '194', 'Pale tangelo'],
    ['255', '194', '158', 'Very light tangelo'],
    ['255', '159', '101', 'Light brilliant tangelo'],
    ['255', '96', '0', 'Luminous vivid tangelo'],
    ['231', '174', '139', 'Light tangelo'],
    ['231', '137', '81', 'Brilliant tangelo'],
    ['231', '87', '0', 'Vivid tangelo'],
    ['168', '109', '74', 'Moderate tangelo'],
    ['168', '63', '0', 'Strong tangelo'],
    ['89', '58', '39', 'Dark tangelo'],
    ['89', '33', '0', 'Deep tangelo'],
    ['255', '240', '226', 'Very pale orange'],
    ['255', '224', '194', 'Pale orange'],
    ['255', '207', '158', 'Very light orange'],
    ['255', '178', '101', 'Light brilliant orange'],
    ['255', '128', '0', 'Luminous vivid orange'],
    ['231', '208', '184', 'Pale, light grayish brown'],
    ['231', '185', '139', 'Light orange'],
    ['231', '156', '81', 'Brilliant orange'],
    ['231', '116', '0', 'Vivid orange'],
    ['168', '147', '125', 'Grayish brown'],
    ['168', '121', '74', 'Moderate orange'],
    ['168', '84', '0', 'Strong orange'],
    ['89', '78', '66', 'Dark grayish brown'],
    ['89', '64', '39', 'Brown'],
    ['89', '45', '0', 'Deep brown'],
    ['29', '23', '17', 'Very brown'],
    ['29', '14', '0', 'Very deep brown'],
    ['255', '232', '194', 'Pale gamboge'],
    ['255', '219', '158', 'Very light gamboge'],
    ['255', '197', '101', 'Light brilliant gamboge'],
    ['255', '159', '0', 'Luminous vivid gamboge'],
    ['231', '197', '139', 'Light gamboge'],
    ['231', '175', '81', 'Brilliant gamboge'],
    ['231', '145', '0', 'Vivid gamboge'],
    ['168', '133', '74', 'Moderate gamboge'],
    ['168', '105', '0', 'Strong gamboge'],
    ['89', '70', '39', 'Dark gamboge'],
    ['89', '56', '0', 'Deep gamboge'],
    ['255', '248', '226', 'Very pale amber'],
    ['255', '240', '194', 'Pale amber'],
    ['255', '231', '158', 'Very light amber'],
    ['255', '216', '101', 'Light brilliant amber'],
    ['255', '191', '0', 'Luminous vivid amber'],
    ['231', '220', '184', 'Pale, light grayish amber'],
    ['231', '208', '139', 'Light amber'],
    ['231', '194', '81', 'Brilliant amber'],
    ['231', '174', '0', 'Vivid amber'],
    ['168', '158', '125', 'Grayish amber'],
    ['168', '145', '74', 'Moderate amber'],
    ['168', '126', '0', 'Strong amber'],
    ['89', '84', '66', 'Dark grayish amber'],
    ['89', '77', '39', 'Dark amber'],
    ['89', '67', '0', 'Deep amber'],
    ['255', '247', '194', 'Pale gold'],
    ['255', '243', '158', 'Very light gold'],
    ['255', '236', '101', 'Light brilliant gold'],
    ['255', '223', '0', 'Luminous vivid gold'],
    ['231', '220', '139', 'Light gold'],
    ['231', '213', '81', 'Brilliant gold'],
    ['231', '202', '0', 'Vivid gold'],
    ['168', '156', '74', 'Moderate gold'],
    ['168', '147', '0', 'Strong gold'],
    ['89', '83', '39', 'Dark gold'],
    ['89', '78', '0', 'Deep gold'],
    ['255', '255', '246', 'Yellowish white'],
    ['255', '255', '226', 'Very pale yellow'],
    ['255', '255', '194', 'Pale yellow'],
    ['255', '255', '158', 'Very light yellow'],
    ['255', '255', '101', 'Light brilliant yellow'],
    ['255', '255', '0', 'Luminous vivid yellow'],
    ['231', '231', '218', 'Light yellowish gray'],
    ['231', '231', '184', 'Pale, light grayish olive'],
    ['231', '231', '139', 'Light yellow'],
    ['231', '231', '81', 'Brilliant yellow'],
    ['231', '231', '0', 'Vivid yellow'],
    ['168', '168', '156', 'Yellowish gray'],
    ['168', '168', '125', 'Grayish olive'],
    ['168', '168', '74', 'Moderate olive'],
    ['168', '168', '0', 'Strong olive'],
    ['89', '89', '83', 'Dark olivish gray'],
    ['89', '89', '66', 'Dark grayish olive'],
    ['89', '89', '39', 'Dark olive'],
    ['89', '89', '0', 'Deep olive'],
    ['29', '29', '26', 'Yellowish black'],
    ['29', '29', '17', 'Very dark olive'],
    ['29', '29', '0', 'Very deep olive'],
    ['247', '255', '194', 'Pale apple green'],
    ['243', '255', '158', 'Very light apple green'],
    ['236', '255', '101', 'Light brilliant apple green'],
    ['223', '255', '0', 'Luminous vivid apple green'],
    ['220', '231', '139', 'Light apple green'],
    ['213', '231', '81', 'Brilliant apple green'],
    ['202', '231', '0', 'Vivid apple green'],
    ['156', '168', '74', 'Moderate apple green'],
    ['147', '168', '0', 'Strong apple green'],
    ['83', '89', '39', 'Dark apple green'],
    ['78', '89', '0', 'Deep apple green'],
    ['248', '255', '226', 'Very pale lime green'],
    ['240', '255', '194', 'Pale lime green'],
    ['231', '255', '158', 'Very light lime green'],
    ['216', '255', '101', 'Light brilliant lime green'],
    ['191', '255', '0', 'Luminous vivid lime green'],
    ['220', '231', '184', 'Pale, light grayish lime green'],
    ['208', '231', '139', 'Light lime green'],
    ['194', '231', '81', 'Brilliant lime green'],
    ['174', '231', '0', 'Vivid lime green'],
    ['158', '168', '125', 'Grayish lime green'],
    ['145', '168', '74', 'Moderate lime green'],
    ['126', '168', '0', 'Strong lime green'],
    ['84', '89', '66', 'Dark grayish lime green'],
    ['77', '89', '39', 'Dark lime green'],
    ['67', '89', '0', 'Deep lime green'],
    ['232', '255', '194', 'Pale spring bud'],
    ['219', '255', '158', 'Very light spring bud'],
    ['197', '255', '101', 'Light brilliant spring bud'],
    ['159', '255', '0', 'Luminous vivid spring bud'],
    ['197', '231', '139', 'Light spring bud'],
    ['175', '231', '81', 'Brilliant spring bud'],
    ['145', '231', '0', 'Vivid spring bud'],
    ['133', '168', '74', 'Moderate spring bud'],
    ['105', '168', '0', 'Strong spring bud'],
    ['70', '89', '39', 'Dark spring bud'],
    ['56', '89', '0', 'Deep spring bud'],
    ['240', '255', '226', 'Very pale chartreuse green'],
    ['224', '255', '194', 'Pale chartreuse green'],
    ['207', '255', '158', 'Very light chartreuse green'],
    ['178', '255', '101', 'Light brilliant chartreuse green'],
    ['128', '255', '0', 'Luminous vivid chartreuse green'],
    ['208', '231', '184', 'Pale, light grayish chartreuse green'],
    ['185', '231', '139', 'Light chartreuse green'],
    ['156', '231', '81', 'Brilliant chartreuse green'],
    ['116', '231', '0', 'Vivid chartreuse green'],
    ['147', '168', '125', 'Grayish chartreuse green'],
    ['121', '168', '74', 'Moderate chartreuse green'],
    ['84', '168', '0', 'Strong chartreuse green'],
    ['78', '89', '66', 'Dark grayish chartreuse green'],
    ['64', '89', '39', 'Dark chartreuse green'],
    ['45', '89', '0', 'Deep chartreuse green'],
    ['23', '29', '17', 'Very dark chartreuse green'],
    ['14', '29', '0', 'Very deep chartreuse green'],
    ['217', '255', '194', 'Pale pistachio'],
    ['194', '255', '158', 'Very light pistachio'],
    ['159', '255', '101', 'Light brilliant pistachio'],
    ['96', '255', '0', 'Luminous vivid pistachio'],
    ['174', '231', '139', 'Light pistachio'],
    ['137', '231', '81', 'Brilliant pistachio'],
    ['87', '231', '0', 'Vivid pistachio'],
    ['109', '168', '74', 'Moderate pistachio'],
    ['63', '168', '0', 'Strong pistachio'],
    ['58', '89', '39', 'Dark pistachio'],
    ['33', '89', '0', 'Deep pistachio'],
    ['233', '255', '226', 'Very pale harlequin'],
    ['209', '255', '194', 'Pale harlequin'],
    ['182', '255', '158', 'Very light harlequin'],
    ['139', '255', '101', 'Light brilliant harlequin'],
    ['64', '255', '0', 'Luminous vivid harlequin'],
    ['196', '231', '184', 'Pale, light grayish harlequin'],
    ['162', '231', '139', 'Light harlequin'],
    ['119', '231', '81', 'Brilliant harlequin'],
    ['58', '231', '0', 'Vivid harlequin'],
    ['136', '168', '125', 'Grayish harlequin'],
    ['97', '168', '74', 'Moderate harlequin'],
    ['42', '168', '0', 'Strong harlequin'],
    ['72', '89', '66', 'Dark grayish harlequin'],
    ['52', '89', '39', 'Dark harlequin'],
    ['22', '89', '0', 'Deep harlequin'],
    ['201', '255', '194', 'Pale sap green'],
    ['170', '255', '158', 'Very light sap green'],
    ['120', '255', '101', 'Light brilliant sap green'],
    ['32', '255', '0', 'Luminous vivid sap green'],
    ['150', '231', '139', 'Light sap green'],
    ['100', '231', '81', 'Brilliant sap green'],
    ['29', '231', '0', 'Vivid sap green'],
    ['85', '168', '74', 'Moderate sap green'],
    ['21', '168', '0', 'Strong sap green'],
    ['45', '89', '39', 'Dark sap green'],
    ['11', '89', '0', 'Deep sap green'],
    ['246', '255', '246', 'Greenish white'],
    ['226', '255', '226', 'Very pale green'],
    ['194', '255', '194', 'Pale green'],
    ['158', '255', '158', 'Very light green'],
    ['101', '255', '101', 'Light brilliant green'],
    ['0', '255', '0', 'Luminous vivid green'],
    ['218', '231', '218', 'Light greenish gray'],
    ['184', '231', '184', 'Pale, light grayish green'],
    ['139', '231', '139', 'Light green'],
    ['81', '231', '81', 'Brilliant green'],
    ['0', '231', '0', 'Vivid green'],
    ['156', '168', '156', 'Greenish gray'],
    ['125', '168', '125', 'Grayish green'],
    ['74', '168', '74', 'Moderate green'],
    ['0', '168', '0', 'Strong green'],
    ['83', '89', '83', 'Dark greenish gray'],
    ['66', '89', '66', 'Dark grayish green'],
    ['39', '89', '39', 'Dark green'],
    ['0', '89', '0', 'Deep green'],
    ['26', '29', '26', 'Greenish black'],
    ['17', '29', '17', 'Very dark green'],
    ['0', '29', '0', 'Very deep green'],
    ['194', '255', '201', 'Pale emerald green'],
    ['158', '255', '170', 'Very light emerald green'],
    ['101', '255', '120', 'Light brilliant emerald green'],
    ['0', '255', '32', 'Luminous vivid emerald green'],
    ['139', '231', '150', 'Light emerald green'],
    ['81', '231', '100', 'Brilliant emerald green'],
    ['0', '231', '29', 'Vivid emerald green'],
    ['74', '168', '85', 'Moderate emerald green'],
    ['0', '168', '21', 'Strong emerald green'],
    ['39', '89', '45', 'Dark emerald green'],
    ['0', '89', '11', 'Deep emerald green'],
    ['226', '255', '233', 'Very pale malachite green'],
    ['194', '255', '209', 'Pale malachite green'],
    ['158', '255', '182', 'Very light malachite green'],
    ['101', '255', '139', 'Light brilliant malachite green'],
    ['0', '255', '64', 'Luminous vivid malachite green'],
    ['184', '231', '196', 'Pale, light grayish malachite green'],
    ['139', '231', '162', 'Light malachite green'],
    ['81', '231', '119', 'Brilliant malachite green'],
    ['0', '231', '58', 'Vivid malachite green'],
    ['125', '168', '136', 'Grayish malachite green'],
    ['74', '168', '97', 'Moderate malachite green'],
    ['0', '168', '42', 'Strong malachite green'],
    ['66', '89', '72', 'Dark grayish malachite green'],
    ['39', '89', '52', 'Dark malachite green'],
    ['0', '89', '22', 'Deep malachite green'],
    ['194', '255', '217', 'Pale sea green'],
    ['158', '255', '194', 'Very light sea green'],
    ['101', '255', '159', 'Light brilliant sea green'],
    ['0', '255', '96', 'Luminous vivid sea green'],
    ['139', '231', '174', 'Light sea green'],
    ['81', '231', '137', 'Brilliant sea green'],
    ['0', '231', '87', 'Vivid sea green'],
    ['74', '168', '109', 'Moderate sea green'],
    ['0', '168', '63', 'Strong sea green'],
    ['39', '89', '58', 'Dark sea green'],
    ['0', '89', '33', 'Deep sea green'],
    ['226', '255', '240', 'Very pale spring green'],
    ['194', '255', '224', 'Pale spring green'],
    ['158', '255', '207', 'Very light spring green'],
    ['101', '255', '178', 'Light brilliant spring green'],
    ['0', '255', '128', 'Luminous vivid spring green'],
    ['184', '231', '208', 'Pale, light grayish spring green'],
    ['139', '231', '185', 'Light spring green'],
    ['81', '231', '156', 'Brilliant spring green'],
    ['0', '231', '116', 'Vivid spring green'],
    ['125', '168', '147', 'Grayish spring green'],
    ['74', '168', '121', 'Moderate spring green'],
    ['0', '168', '84', 'Strong spring green'],
    ['66', '89', '78', 'Dark grayish spring green'],
    ['39', '89', '64', 'Dark spring green'],
    ['0', '89', '45', 'Deep spring green'],
    ['17', '29', '23', 'Very dark spring green'],
    ['0', '29', '14', 'Very deep spring green'],
    ['194', '255', '232', 'Pale aquamarine'],
    ['158', '255', '219', 'Very light aquamarine'],
    ['101', '255', '197', 'Light brilliant aquamarine'],
    ['0', '255', '159', 'Luminous vivid aquamarine'],
    ['139', '231', '197', 'Light aquamarine'],
    ['81', '231', '175', 'Brilliant aquamarine'],
    ['0', '231', '145', 'Vivid aquamarine'],
    ['74', '168', '133', 'Moderate aquamarine'],
    ['0', '168', '105', 'Strong aquamarine'],
    ['39', '89', '70', 'Dark aquamarine'],
    ['0', '89', '56', 'Deep aquamarine'],
    ['226', '255', '248', 'Very pale turquoise'],
    ['194', '255', '240', 'Pale turquoise'],
    ['158', '255', '231', 'Very light turquoise'],
    ['101', '255', '216', 'Light brilliant turquoise'],
    ['0', '255', '191', 'Luminous vivid turquoise'],
    ['184', '231', '220', 'Pale, light grayish turquoise'],
    ['139', '231', '208', 'Light turquoise'],
    ['81', '231', '194', 'Brilliant turquoise'],
    ['0', '231', '174', 'Vivid turquoise'],
    ['125', '168', '158', 'Grayish turquoise'],
    ['74', '168', '145', 'Moderate turquoise'],
    ['0', '168', '126', 'Strong turquoise'],
    ['66', '89', '84', 'Dark grayish turquoise'],
    ['39', '89', '77', 'Dark turquoise'],
    ['0', '89', '67', 'Deep turquoise'],
    ['194', '255', '247', 'Pale opal'],
    ['158', '255', '243', 'Very light opal'],
    ['101', '255', '236', 'Light brilliant opal'],
    ['0', '255', '223', 'Luminous vivid opal'],
    ['139', '231', '220', 'Light opal'],
    ['81', '231', '213', 'Brilliant opal'],
    ['0', '231', '202', 'Vivid opal'],
    ['74', '168', '156', 'Moderate opal'],
    ['0', '168', '147', 'Strong opal'],
    ['39', '89', '83', 'Dark opal'],
    ['0', '89', '78', 'Deep opal'],
    ['246', '255', '255', 'Cyanish white'],
    ['226', '255', '255', 'Very pale cyan'],
    ['194', '255', '255', 'Pale cyan'],
    ['158', '255', '255', 'Very light cyan'],
    ['101', '255', '255', 'Light brilliant cyan'],
    ['0', '255', '255', 'Luminous vivid cyan'],
    ['218', '231', '231', 'Light cyanish gray'],
    ['184', '231', '231', 'Pale, light grayish cyan'],
    ['139', '231', '231', 'Light cyan'],
    ['81', '231', '231', 'Brilliant cyan'],
    ['0', '231', '231', 'Vivid cyan'],
    ['156', '168', '168', 'Cyanish gray'],
    ['125', '168', '168', 'Grayish cyan'],
    ['74', '168', '168', 'Moderate cyan'],
    ['0', '168', '168', 'Strong cyan'],
    ['83', '89', '89', 'Dark cyanish gray'],
    ['66', '89', '89', 'Dark grayish cyan'],
    ['39', '89', '89', 'Dark cyan'],
    ['0', '89', '89', 'Deep cyan'],
    ['26', '29', '29', 'Cyanish black'],
    ['17', '29', '29', 'Very dark cyan'],
    ['0', '29', '29', 'Very deep cyan'],
    ['194', '247', '255', 'Pale arctic blue'],
    ['158', '243', '255', 'Very light arctic blue'],
    ['101', '236', '255', 'Light brilliant arctic blue'],
    ['0', '223', '255', 'Luminous vivid arctic blue'],
    ['139', '220', '231', 'Light arctic blue'],
    ['81', '213', '231', 'Brilliant arctic blue'],
    ['0', '202', '231', 'Vivid arctic blue'],
    ['74', '156', '168', 'Moderate arctic blue'],
    ['0', '147', '168', 'Strong arctic blue'],
    ['39', '83', '89', 'Dark arctic blue'],
    ['0', '78', '89', 'Deep arctic blue'],
    ['226', '248', '255', 'Very pale cerulean'],
    ['194', '240', '255', 'Pale cerulean'],
    ['158', '231', '255', 'Very light cerulean'],
    ['101', '216', '255', 'Light brilliant cerulean'],
    ['0', '191', '255', 'Luminous vivid cerulean'],
    ['184', '220', '231', 'Pale, light grayish cerulean'],
    ['139', '208', '231', 'Light cerulean'],
    ['81', '194', '231', 'Brilliant cerulean'],
    ['0', '174', '231', 'Vivid cerulean'],
    ['125', '158', '168', 'Grayish cerulean'],
    ['74', '145', '168', 'Moderate cerulean'],
    ['0', '126', '168', 'Strong cerulean'],
    ['66', '84', '89', 'Dark grayish cerulean'],
    ['39', '77', '89', 'Dark cerulean'],
    ['0', '67', '89', 'Deep cerulean'],
    ['194', '232', '255', 'Pale cornflower blue'],
    ['158', '219', '255', 'Very light cornflower blue'],
    ['101', '197', '255', 'Light brilliant cornflower blue'],
    ['0', '159', '255', 'Luminous vivid cornflower blue'],
    ['139', '197', '231', 'Light cornflower blue'],
    ['81', '175', '231', 'Brilliant cornflower blue'],
    ['0', '145', '231', 'Vivid cornflower blue'],
    ['74', '133', '168', 'Moderate cornflower blue'],
    ['0', '105', '168', 'Strong cornflower blue'],
    ['39', '70', '89', 'Dark cornflower blue'],
    ['0', '56', '89', 'Deep cornflower blue'],
    ['226', '240', '255', 'Very pale azure'],
    ['194', '224', '255', 'Pale azure'],
    ['158', '207', '255', 'Very light azure'],
    ['101', '178', '255', 'Light brilliant azure'],
    ['0', '128', '255', 'Luminous vivid azure'],
    ['184', '208', '231', 'Pale, light grayish azure'],
    ['139', '185', '231', 'Light azure'],
    ['81', '156', '231', 'Brilliant azure'],
    ['0', '116', '231', 'Vivid azure'],
    ['125', '147', '168', 'Grayish azure'],
    ['74', '121', '168', 'Moderate azure'],
    ['0', '84', '168', 'Strong azure'],
    ['66', '78', '89', 'Dark grayish azure'],
    ['39', '64', '89', 'Dark azure'],
    ['0', '45', '89', 'Deep azure'],
    ['17', '23', '29', 'Very dark azure'],
    ['0', '14', '29', 'Very deep azure'],
    ['194', '217', '255', 'Pale cobalt blue'],
    ['158', '194', '255', 'Very light cobalt blue'],
    ['101', '159', '255', 'Light brilliant cobalt blue'],
    ['0', '96', '255', 'Luminous vivid cobalt blue'],
    ['139', '174', '231', 'Light cobalt blue'],
    ['81', '137', '231', 'Brilliant cobalt blue'],
    ['0', '87', '231', 'Vivid cobalt blue'],
    ['74', '109', '168', 'Moderate cobalt blue'],
    ['0', '63', '168', 'Strong cobalt blue'],
    ['39', '58', '89', 'Dark cobalt blue'],
    ['0', '33', '89', 'Deep cobalt blue'],
    ['226', '233', '255', 'Very pale sapphire blue'],
    ['194', '209', '255', 'Pale sapphire blue'],
    ['158', '182', '255', 'Very light sapphire blue'],
    ['101', '139', '255', 'Light brilliant sapphire blue'],
    ['0', '64', '255', 'Luminous vivid sapphire blue'],
    ['184', '196', '231', 'Pale, light grayish sapphire blue'],
    ['139', '162', '231', 'Light sapphire blue'],
    ['81', '119', '231', 'Brilliant sapphire blue'],
    ['0', '58', '231', 'Vivid sapphire blue'],
    ['125', '136', '168', 'Grayish sapphire blue'],
    ['74', '97', '168', 'Moderate sapphire blue'],
    ['0', '42', '168', 'Strong sapphire blue'],
    ['66', '72', '89', 'Dark grayish sapphire blue'],
    ['39', '52', '89', 'Dark sapphire blue'],
    ['0', '22', '89', 'Deep sapphire blue'],
    ['194', '201', '255', 'Pale phthalo blue'],
    ['158', '170', '255', 'Very light phthalo blue'],
    ['101', '120', '255', 'Light brilliant phthalo blue'],
    ['0', '32', '255', 'Luminous vivid phthalo blue'],
    ['139', '150', '231', 'Light phthalo blue'],
    ['81', '100', '231', 'Brilliant phthalo blue'],
    ['0', '29', '231', 'Vivid phthalo blue'],
    ['74', '85', '168', 'Moderate phthalo blue'],
    ['0', '21', '168', 'Strong phthalo blue'],
    ['39', '45', '89', 'Dark phthalo blue'],
    ['0', '11', '89', 'Deep phthalo blue'],
    ['246', '246', '255', 'Bluish white'],
    ['226', '226', '255', 'Very pale blue'],
    ['194', '194', '255', 'Pale blue'],
    ['158', '158', '255', 'Very light blue'],
    ['101', '101', '255', 'Light brilliant blue'],
    ['0', '0', '255', 'Luminous vivid blue'],
    ['218', '218', '231', 'Light bluish gray'],
    ['184', '184', '231', 'Pale, light grayish blue'],
    ['139', '139', '231', 'Light blue'],
    ['81', '81', '231', 'Brilliant blue'],
    ['0', '0', '231', 'Vivid blue'],
    ['156', '156', '168', 'Bluish gray'],
    ['125', '125', '168', 'Grayish blue'],
    ['74', '74', '168', 'Moderate blue'],
    ['0', '0', '168', 'Strong blue'],
    ['83', '83', '89', 'Dark bluish gray'],
    ['66', '66', '89', 'Dark grayish blue'],
    ['39', '39', '89', 'Dark blue'],
    ['0', '0', '89', 'Deep blue'],
    ['26', '26', '29', 'Bluish black'],
    ['17', '17', '29', 'Very dark blue'],
    ['0', '0', '29', 'Very deep blue'],
    ['201', '194', '255', 'Pale persian blue'],
    ['170', '158', '255', 'Very light persian blue'],
    ['120', '101', '255', 'Light brilliant persian blue'],
    ['32', '0', '255', 'Luminous vivid persian blue'],
    ['150', '139', '231', 'Light persian blue'],
    ['100', '81', '231', 'Brilliant persian blue'],
    ['29', '0', '231', 'Vivid persian blue'],
    ['85', '74', '168', 'Moderate persian blue'],
    ['21', '0', '168', 'Strong persian blue'],
    ['45', '39', '89', 'Dark persian blue'],
    ['11', '0', '89', 'Deep persian blue'],
    ['233', '226', '255', 'Very pale indigo'],
    ['209', '194', '255', 'Pale indigo'],
    ['182', '158', '255', 'Very light indigo'],
    ['139', '101', '255', 'Light brilliant indigo'],
    ['64', '0', '255', 'Luminous vivid indigo'],
    ['196', '184', '231', 'Pale, light grayish indigo'],
    ['162', '139', '231', 'Light indigo'],
    ['119', '81', '231', 'Brilliant indigo'],
    ['58', '0', '231', 'Vivid indigo'],
    ['136', '125', '168', 'Grayish indigo'],
    ['97', '74', '168', 'Moderate indigo'],
    ['42', '0', '168', 'Strong indigo'],
    ['72', '66', '89', 'Dark grayish indigo'],
    ['52', '39', '89', 'Dark indigo'],
    ['22', '0', '89', 'Deep indigo'],
    ['217', '194', '255', 'Pale blue violet'],
    ['194', '158', '255', 'Very light blue violet'],
    ['159', '101', '255', 'Light brilliant blue violet'],
    ['96', '0', '255', 'Luminous vivid blue violet'],
    ['174', '139', '231', 'Light blue violet'],
    ['137', '81', '231', 'Brilliant blue violet'],
    ['87', '0', '231', 'Vivid blue violet'],
    ['109', '74', '168', 'Moderate blue violet'],
    ['63', '0', '168', 'Strong blue violet'],
    ['58', '39', '89', 'Dark blue violet'],
    ['33', '0', '89', 'Deep blue violet'],
    ['240', '226', '255', 'Very pale violet'],
    ['224', '194', '255', 'Pale violet'],
    ['207', '158', '255', 'Very light violet'],
    ['178', '101', '255', 'Light brilliant violet'],
    ['128', '0', '255', 'Luminous vivid violet'],
    ['208', '184', '231', 'Pale, light grayish violet'],
    ['185', '139', '231', 'Light violet'],
    ['156', '81', '231', 'Brilliant violet'],
    ['116', '0', '231', 'Vivid violet'],
    ['147', '125', '168', 'Grayish violet'],
    ['121', '74', '168', 'Moderate violet'],
    ['84', '0', '168', 'Strong violet'],
    ['78', '66', '89', 'Dark grayish violet'],
    ['64', '39', '89', 'Dark violet'],
    ['45', '0', '89', 'Deep violet'],
    ['23', '17', '29', 'Very dark violet'],
    ['14', '0', '29', 'Very deep violet'],
    ['232', '194', '255', 'Pale purple'],
    ['219', '158', '255', 'Very light purple'],
    ['197', '101', '255', 'Light brilliant purple'],
    ['159', '0', '255', 'Luminous vivid purple'],
    ['197', '139', '231', 'Light purple'],
    ['175', '81', '231', 'Brilliant purple'],
    ['145', '0', '231', 'Vivid purple'],
    ['133', '74', '168', 'Moderate purple'],
    ['105', '0', '168', 'Strong purple'],
    ['70', '39', '89', 'Dark purple'],
    ['56', '0', '89', 'Deep purple'],
    ['248', '226', '255', 'Very pale mulberry'],
    ['240', '194', '255', 'Pale mulberry'],
    ['231', '158', '255', 'Very light mulberry'],
    ['216', '101', '255', 'Light brilliant mulberry'],
    ['191', '0', '255', 'Luminous vivid mulberry'],
    ['220', '184', '231', 'Pale, light grayish mulberry'],
    ['208', '139', '231', 'Light mulberry'],
    ['194', '81', '231', 'Brilliant mulberry'],
    ['174', '0', '231', 'Vivid mulberry'],
    ['158', '125', '168', 'Grayish mulberry'],
    ['145', '74', '168', 'Moderate mulberry'],
    ['126', '0', '168', 'Strong mulberry'],
    ['84', '66', '89', 'Dark grayish mulberry'],
    ['77', '39', '89', 'Dark mulberry'],
    ['67', '0', '89', 'Deep mulberry'],
    ['247', '194', '255', 'Pale heliotrope'],
    ['243', '158', '255', 'Very light heliotrope'],
    ['236', '101', '255', 'Light brilliant heliotrope'],
    ['223', '0', '255', 'Luminous vivid heliotrope'],
    ['220', '139', '231', 'Light heliotrope'],
    ['213', '81', '231', 'Brilliant heliotrope'],
    ['202', '0', '231', 'Vivid heliotrope'],
    ['156', '74', '168', 'Moderate heliotrope'],
    ['147', '0', '168', 'Strong heliotrope'],
    ['83', '39', '89', 'Dark heliotrope'],
    ['78', '0', '89', 'Deep heliotrope'],
    ['255', '246', '255', 'Magentaish white'],
    ['255', '226', '255', 'Very pale magenta'],
    ['255', '194', '255', 'Pale magenta'],
    ['255', '158', '255', 'Very light magenta'],
    ['255', '101', '255', 'Light brilliant magenta'],
    ['255', '0', '255', 'Luminous vivid magenta'],
    ['231', '218', '231', 'Light magentaish gray'],
    ['231', '184', '231', 'Pale, light grayish magenta'],
    ['231', '139', '231', 'Light magenta'],
    ['231', '81', '231', 'Brilliant magenta'],
    ['231', '0', '231', 'Vivid magenta'],
    ['168', '156', '168', 'Magentaish gray'],
    ['168', '125', '168', 'Grayish magenta'],
    ['168', '74', '168', 'Moderate magenta'],
    ['168', '0', '168', 'Strong magenta'],
    ['89', '83', '89', 'Dark magentaish gray'],
    ['89', '66', '89', 'Dark grayish magenta'],
    ['89', '39', '89', 'Dark magenta'],
    ['89', '0', '89', 'Deep magenta'],
    ['29', '26', '29', 'Magentaish black'],
    ['29', '17', '29', 'Very dark magenta'],
    ['29', '0', '29', 'Very deep magenta'],
    ['255', '194', '247', 'Pale orchid'],
    ['255', '158', '243', 'Very light orchid'],
    ['255', '101', '236', 'Light brilliant orchid'],
    ['255', '0', '223', 'Luminous vivid orchid'],
    ['231', '139', '220', 'Light orchid'],
    ['231', '81', '213', 'Brilliant orchid'],
    ['231', '0', '202', 'Vivid orchid'],
    ['168', '74', '156', 'Moderate orchid'],
    ['168', '0', '147', 'Strong orchid'],
    ['89', '39', '83', 'Dark orchid'],
    ['89', '0', '78', 'Deep orchid'],
    ['255', '226', '248', 'Very pale fuchsia'],
    ['255', '194', '240', 'Pale fuchsia'],
    ['255', '158', '231', 'Very light fuchsia'],
    ['255', '101', '216', 'Light brilliant fuchsia'],
    ['255', '0', '191', 'Luminous vivid fuchsia'],
    ['231', '184', '220', 'Pale, light grayish fuchsia'],
    ['231', '139', '208', 'Light fuchsia'],
    ['231', '81', '194', 'Brilliant fuchsia'],
    ['231', '0', '174', 'Vivid fuchsia'],
    ['168', '125', '158', 'Grayish fuchsia'],
    ['168', '74', '145', 'Moderate fuchsia'],
    ['168', '0', '126', 'Strong fuchsia'],
    ['89', '66', '84', 'Dark grayish fuchsia'],
    ['89', '39', '77', 'Dark fuchsia'],
    ['89', '0', '67', 'Deep fuchsia'],
    ['255', '194', '232', 'Pale cerise'],
    ['255', '158', '219', 'Very light cerise'],
    ['255', '101', '197', 'Light brilliant cerise'],
    ['255', '0', '159', 'Luminous vivid cerise'],
    ['231', '139', '197', 'Light cerise'],
    ['231', '81', '175', 'Brilliant cerise'],
    ['231', '0', '145', 'Vivid cerise'],
    ['168', '74', '133', 'Moderate cerise'],
    ['168', '0', '105', 'Strong cerise'],
    ['89', '39', '70', 'Dark cerise'],
    ['89', '0', '56', 'Deep cerise'],
    ['255', '226', '240', 'Very pale rose'],
    ['255', '194', '224', 'Pale rose'],
    ['255', '158', '207', 'Very light rose'],
    ['255', '101', '178', 'Light brilliant rose'],
    ['255', '0', '128', 'Luminous vivid rose'],
    ['231', '184', '208', 'Pale, light grayish rose'],
    ['231', '139', '185', 'Light rose'],
    ['231', '81', '156', 'Brilliant rose'],
    ['231', '0', '116', 'Vivid rose'],
    ['168', '125', '147', 'Grayish rose'],
    ['168', '74', '121', 'Moderate rose'],
    ['168', '0', '84', 'Strong rose'],
    ['89', '66', '78', 'Dark grayish rose'],
    ['89', '39', '64', 'Dark rose'],
    ['89', '0', '45', 'Deep rose'],
    ['29', '17', '23', 'Very dark rose'],
    ['29', '0', '14', 'Very deep rose'],
    ['255', '194', '217', 'Pale raspberry'],
    ['255', '158', '194', 'Very light raspberry'],
    ['255', '101', '159', 'Light brilliant raspberry'],
    ['255', '0', '96', 'Luminous vivid raspberry'],
    ['231', '139', '174', 'Light raspberry'],
    ['231', '81', '137', 'Brilliant raspberry'],
    ['231', '0', '87', 'Vivid raspberry'],
    ['168', '74', '109', 'Moderate raspberry'],
    ['168', '0', '63', 'Strong raspberry'],
    ['89', '39', '58', 'Dark raspberry'],
    ['89', '0', '33', 'Deep raspberry'],
    ['255', '226', '233', 'Very pale crimson'],
    ['255', '194', '209', 'Pale crimson'],
    ['255', '158', '182', 'Very light crimson'],
    ['255', '101', '139', 'Light brilliant crimson'],
    ['255', '0', '64', 'Luminous vivid crimson'],
    ['231', '184', '196', 'Pale, light grayish crimson'],
    ['231', '139', '162', 'Light crimson'],
    ['231', '81', '119', 'Brilliant crimson'],
    ['231', '0', '58', 'Vivid crimson'],
    ['168', '125', '136', 'Grayish crimson'],
    ['168', '74', '97', 'Moderate crimson'],
    ['168', '0', '42', 'Strong crimson'],
    ['89', '66', '72', 'Dark grayish crimson'],
    ['89', '39', '52', 'Dark crimson'],
    ['89', '0', '22', 'Deep crimson'],
    ['255', '194', '201', 'Pale amaranth'],
    ['255', '158', '170', 'Very light amaranth'],
    ['255', '101', '120', 'Light brilliant amaranth'],
    ['255', '0', '32', 'Luminous vivid amaranth'],
    ['231', '139', '150', 'Light amaranth'],
    ['231', '81', '100', 'Brilliant amaranth'],
    ['231', '0', '29', 'Vivid amaranth'],
    ['168', '74', '85', 'Moderate amaranth'],
    ['168', '0', '21', 'Strong amaranth'],
    ['89', '39', '45', 'Dark amaranth'],
    ['89', '0', '11', 'Deep amaranth']
]