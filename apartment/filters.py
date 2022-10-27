from django.http import QueryDict
from django.db.models import QuerySet


class ApartmentFilter(object):

    def filter_all(querys: QueryDict, queryset: QuerySet):
        queryset = ApartmentFilter.filter_district(querys, queryset)
        queryset = ApartmentFilter.filter_price(querys, queryset)
        queryset = ApartmentFilter.filter_rent_type(querys, queryset)
        queryset = ApartmentFilter.filter_apartment_type(querys, queryset)
        queryset = ApartmentFilter.filter_room_type(querys, queryset)
        queryset = ApartmentFilter.filter_restrict(querys, queryset)
        queryset = ApartmentFilter.filter_device(querys, queryset)

        return queryset

    # 區域篩選
    def filter_district(querys: QueryDict, queryset: QuerySet):
        district = querys.getlist("district")
        if (district):
            queryset = queryset.filter(distrcit__in=district)

        return queryset

    # 價格篩選
    def filter_price(querys: QueryDict, queryset: QuerySet):
        min_price = querys.get("min_price")
        max_price = querys.get("max_price")

        if (min_price and max_price):
            queryset = queryset.filter(
                price__range=(int(min_price), int(max_price)))

        return queryset

    # 租屋類型篩選
    def filter_rent_type(querys: QueryDict, queryset: QuerySet):
        rent_types = querys.getlist("rent_type")
        if (rent_types):
            queryset = queryset.filter(rent_type__in=rent_types)

        return queryset

    # 房子類型篩選
    def filter_apartment_type(querys: QueryDict, queryset: QuerySet):
        apartment_types = querys.getlist("apartment_type")
        if (apartment_types):
            queryset = queryset.filter(apartment_type__in=apartment_types)

        return queryset

    # 格局篩選
    def filter_room_type(querys: QueryDict, queryset: QuerySet):
        room_types = querys.getlist("room_type")
        if (room_types):
            queryset = queryset.filter(room_type__in=room_types)

        return queryset

    # 限制篩選
    def filter_restrict(querys: QueryDict, queryset: QuerySet):
        restricts = querys.getlist("restrict")
        if (restricts):
            queryset = queryset.filter(restrict__in=restricts)

        return queryset

    # 設備篩選
    def filter_device(querys: QueryDict, queryset: QuerySet):
        devices = querys.getlist("device")
        if (devices):
            queryset = queryset.filter(device__in=devices)

        return queryset
