# -*- coding: utf-8 -*-


def test_add_node():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_node("waffles3")
    assert 'waffles' in instance.graph_dict
    assert 'waffles2' in instance.graph_dict
    assert 'waffles3' in instance.graph_dict


def test_display_nodes():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_node("waffles3")
    for waffle in ['waffles', 'waffles2', 'waffles3']:
        assert waffle in instance.nodes()


def test_add_edge():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_node("waffles")
    instance.add_node("waffles2")
    instance.add_edge('waffles', 'waffles2')
    assert instance.graph_dict['waffles'][0] == 'waffles2'


def test_add_edge_not_exist():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    assert instance.graph_dict['waffles'][0] == 'waffles2'


def test_edge_display():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge('waffles', 'waffles2')
    assert instance.edges()[0] == 'waffles-waffles2'


def test_edge_display_empty():
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    assert instance.edges() == []
