import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        ruolo = self._view.dd_ruolo.value
        if ruolo is None:
            self._view.create_alert("Selezionare un ruolo")
            return
        grafo = self._model.creaGrafo(ruolo)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))

        self._view.update_page()

    def handle_connessi(self, e):
        lista = self._model.analisi()
        for (a1, a2, peso) in lista:
            self._view.txt_result.controls.append(ft.Text(f"{a1} e {a2} con {peso} esibizioni in comune"))
        self._view.update_page()
    def fillDD(self):
        ruoli=self._model.getRuoli
        for ruolo in ruoli:
            self._view.dd_ruolo.options.append(ft.dropdown.Option(
                text=ruolo))