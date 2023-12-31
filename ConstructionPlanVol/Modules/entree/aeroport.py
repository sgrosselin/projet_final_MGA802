
import pandas as pd
from math import sin, cos, acos, radians


#data = pd.read_csv('Base_donnee_aeroports.csv' ,index_col=0 ,delimiter=';' ,decimal='.' ,thousands=' ')
#import pdb;pdb.set_trace()
#data.columns = ['Destination','Latitude (Nord)' ,'Longitude (Est)' ,'Altitude']


class Aeroports:
    """
    Classe Aeroports qui va être crée en utlisant le sigle IATA imposé par l'utilisateur et le fichier csv "Base_donnee_aeroports"
    """

    def __init__(self):
        data = pd.read_csv('Base_donnee_aeroports.csv', index_col=0, delimiter=';', decimal='.', thousands=' ')
        data.columns = ['Destination', 'Latitude (Nord)', 'Longitude (Est)', 'Altitude']
        self.name = str(input('Entrez le sigle IATA de l\' aéroport d\'arrivée : '))
        aeroport = data.loc[[self.name]]
        self.destination = aeroport['Destination'].values[0]
        self.latitude_arr = aeroport['Latitude (Nord)'].astype("float").values[0]
        self.longitude_arr =aeroport['Longitude (Est)'].astype("float").values[0]
        self.altitude = aeroport['Altitude'].astype("float").values[0]


    def distance_aeroports(self):
        """
        Fonction qui calcule la distance à vol d'oiseau entre l'aéroport de départ CDG et l'aéroport d'arrivée choisi par l'utilisateur

        :return: - (float) : Distance entre les aéroports en km

        """
        self.aeroport_depart='CDG'
        self.latitude_dep = 49.008014499166165
        self.longitude_dep= 2.550717852775395

        # Altitude + RT en mètres (sphère IAG-GRS80)
        RT = 6378137
        H = 12192
        # angle en radians entre les 2 points
        S = acos(sin(radians(float(self.latitude_dep))) * sin(radians(float(self.latitude_arr))) + cos(radians(float(self.latitude_dep))) * cos(radians(float(self.latitude_arr))) * cos(abs(radians(float(self.longitude_arr)) - radians(float(self.longitude_dep)))))
        # distance entre les 2 points, comptée sur un arc de grand cercle
        dist_aeroports = (S * (RT+H))/1000     ## en km
        print('\n----------------------------------------\n')
        print(f"Vôtre destination est", self.destination)
        print(f"Vous êtes à",round(dist_aeroports,2), " km de l'aéroport d'arrivé")
        return dist_aeroports

    def coordonnees_arrive(self):
        """
        Fonction qui va retourner la latitude et la longitude de l'aéroport d'arrivée

        :return:

            - (float) : latitude aéroport arrivée
            - (float) : longitude aéroport arrivée

        """
        return self.latitude_arr, self.longitude_arr

