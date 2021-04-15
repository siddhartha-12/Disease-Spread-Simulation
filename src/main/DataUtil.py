from Person import Person
from ConfigUtil import ConfigUtil
import logging
import numpy as np
from SimulationData import SimalationData
import random
from numpy.random import choice
from collections import defaultdict


class DataUtil:

    def __init__(self):
        self.cu = ConfigUtil.get_instance()

    def getLocationInfected(self,personDataset:list) -> list:
        x_coordinate  = list()
        y_coordinate = list()
        for i in personDataset:
            if i.get_infected():
                x_coordinate.append(i.get_x())
                y_coordinate.append(i.get_y())
        return [x_coordinate,y_coordinate]
    
    def getLocationHealthy(self,personDataset:list) -> list:
        x_coordinate  = list()
        y_coordinate = list()
        for i in personDataset:
            if not i.get_infected() or i.get_recovered():
                x_coordinate.append(i.get_x())
                y_coordinate.append(i.get_y())
        return [x_coordinate,y_coordinate]

    def getLocationRecovered(self,personDataset:list) -> list:
        x_coordinate  = list()
        y_coordinate = list()
        for i in personDataset:
            if i.get_recovered:
                x_coordinate.append(i.get_x())
                y_coordinate.append(i.get_y())
        return [x_coordinate,y_coordinate]

    def getLocationVaccincated(self,personDataset:list) -> list:
        x_coordinate  = list()
        y_coordinate = list()
        for i in personDataset:
            if i.get_recovered:
                x_coordinate.append(i.get_x())
                y_coordinate.append(i.get_y())
        return [x_coordinate,y_coordinate]

    def getLocationOfMaskedPerson(self,personDataset:list) -> list:
        x_coordinate  = list()
        y_coordinate = list()
        for i in personDataset:
            if i.get_mask_usage:
                x_coordinate.append(i.get_x())
                y_coordinate.append(i.get_y())
        return [x_coordinate,y_coordinate]
    
    def getTotalCountInfected(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountHealthy(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountDead(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountRecovered(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountMask(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountQuarantine(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count
    def getTotalCountRecovered(self,personDataset:list) -> int:
        count = 0 
        for i in personDataset:
            if i.get_infected():
                count +=1
        return count

    def getTotalCountAll(self,personDataset:list) -> dict:
        count = 0 
        count_dict = defaultdict(int)
        for i in personDataset:
            if i.get_infected():
                count_dict["Infected"] +=1
            if i.get_can_infect()>0:
                count_dict["Super"] +=1
            if i.get_recovered():
                count_dict["Recover"] +=1
            if i.get_deceased():
                count_dict["Dead"] +=1
            if i.get_mask_usage():
                count_dict["Mask"] +=1
            if i.get_qurantine():
                count_dict["Quarantine"] +=1
            if i.get_vaccinated():
                count_dict["Vaccinate"] +=1
        return count_dict

if __name__=="__main__":
    du = DataUtil()
    # covid = SimalationData()
    # covid.intialData() #pass the name of the virus to fetch corresponding data
    # print("Infected person " + str(du.getTotalCountInfected(covid.intialData())))

    # du.testInfectionProbability(8)