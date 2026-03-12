class PointsForPlace:
    points = 0
    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return points
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return points
        else:
            points = 101 - place
            return points


class PointsForMeters:
    points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return points
        else:
            points = meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    @staticmethod
    def get_total_points(place, meters):
        points_for_place = PointsForPlace.get_points_for_place(place)
        points_for_meters = PointsForMeters.get_points_for_meters(meters)
        total = points_for_place + points_for_meters
        return total