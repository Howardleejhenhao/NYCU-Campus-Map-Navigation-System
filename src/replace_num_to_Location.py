node_index_to_building_code = [
    None,
    "EA", "EB", "EC", "ED", "EE", "EF", "M", "MB", "SA", "SB",
    "SC", "AC", "A", "AB", "HA", "HB/F", "HC", "CY", "EO", "EV",
    "CS", "ES", "CE", "AD", "Lib", "RA", "RB", "RC", "RD", "RE",
    "RG", "RH", "RI", "RJ", "RK", "RL", "RM", "DA", "DB", "DC", "DD",
    "PA", "PB", "PC", "PD", "PE", "PF", "PG", "P", "BA", "BC", "BD",
    "BH", "GN", "GS", "GP", "LA", "LB", "LC", "LD", "FA", "FB", "FC",
    "FD", "FE", "FF", "FG", "FH", "FI", "FJ", "ZA", "ZB", "ZC", "ZD",
    "ZE", "ZF", "ZG", "ZH", "ZI", "ZJ", "XA", "XB", "XC", "XD", "XE",
    "XF", "XG", "XH", "XI", "XJ", "XK", "XL", "XM", "XN", "XO", "XP", "XQ", "XR", "XS", "XT"
]

building_code_to_node_index = {value: idx for idx, value in enumerate(node_index_to_building_code) if value is not None}

# print("數字對應字串 (1-based):")
# for i, value in enumerate(num_to_str):
#     if value is not None:
#         print(f"{i} -> {value}")

# print("\n字串對應數字:")
# for key, value in str_to_num.items():
#     print(f"{key} -> {value}")
