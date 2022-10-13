from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from scrapper.utils import ClinicaSantaMariaViews, RecetasDeCocinaViews, TablaDeCaloriasViews

@api_view(['GET'])
def get_data_clinica_santa_maria(request: WSGIRequest) -> Response:

    respuesta = ClinicaSantaMariaViews.get_data()

    if respuesta == True:
        return Response(status=status.HTTP_200_OK,
                    data={"response": f"Data extraida con exito"})
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"response": f"Error al extraer la data"})


@api_view(['GET'])
def get_data_recetas_de_cocinas(request: WSGIRequest) -> Response:

    respuesta = RecetasDeCocinaViews.get_data()

    if respuesta == True:
        return Response(status=status.HTTP_200_OK,
                    data={"response": f"Data extraida con exito"})
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"response": f"Error al extraer la data"})


@api_view(['GET'])
def get_data_tabla_de_calorias(request: WSGIRequest) -> Response:

    respuesta = TablaDeCaloriasViews.get_data()

    if respuesta == True:
        return Response(status=status.HTTP_200_OK,
                    data={"response": f"Data extraida con exito"})
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"response": f"Error al extraer la data"})