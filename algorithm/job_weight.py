from algorithm.weight import Weight


class JobWeight(Weight):
    MAX_DISTANCE_METER = 50000

    def get_weight(self, item):
        result = self.__get_score_weigth(
            item) + self.__get_distance_weight(item)

        return result

    def __get_score_weigth(self, item):
        score = item.get("score")

        if (score > 100):
            weight = 30
        else:
            weight = score * 0.3

        return weight

    def __get_distance_weight(self, item):
        coordinate1 = item.get("coordinate")
        coordinate2 = self.google_api.get_coordinate(self.address)
        distance = self.google_api.get_distance(coordinate1, coordinate2)

        if (distance > self.MAX_DISTANCE_METER):
            weight = 0
        else:
            weight = (1 - distance / self.MAX_DISTANCE_METER) * 70

        return weight
