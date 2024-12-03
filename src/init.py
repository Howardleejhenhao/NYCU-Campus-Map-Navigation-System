import pygame
import pygame_gui
import sys
from Location import Location
from Location_Manager import LocationManager
from initialize import initialize_locations, initialize_edge
from Map import Map
from edge import Edge
from edgeManager import EdgeManager
from path_data import Path_Data
from dropdown import Dropdown
from dropdownmanager import DropdownManager
from replace_num_to_Location import node_index_to_building_code, building_code_to_node_index
from Button import Button
from scrollingbackground import ScrollingBackground
from pygame_gui_theme import theme_data

building_dict = {
    "Engineering Building 1": "EA",
    "Engineering Building 2": "EB",
    "Engineering Building 3": "EC",
    "Engineering Building 4": "ED",
    "Engineering Building 5": "EE",
    "Engineering Building 6": "EF",
    "Management Building": "M",
    "Management Building 2": "MB",
    "Science Building 1": "SA",
    "Science Building 2": "SB",
    "Science Building 3": "SC",
    "Activity Center": "AC",
    "General Building 1": "A",
    "General Building 1 Basement": "AB",
    "Humanities and Social Sciences Building 1": "HA",
    "Humanities and Social Sciences Building 2": "HB/F",
    "Humanities and Social Sciences Building 3": "HC",
    "Chiao-Ying Building": "CY",
    "Tien-Chia-Ping Photonics Building": "EO",
    "Environmental Engineering Building": "EV",
    "IT Services Center": "CS",
    "Electronics and Information Center": "ES",
    "Civil Engineering Structure Lab": "CE",
    "Auditorium": "AD",
    "Horng-Yang Library and Information Center": "Lib",
    "Zhuxuan Female Dormitory": "RA",
    "Female Dormitory 2": "RB",
    "Graduate Dormitory 1": "RC",
    "Graduate Dormitory 2": "RD",
    "Graduate Dormitory 3": "RE",
    "Student Dormitory 7": "RG",
    "Student Dormitory 8": "RH",
    "Student Dormitory 9": "RI",
    "Student Dormitory 10": "RJ",
    "Student Dormitory 11": "RK",
    "Student Dormitory 12": "RL",
    "Student Dormitory 13": "RM",
    "Dining Hall 1": "DA",
    "Dining Hall 2": "DB",
    "Female Dormitory 2 Dining Hall": "DC",
    "Graduate Dormitory 3 Dining Hall": "DD",
    "Parking Lot P1": "PA",
    "Parking Lot P2": "PB",
    "Parking Lot P3": "PC",
    "Parking Lot P4": "PD",
    "Parking Lot P5": "PE",
    "Parking Lot P6": "PF",
    "Parking Lot P7": "PG",
    "General Parking": "P",
    "Motorcycle Shelter A": "BA",
    "Motorcycle Shelter C": "BC",
    "Motorcycle Shelter D": "BD",
    "Motorcycle Shelter H": "BH",
    "North Gate": "GN",
    "South Gate": "GS",
    "Chiao-Ching Trail": "GP",
    "Bamboo Lake": "LA",
    "Siyuan Pool": "LB",
    "Lotus Pond": "LC",
    "Detention Pond": "LD",
    "Gymnasium": "FA",
    "Swimming Pool": "FB",
    "Comprehensive Sports Hall": "FC",
    "Track and Field Stadium": "FD",
    "Basketball Court": "FE",
    "Volleyball Court": "FF",
    "Tennis Court A": "FG",
    "Tennis Court B": "FH",
    "Badminton Hall": "FI",
    "Baseball Field": "FJ",
    "Bamboo Lake Hall": "ZA",
    "Zhufeng Hall": "ZB",
    "Administrative Building": "ZC",
    "Solid-State Electronics Systems Building": "ZD",
    "Taiwan Semiconductor Research Center": "ZE",
    "Materials Laboratory and Disaster Prevention Center": "ZF",
    "Service Building": "ZG",
    "Barbecue Area": "ZH",
    "Multifunctional Activity Area": "ZI",
    "Sewage Plant": "ZJ"
}

building_full_names = list(building_dict.keys())