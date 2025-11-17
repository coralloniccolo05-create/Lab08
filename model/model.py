
from database.impianto_DAO import ImpiantoDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Model:
    def __init__(self):
        self._impianti = None
        self.load_impianti()

        self.__sequenza_ottima = []
        self.__costo_ottimo = -1

    def load_impianti(self):
        """ Carica tutti gli impianti e li setta nella variabile self._impianti """
        self._impianti = ImpiantoDAO.get_impianti()

    def get_consumo_medio(self, mese:int):
        """
        Calcola, per ogni impianto, il consumo medio giornaliero per il mese selezionato.
        :param mese: Mese selezionato (un intero da 1 a 12)
        :return: lista di tuple --> (nome dell'impianto, media), es. (Impianto A, 123)
        """
        # TODO
        consumi_per_impianto = {}
        lista_result = []
        for impianto in self._impianti:
            lista_consumi = impianto.get_consumi()
            for consumo in lista_consumi:
                if consumo.data.month == mese:
                    if consumo.id_impianto not in consumi_per_impianto: #creo dizionario con gli id ch leggo
                        consumi_per_impianto[consumo.id_impianto] = {'nome': impianto.nome,
                                                                    'kwh': []}
                    consumi_per_impianto[consumo.id_impianto]['kwh'].append(float(consumo.kwh))
        for valori in consumi_per_impianto.values():
            lista_consumi = valori['kwh']
            media_consumi = sum(lista_consumi)/len(lista_consumi)
            lista_result.append((valori['nome'], media_consumi))
        return lista_result


    def get_sequenza_ottima(self, mese:int):
        """
        Calcola la sequenza ottimale di interventi nei primi 7 giorni
        :return: sequenza di nomi impianto ottimale
        :return: costo ottimale (cioè quello minimizzato dalla sequenza scelta)
        """
        self.__sequenza_ottima = []
        self.__costo_ottimo = -1
        consumi_settimana = self.__get_consumi_prima_settimana_mese(mese)

        self.__ricorsione([], 1, None, 0, consumi_settimana)

        # Traduci gli ID in nomi
        id_to_nome = {impianto.id: impianto.nome for impianto in self._impianti}
        sequenza_nomi = [f"Giorno {giorno}: {id_to_nome[i]}" for giorno, i in enumerate(self.__sequenza_ottima, start=1)]
        return sequenza_nomi, self.__costo_ottimo


    def __ricorsione(self, sequenza_parziale, giorno, ultimo_impianto, costo_corrente, consumi_settimana):
        """ Implementa la ricorsione """
        # TODO
        # Condizione terminale o di uscita
        if ...:
            ...
        # Condizione ricorsiva
        else:
            ...

    def __get_consumi_prima_settimana_mese(self, mese: int):
        """
        Restituisce i consumi dei primi 7 giorni del mese selezionato per ciascun impianto.
        :return: un dizionario: {id_impianto: [kwh_giorno1, ..., kwh_giorno7]}
        """
        # TODO
        consumi_prima_setttimana = {}
        for impianto in self._impianti:
            lista_consumi = impianto.get_consumi()
            for consumo in lista_consumi:
                if consumo.data.month == mese:
                    if consumo.data.day <= 7:
                        if consumo.id_impianto not in consumi_prima_setttimana: #creo dizionario con gli id ch leggo
                            consumi_prima_setttimana[consumo.id_impianto] = {'id_impianto': impianto.id,
                                                                             'kwh': []}
                        consumi_prima_setttimana[consumo.id_impianto]['kwh'].append(float(consumo.kwh))
        return consumi_prima_setttimana

