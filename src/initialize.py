from Location_Manager import LocationManager
from identity_matrix import identity_matrix


def initialize_locations(location_manager):
    # EA 系列
    location_manager.add_location("EA", 860, 315, is_show=True)
    location_manager.add_location("EB", 792, 267, is_show=True)
    location_manager.add_location("EC", 710, 421, is_show=True)
    location_manager.add_location("ED", 602, 363, is_show=True)
    location_manager.add_location("EE", 684, 542, is_show=True)
    location_manager.add_location("EF", 415, 401, is_show=True)

    # M 系列
    location_manager.add_location("M", 1113, 543, is_show=True)
    location_manager.add_location("MB", 693, 595, is_show=True)

    # SA 系列
    location_manager.add_location("SA", 727, 364, is_show=True)
    location_manager.add_location("SB", 722, 231, is_show=True)
    location_manager.add_location("SC", 608, 294, is_show=True)

    # AC 系列
    location_manager.add_location("AC", 933, 552, is_show=True)
    location_manager.add_location("A", 481, 666, is_show=True)
    location_manager.add_location("AB", 481, 666, is_show=False)

    # HA 系列
    location_manager.add_location("HA", 841, 452, is_show=True)
    location_manager.add_location("HB/F", 1038, 576, is_show=True)
    location_manager.add_location("HC", 942, 631, is_show=True)

    # CY, EO, EV, CS, ES, CE, AD
    location_manager.add_location("CY", 552, 356, is_show=True)
    location_manager.add_location("EO", 580, 292, is_show=True)
    location_manager.add_location("EV", 741, 54, is_show=True)
    location_manager.add_location("CS", 789, 401, is_show=True)
    location_manager.add_location("ES", 1144, 607, is_show=True)
    location_manager.add_location("CE", 587, 715, is_show=True)
    location_manager.add_location("AD", 951, 357, is_show=True)

    # Lib 系列
    location_manager.add_location("Lib", 743, 485, is_show=True)

    # RA 系列
    location_manager.add_location("RA", 910, 249, is_show=True)
    location_manager.add_location("RB", 815, 696, is_show=True)
    location_manager.add_location("RC", 875, 189, is_show=True)
    location_manager.add_location("RD", 358, 521, is_show=True)
    location_manager.add_location("RE", 431, 644, is_show=True)
    location_manager.add_location("RG", 812, 596, is_show=True)
    location_manager.add_location("RH", 788, 662, is_show=True)
    location_manager.add_location("RI", 843, 165, is_show=True)
    location_manager.add_location("RJ", 861, 141, is_show=True)
    location_manager.add_location("RK", 879, 123, is_show=True)
    location_manager.add_location("RL", 369, 576, is_show=True)
    location_manager.add_location("RM", 391, 619, is_show=True)

    # DA 系列
    location_manager.add_location("DA", 887, 527, is_show=True)
    location_manager.add_location("DB", 821, 207, is_show=True)
    location_manager.add_location("DC", 815, 696, is_show=True)
    location_manager.add_location("DD", 431, 644, is_show=True)

    # PA 系列
    location_manager.add_location("PA", 971, 361, is_show=True)
    location_manager.add_location("PB", 662, 147, is_show=True)
    location_manager.add_location("PC", 393, 376, is_show=True)
    location_manager.add_location("PD", 676, 680, is_show=True)
    location_manager.add_location("PE", 555, 663, is_show=True)
    location_manager.add_location("PF", 446, 658, is_show=True)
    location_manager.add_location("PG", 930, 605, is_show=True)
    location_manager.add_location("P", 1190, 537, is_show=True)

    # BA 系列
    location_manager.add_location("BA", 516, 800, is_show=True)
    location_manager.add_location("BC", 1212, 364, is_show=True)
    location_manager.add_location("BD", 1268, 551, is_show=True)
    location_manager.add_location("BH", 146, 546, is_show=True)

    # GN, GS, GP
    location_manager.add_location("GN", 1136, 323, is_show=True)
    location_manager.add_location("GS", 73, 480, is_show=True)
    location_manager.add_location("GP", 709, 43, is_show=True)

    # LA 系列
    location_manager.add_location("LA", 1080, 385, is_show=True)
    location_manager.add_location("LB", 868, 498, is_show=True)
    location_manager.add_location("LC", 1106, 595, is_show=True)
    location_manager.add_location("LD", 240, 172, is_show=True)

    # FA 系列
    location_manager.add_location("FA", 649, 166, is_show=True)
    location_manager.add_location("FB", 681, 123, is_show=True)
    location_manager.add_location("FC", 596, 85, is_show=True)
    location_manager.add_location("FD", 601, 152, is_show=True)
    location_manager.add_location("FE", 418, 231, is_show=True)
    location_manager.add_location("FF", 508, 269, is_show=True)
    location_manager.add_location("FG", 1196, 494, is_show=True)
    location_manager.add_location("FH", 441, 364, is_show=True)
    location_manager.add_location("FI", 1153, 556, is_show=True)
    location_manager.add_location("FJ", 540, 531, is_show=True)

    # ZA 系列
    location_manager.add_location("ZA", 1057, 318, is_show=True)
    # location_manager.add_location("ZB", 0, 0, is_show=True)
    location_manager.add_location("ZC", 950, 402, is_show=True)
    location_manager.add_location("ZD", 984, 611, is_show=True)
    location_manager.add_location("ZE", 881, 737, is_show=True)
    location_manager.add_location("ZF", 536, 776, is_show=True)
    location_manager.add_location("ZG", 491, 759, is_show=True)
    location_manager.add_location("ZH", 223, 410, is_show=True)
    location_manager.add_location("ZI", 219, 257, is_show=True)
    location_manager.add_location("ZJ", 852, 53, is_show=True)

    location_manager.add_location("XA", 1103, 334, is_show=True)
    location_manager.add_location("XB", 951, 391, is_show=True)
    location_manager.add_location("XC", 837, 180, is_show=True)
    location_manager.add_location("XD", 631, 109, is_show=True)
    location_manager.add_location("XE", 758, 299, is_show=True)
    location_manager.add_location("XF", 627, 322, is_show=True)
    location_manager.add_location("XG", 562, 421, is_show=True)
    location_manager.add_location("XH", 659, 582, is_show=True)
    location_manager.add_location("XI", 360, 477, is_show=True)
    location_manager.add_location("XJ", 540, 696, is_show=True)
    location_manager.add_location("XK", 507, 766, is_show=True)
    location_manager.add_location("XL", 843, 523, is_show=True)
    location_manager.add_location("XM", 888, 721, is_show=True)
    location_manager.add_location("XN", 1017, 588, is_show=True)
    location_manager.add_location("XO", 157, 464, is_show=True)
    location_manager.add_location("XP", 727, 366, is_show=True)
    location_manager.add_location("XQ", 1157, 526, is_show=True)
    location_manager.add_location("XR", 622, 729, is_show=True)
    location_manager.add_location("XS", 1217, 397, is_show=True)
    location_manager.add_location("XT", 753, 785, is_show=True)



def initialize_edge(edges):
    for i in range(len(identity_matrix) - 1):
        for j in range(len(identity_matrix[0]) - 1):
            if identity_matrix[i + 1][j + 1] == 1:
                edges.add_edge(i + 1, j + 1, 1)
