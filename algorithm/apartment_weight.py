from algorithm.weight import Weight


class ApartmentWeight(Weight):
    MAX_DISTANCE_METER = 50000
    FACILITY_WEIGTH = {"捷運": 10, "公車": 1, "學校": 5}
    FACILITY_WEIGTH_PERCEN = 0.3
    DISTANCE_WEIGTH_PERCEN = 0.7

    def get_weight(self, item):
        result = self.__get_facility_weigth(
            item) + self.__get_distance_weight(item)

        return result

    def __get_facility_weigth(self, item):
        facilities = item.get('surroundingfacility_set')
        weight = 0

        for facility in facilities:
            weight += self.FACILITY_WEIGTH[facility['name']]

        if (weight > 100):
            weight = 100

        weight = weight * self.FACILITY_WEIGTH_PERCEN

        return weight

    def __get_distance_weight(self, item):
        coordinate1 = item.get("coordinate")
        coordinate2 = self.google_api.get_coordinate(self.address)
        distance = self.google_api.get_distance(coordinate1, coordinate2)

        if (distance > self.MAX_DISTANCE_METER):
            weight = 0
        else:
            weight = (1 - distance / self.MAX_DISTANCE_METER) * \
                self.DISTANCE_WEIGTH_PERCEN * 100

        return weight
