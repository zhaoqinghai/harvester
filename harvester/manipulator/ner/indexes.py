""" 所有 algorithm 的基础 tag indexes

!!慎改!!

"""

from collections import OrderedDict


class TagIndexError(IndexError):
    """ 词典等有误，抛 Index Error"""

    def __init__(self, message):
        self.message = message


# JIEBA_POS_INDEX
JIEBA_POS_INDEX = OrderedDict([
    ('n', 0),
    ('nr', 1),
    ('ns', 2),
    ('nt', 3),
    ('nz', 4),
    ('v', 5),
    ('a', 6),
    ('ad', 7),
    ('ag', 8),
    ('an', 9),
    ('b', 10),
    ('c', 11),
    ('d', 12),
    ('df', 13),
    ('dg', 14),
    ('e', 15),
    ('f', 16),
    ('g', 17),
    ('h', 18),
    ('i', 19),
    ('j', 20),
    ('k', 21),
    ('l', 22),
    ('m', 23),
    ('mq', 24),
    ('mg', 25),
    ('nrt', 26),
    ('nrfg', 27),
    ('ng', 28),
    ('o', 29),
    ('p', 30),
    ('q', 31),
    ('r', 32),
    ('rr', 33),
    ('rz', 34),
    ('rg', 35),
    ('s', 36),
    ('t', 37),
    ('tg', 38),
    ('u', 39),
    ('ug', 40),
    ('uv', 41),
    ('ul', 42),
    ('uz', 43),
    ('uj', 44),
    ('ud', 45),
    ('vd', 46),
    ('vg', 47),
    ('vi', 48),
    ('vn', 49),
    ('vq', 50),
    ('x', 51),
    ('y', 52),
    ('z', 53),
    ('zg', 54),
    ('w', 55),
    ('eng', 56),
    ('yg', 57),
    ('placeholder1', 58)
])

# INDEX_POS_JIEBA( Reversed jieba index)
INDEX_POS_JIEBA = OrderedDict([
    (0, 'n'),
    (1, 'nr'),
    (2, 'ns'),
    (3, 'nt'),
    (4, 'nz'),
    (5, 'v'),
    (6, 'a'),
    (7, 'ad'),
    (8, 'ag'),
    (9, 'an'),
    (10, 'b'),
    (11, 'c'),
    (12, 'd'),
    (13, 'df'),
    (14, 'dg'),
    (15, 'e'),
    (16, 'f'),
    (17, 'g'),
    (18, 'h'),
    (19, 'i'),
    (20, 'j'),
    (21, 'k'),
    (22, 'l'),
    (23, 'm'),
    (24, 'mq'),
    (25, 'mg'),
    (26, 'nrt'),
    (27, 'nrfg'),
    (28, 'ng'),
    (29, 'o'),
    (30, 'p'),
    (31, 'q'),
    (32, 'r'),
    (33, 'rr'),
    (34, 'rz'),
    (35, 'rg'),
    (36, 's'),
    (37, 't'),
    (38, 'tg'),
    (39, 'u'),
    (40, 'ug'),
    (41, 'uv'),
    (42, 'ul'),
    (43, 'uz'),
    (44, 'uj'),
    (45, 'ud'),
    (46, 'vd'),
    (47, 'vg'),
    (48, 'vi'),
    (49, 'vn'),
    (50, 'vq'),
    (51, 'x'),
    (52, 'y'),
    (53, 'z'),
    (54, 'zg'),
    (55, 'w'),
    (56, 'eng'),
    (57, 'yg'),
    (58, 'placeholder1')
])


# NER_PART_CHOICES_INDEX
NER_PART_CHOICES_INDEX = OrderedDict([
    ('nr_s', 0), ('nr_i', 1), ('nr_e', 2),
    ('ns_s', 3), ('ns_i', 4), ('ns_e', 5),
    ('nt_s', 6), ('nt_i', 7), ('nt_e', 8),
    ('o', 9)
])


# INDEX_CHOICES_PART_NER(Reversed)
INDEX_CHOICES_PART_NER = OrderedDict([
    (0, 'nr_s'), (1, 'nr_i'), (2, 'nr_e'),
    (3, 'ns_s'), (4, 'ns_i'), (5, 'ns_e'),
    (6, 'nt_s'), (7, 'nt_i'), (8, 'nt_e'),
    (9, 'o')
])


# LEGAL_NER_INDEX
LEGAL_NER_INDEX = {
    '0_0', '0_1', '0_2', '0_3', '0_6', '0_9',
    '1_1', '1_2',
    '2_0', '2_3', '2_6', '2_9',
    '3_0', '3_3', '3_4', '3_5', '3_6', '3_9',
    '4_4', '4_5',
    '5_0', '5_3', '5_6', '5_9',
    '6_0', '6_3', '6_6', '6_7', '6_8', '6_9',
    '7_7', '7_8',
    '8_0', '8_3', '8_6', '8_9',
    '9_0', '9_3', '9_6', '9_9'
 }



