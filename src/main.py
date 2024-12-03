from init import *

pygame.init()
SCREEN_WIDTH = 1304
SCREEN_HEIGHT = 862
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NYCU Campus Map Navigation System")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

OFFSET_X = 0
OFFSET_Y = 0

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
manager.get_theme().load_theme(theme_data)

title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 650 // 2, 50), (650, 70)),
    text="NYCU Campus Map Navigation System",
    manager=manager
)

Departure_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((SCREEN_WIDTH // 4 - 330, SCREEN_HEIGHT // 2 - 100 - 200), (650, 70)),
    text="Departure",
    manager=manager
)

destination_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((3 * SCREEN_WIDTH // 4 - 330, SCREEN_HEIGHT // 2 - 100 - 200), (650, 70)),
    text="Destination",
    manager=manager
)

Show_distance_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 800), (300, 70)),
    text="Distance : ",
    manager=manager
)

dropdown_manager = DropdownManager()
departure_dropdown = Dropdown(
    name = "departure",
    options = building_full_names,
    starting_option = building_full_names[0],
    position = (SCREEN_WIDTH // 4 - 300 // 2, SCREEN_HEIGHT // 2 - 35 - 200),
    size = (300, 40),
    manager=manager
)
dropdown_manager.add_dropdown(departure_dropdown)
destination_dropdown = Dropdown(
    name = "destination",
    options = building_full_names,
    starting_option = building_full_names[0],
    position = (3 * SCREEN_WIDTH // 4 - 300 // 2, SCREEN_HEIGHT // 2 - 35 - 200),
    size = (300, 40),
    manager=manager
)
dropdown_manager.add_dropdown(destination_dropdown)

start_button = Button(
    text="Start",
    position=(SCREEN_WIDTH // 2 - 300 // 2, SCREEN_HEIGHT - 150 - 200),
    size=(300, 40),
    manager=manager
)
back_button = Button(
    text="Back",
    position=(10, 10),
    size=(200, 40),
    manager=manager
)

# dropdown.hide()
def main():
    campus_map = Map("../image/campus_map.png", OFFSET_X, OFFSET_Y)
    locations = LocationManager(OFFSET_X, OFFSET_Y)
    STATE = 0
    initialize_locations(locations)
    edges = EdgeManager(locations, OFFSET_X, OFFSET_Y)
    path_length_route = Path_Data('../data/output.json')
    initialize_edge(edges)
    bg = ScrollingBackground("../image/campus_map.png", SCREEN_WIDTH, SCREEN_HEIGHT, 1, blur_radius = 10)
    running = True
    departure = 0
    destination = 0
    while running:
        time_delta = clock.tick(FPS) / 1000.0
        button_click = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            dropdown_manager.handle_event(event)
            if STATE == 0:
                if start_button.handle_event(event):
                    button_click = 1
            elif STATE == 1:
                if back_button.handle_event(event):
                    button_click = 1
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill(BLACK)
        if STATE == 0:
            bg.update()
            bg.draw(screen)
            start_button.show()
            back_button.hide()
            destination_label.show()
            Departure_label.show()
            title_label.show()
            Show_distance_label.hide()
            dropdown_manager.show_all()
            manager.draw_ui(screen)
            if button_click:
                departure_building_code = departure_dropdown.get_selected_option()
                destination_building_code = destination_dropdown.get_selected_option()
                departure = building_code_to_node_index[building_dict[departure_building_code]]
                destination = building_code_to_node_index[building_dict[destination_building_code]]
                STATE = 1
        elif STATE == 1:
            start_button.hide()
            back_button.show()
            destination_label.hide()
            Departure_label.hide()
            title_label.hide()
            dropdown_manager.hide_all()

            path_w = path_length_route.path_length(departure, destination)
            path_route = path_length_route.path_route(departure, destination)
            locations.set_group_visible(path_route)
            edges.set_path_edge_visible(path_route)

            Show_distance_label.set_text(f'Distance : {path_w} m')
            Show_distance_label.show()
            campus_map.draw(screen)
            locations.draw_locations(screen)
            edges.draw_all_the_edges(screen)
            manager.draw_ui(screen)

            if button_click:
                STATE = 0

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()