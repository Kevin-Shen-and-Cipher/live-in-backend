from django.db.models import QuerySet
from django.http import QueryDict


class JobFilter(object):

    def filter_all(querys: QueryDict, queryset: QuerySet):
        queryset = JobFilter.filter_district(querys, queryset)
        queryset = JobFilter.filter_salary(querys, queryset)
        queryset = JobFilter.filter_job_position(querys, queryset)
        queryset = JobFilter.filter_working_hour(querys, queryset)

        return queryset

    # 區域篩選
    def filter_district(querys: QueryDict, queryset: QuerySet):
        district = querys.getlist("district")

        if (district):
            district = list(map(int, district))

            queryset = queryset.filter(district__in=district)

        return queryset

    # 薪水篩選
    def filter_salary(querys: QueryDict, queryset: QuerySet):
        min_salary = querys.get("min_salary")

        if (min_salary):
            min_salary = int(min_salary)

            queryset = queryset.filter(
                salary__gte=min_salary)

        return queryset

    # 職位篩選
    def filter_job_position(querys: QueryDict, queryset: QuerySet):
        job_positions = querys.getlist("job_position")
        
        if (job_positions):
            job_positions = list(map(int, job_positions))

            queryset = queryset.filter(job_position__in=job_positions)

        return queryset

    # 工作時段篩選
    def filter_working_hour(querys: QueryDict, queryset: QuerySet):
        working_hours = querys.getlist("working_hour")

        if (working_hours):
            working_hours = list(map(int, working_hours))

            queryset = queryset.filter(working_hour__in=working_hours)

        return queryset
