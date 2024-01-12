from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from AutoTechApi.car.models import Car, CarMake
from AutoTechApi.utils.general_function import valid_id


class CarMakeViewSet(APIView):

    @staticmethod
    def get(request):
        car_make_name = request.query_params.get('car_make_name')

        car_make_list = CarMake.objects.all()
        data = []

        if car_make_name is not None:
            if len(car_make_name) == 0:
                return Response({'message': 'infome um nome da marca'}, status=status.HTTP_400_BAD_REQUEST)

            if len(car_make_list) != 0:
                car_make_list = car_make_list.filter(name__icontains=car_make_name)
                data = [{
                    'id': car_make.id,
                    'name': car_make.name
                } for car_make in car_make_list]
        else:
            if len(car_make_list) != 0:
                data = [{
                    'id': car_make.id,
                    'name': car_make.name
                } for car_make in car_make_list]

        content = {'message': 'processado com sucesso', 'data': data}
        return Response(content, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        name = request.data.get('name')

        if name is None or len(name) == 0:
            return Response({'message': 'informe um nome'}, status=status.HTTP_400_BAD_REQUEST)

        name_lower = name.lower()

        car_make = CarMake(
            name=name_lower
        )

        car_make.save()

        return Response({'message': 'criado com sucesso'}, status=status.HTTP_201_CREATED)

    #@staticmethod
    # def patch(request):
    #     car_make_id = request.data.get('car_make_id')
    #     name = request.data.get('name')
    #
    #     try:
    #         car_make = CarMake.objects.get(id=car_make_id):
    #
    #     if name is None or len(name) == 0:
    #         return Response({'message': 'informe um nome'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     name_lower = name.lower()
    #
    #     car_make = CarMake(
    #         name=name_lower
    #     )
    #
    #     car_make.save()
    #
    #     return Response({'message': 'criado com sucesso'}, status=status.HTTP_201_CREATED)




class CarViewSet(APIView):
    renderer_classes = [JSONRenderer]

    @staticmethod
    def get(request):
        data = [{
            'placa': car.license_plate,
            'veiculo': f'{car.car_make} - {car.car_model}',
            'KM': car.kilometers,
            'cliente': car.client.name
        } for car in Car.objects.filter(is_active=True)]

        content = {'message': 'processado com sucesso', 'data': data}
        return Response(content, status=status.HTTP_200_OK)
