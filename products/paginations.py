from rest_framework.pagination import PageNumberPagination

class ProductsPaginations(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'limit'
    max_page_size = 100