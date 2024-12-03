from edge import Edge
from replace_num_to_Location import node_index_to_building_code

class EdgeManager:
    def __init__(self, location_manager, offset_x, offset_y):
        self.edges = []
        self.location_manager = location_manager
        self.offset_x = offset_x
        self.offset_y = offset_y

    def add_edge(self, start_node, end_node, weight=1):
        edge = Edge(self.location_manager, start_node, end_node, weight, offset_x = self.offset_x, offset_y = self.offset_y)
        self.edges.append(edge)

    def remove_edge(self, start_node, end_node):
        self.edges = [edge for edge in self.edges if not (edge.start_node == start_node and edge.end_node == end_node)]

    def find_edges_from(self, node):
        return [edge for edge in self.edges if edge.start_node == node]

    def find_edges_to(self, node):
        return [edge for edge in self.edges if edge.end_node == node]

    def display_edges_at_terminal(self):
        for edge in self.edges:
            print(edge.start_node, edge.end_node)

    def draw_all_the_edges(self, screen):
        for edge in self.edges:
            edge.draw(screen)
    
    def set_all_edge_invisible(self):
        for edge in self.edges:
            edge.is_show = 0
    
    def set_all_edge_visible(self):
        for edge in self.edges:
            edge.is_show = 1

    def set_single_edge_visible(self, start_node, end_node):
        for edge in self.edges:
            if edge.start_node == start_node and edge.end_node == end_node:
                edge.is_show = 1
                return

    def set_path_edge_visible(self, path):
        self.set_all_edge_invisible()
        for i in range(1, len(path)):
            self.set_single_edge_visible(path[i - 1], path[i])