from graphviz import Digraph

dot = Digraph(comment='Family Tree')
dot.node('A', 'John')
dot.node('B', 'Mary')
dot.node('C', 'Bob')
dot.edges(['AB', 'AC'])

dot.attr('graph', style='filled', bgcolor='white')
dot.attr('node', shape='circle', style='filled', color='lightgrey', fontname='Helvetica')
dot.attr('edge', style='dashed', color='lightgrey', arrowhead='open')

dot.attr('node', fillcolor='red')
dot.edge('B', 'C', constraint='false')

dot.attr(stylesheet='style.css')  # Встановлюємо CSS-файл
dot.render('test-output/family-tree', view=True)