# ENTITY_PART_CHOICES_INDEX
ENTITY_PART_CHOICES_INDEX = OrderedDict([
    ('n_s', 0), ('n_i', 1), ('n_e', 2),
    ('e_s', 3), ('e_i', 4), ('e_e', 5),
    ('d_s', 6), ('d_i', 7), ('d_e', 8),
    ('s_s', 9), ('s_i', 10), ('s_e', 11),
    ('p_s', 12), ('p_i', 13), ('p_e', 14),
    ('o', 15)
])


# INDEX_CHOICES_PART_ENTITY
INDEX_CHOICES_PART_ENTITY = OrderedDict([
    (0, 'n_s'), (1, 'n_i'), (2, 'n_e'),
    (3, 'e_s'), (4, 'e_i'), (5, 'e_e'),
    (6, 'd_s'), (7, 'd_i'), (8, 'd_e'),
    (9, 's_s'), (10, 's_i'), (11, 's_e'),
    (12, 'p_s'), (13, 'p_i'), (14, 'p_e'),
    (15, 'o')
])


# LEGAL_ENTITY_INDEX
LEGAL_ENTITY_INDEX = {
    '0_1', '0_2', '0_0', '0_3', '0_6', '0_9', '0_12', '0_15',
    '1_1', '1_2',
    '2_0', '2_3', '2_6', '2_9', '2_12', '2_15',
    '3_4', '3_5', '3_0', '3_3', '3_6', '3_9', '3_12', '3_15',
    '4_4', '4_5',
    '5_0', '5_3', '5_6', '5_9', '5_12', '5_15',
    '6_7', '6_8', '6_0', '6_3', '6_6', '6_9', '6_12', '6_15',
    '7_7', '7_8',
    '8_0', '8_3', '8_6', '8_9', '8_12', '8_15',
    '9_10', '9_11', '9_0', '9_3', '9_6', '9_9', '9_12', '9_15',
    '10_10', '10_11',
    '11_0', '11_3', '11_6', '11_9', '11_12', '11_15',
    '12_13', '12_14',
    '12_0', '12_3', '12_6', '12_9', '12_12', '12_15',
    '13_13', '13_14',
    '14_0', '14_3', '14_6', '14_9', '14_12', '14_15',
    '15_0', '15_3', '15_6', '15_9', '15_12', '15_15'
}


# NAME_ENTITY_PART_CHOICES_INDEX
NAME_ENTITY_PART_CHOICES_INDEX = OrderedDict([
    ('s_s', 0),
    ('s_i', 1),
    ('s_e', 2),
    ('o', 3)
])


# INDEX_NAME_ENITTY_CHOICES
INDEX_NAME_ENITTY_CHOICES = OrderedDict([
    (0, 's_s'),
    (1, 's_i'),
    (2, 's_e'),
    (3, 'o')
])


# LEGAL_NAME_ENTITY_INDEX
LEGAL_NAME_ENTITY_INDEX = {
    '0_0', '0_1', '0_2', '0_3',
    '1_1', '1_2',
    '2_0', '2_3',
    '3_0', '3_3'
}


# ICTPOS
ICTPOS_DICT = {
    'PAD': 0,
    'Mg': 1, 'q': 2, 'c': 3, 'na': 4, 'ude1': 5,
    'i': 6, 'rzs': 7, 'ag': 8, 'nsf': 9, 'e': 10,
    'ntcb': 11, 'cc': 12, 'nz': 13, 'gi': 14, 'nrj': 15,
    'uguo': 16, 'vd': 17, 'nto': 18, 'tg': 19, 'dl': 20,
    'gb': 21, 'v': 22, 'j': 23, 'ry': 24, 'o': 25,
    's': 26, 'gm': 27, 'vx': 28, 'k': 29, 'udh': 30,
    'nnt': 31, 'vi': 32, 'u': 33, 'x': 34, 'l': 35,
    'd': 36, 'Rg': 37, 'r': 38, 'uyy': 39, 'vl': 40,
    'ule': 41, 'n': 42, 'nit': 43, 'nt': 44, 'vshi': 45,
    'vyou': 46, 'dg': 47, 'pbei': 48, 'nrf': 49, 'a': 50,
    'gc': 51, 'p': 52, 'ntc': 53, 'rzv': 54, 'uzhe': 55,
    'qv': 56, 'nbc': 57, 'nr2': 58, 'vn': 59, 'z': 60,
    'usuo': 61, 'f': 62, 'nba': 63, 'nf': 64, 'ryt': 65,
    'b': 66, 'ntu': 67, 'ad': 68, 'bl': 69, 'ude3': 70,
    'ns': 71, 'nr': 72, 'rr': 73, 'udeng': 74, 'vg': 75,
    'ude2': 76, 'ng': 77, 'rz': 78, 'rzt': 79, 'qt': 80,
    'nnd': 81, 'nmc': 82, 'al': 83, 't': 84, 'an': 85,
    'ryv': 86, 'y': 87, 'ulian': 88, 'uls': 89, 'vf': 90,
    'gg': 91, 'nis': 92, 'rys': 93, 'mq': 94, 'uzhi': 95,
    'w': 96, 'nhm': 97, 'pba': 98, 'nr1': 99, 'gp': 100,
    'nhd': 101, 'm': 102
}
