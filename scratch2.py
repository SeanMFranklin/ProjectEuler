import graphviz

g = graphviz.Graph(filename='city.gv', format='png')
g.edge('Horse(h)','Offspring(h,h2)')
g.edge('Horse(h)','Horse(Bluebeard)')
g.edge('Offspring(h,h2)','Parent(h2,h)')
g.edge('Horse(Bluebeard)','Offspring(Bluebeard,h2)')
g.edge('Offspring(Bluebeard,h2)','Parent(h2,Bluebeard)')
g.edge('Parent(h2,Bluebeard)','Offspring(Bluebeard,h2)')

g.view()