from model.model import Model

mdl = Model()
mdl.buildGraph()
print(f"Grafo Creato. Contiene {mdl.getNumNodes()} nodi e {mdl.getNumEdges()} archi.")

mdl.getInfoCompConnessa(1224)