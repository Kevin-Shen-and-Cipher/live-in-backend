from algorithm.weight import Weight


class JobWeight(Weight):
    MAX_DISTANCE_METER = 50000
    BENEFIT_WEIGTH = 2
    BENEFIT_WEIGTH_PERCEN = 0.3
    DISTANCE_WEIGTH_PERCEN = 0.7

    def get_weight(self, item):
        result = self.__get_benefit_weigth(
            item) + self.__get_distance_weight(item)

        return result

    def __get_benefit_weigth(self, item):
        benefits = item.get('benefit_set')
        weight = len(benefits) * self.BENEFIT_WEIGTH

        if (weight > 100):
            weight = 100

        weight = weight * self.BENEFIT_WEIGTH_PERCEN

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
