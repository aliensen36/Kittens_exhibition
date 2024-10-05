from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
import kittens_app.views



class KittenViewSetExtension(OpenApiViewExtension):
    target_class = kittens_app.views.KittenViewSet

    def view_replacement(self):
        @extend_schema(tags=['Kittens'])
        class Fixed(self.target_class):

            @extend_schema(
                summary="List kittens",
                description="Retrieve a list of kittens. Optionally filter by breed ID.",
                parameters=[
                    OpenApiParameter(
                        "breed_id",
                        OpenApiTypes.INT,
                        OpenApiParameter.QUERY,
                        description="Filter by breed ID",
                        required=False,
                    ),
                ],
                responses={
                    200: OpenApiResponse(
                        description="List of kittens",
                        examples=[
                            OpenApiExample(
                                "Example response",
                                value=[
                                    {
                                        "id": 1,
                                        "name": "Мурзик",
                                        "color": "Серый",
                                        "age": 12,
                                        "description": "Игривый котенок",
                                        "breed": 3,
                                        "owner": 1
                                    },
                                    {
                                        "id": 2,
                                        "name": "Барсик",
                                        "color": "Белый",
                                        "age": 8,
                                        "description": "Ласковый котенок",
                                        "breed": 1,
                                        "owner": 2
                                    }
                                ]
                            )
                        ]
                    )
                }
            )
            def list(self, request, *args, **kwargs):
                return super().list(request, *args, **kwargs)

            @extend_schema(
                summary="Create a kitten",
                description="Add a new kitten. The kitten will be linked to the current user.",
                request=OpenApiTypes.OBJECT,
                responses={
                    201: OpenApiResponse(
                        description="Kitten successfully created",
                        examples={
                            "id": 1,
                            "name": "Мурзик",
                            "color": "Серый",
                            "age": 12,
                            "description": "Игривый котенок",
                            "breed": 3,
                            "owner": 1
                        }
                    )
                }
            )
            def create(self, request, *args, **kwargs):
                return super().create(request, *args, **kwargs)

            @extend_schema(
                summary="Get a kitten",
                description="Retrieve details of a specific kitten.",
                parameters=[
                    OpenApiParameter(
                        "kitten_id",
                        OpenApiTypes.INT,
                        OpenApiParameter.PATH,
                        description="ID of the kitten to retrieve",
                        required=True,
                    ),
                ],
                responses={
                    200: OpenApiResponse(
                        description="Kitten details",
                        examples={
                            "id": 1,
                            "name": "Мурзик",
                            "color": "Серый",
                            "age": 12,
                            "description": "Игривый котенок",
                            "breed": 3,
                            "owner": 1
                        }
                    ),
                    404: OpenApiResponse(
                        description="Kitten not found",
                        examples={"error": "Kitten not found"}
                    )
                }
            )
            def retrieve(self, request, pk, *args, **kwargs):
                return super().retrieve(request, pk, *args, **kwargs)

            @extend_schema(
                summary="Update a kitten",
                description="Update details of a specific kitten. Only the owner can update their kitten.",
                parameters=[
                    OpenApiParameter(
                        "kitten_id",
                        OpenApiTypes.INT,
                        OpenApiParameter.PATH,
                        description="ID of the kitten to update",
                        required=True,
                    ),
                ],
                responses={
                    200: OpenApiResponse(
                        description="Kitten successfully updated",
                        examples={
                            "id": 1,
                            "name": "Мурзик",
                            "color": "Серый",
                            "age": 12,
                            "description": "Игривый котенок",
                            "breed": 3,
                            "owner": 1
                        }
                    ),
                    403: OpenApiResponse(
                        description="Error: You are not authorized to update this kitten",
                        examples={"error": "You are not authorized to update this kitten"}
                    )
                }
            )
            def update(self, request, pk, *args, **kwargs):
                return super().update(request, pk, *args, **kwargs)

            @extend_schema(
                summary="Delete a kitten",
                description="Remove a specific kitten. Only the owner can delete their kitten.",
                parameters=[
                    OpenApiParameter(
                        "kitten_id",
                        OpenApiTypes.INT,
                        OpenApiParameter.PATH,
                        description="ID of the kitten to delete",
                        required=True,
                    ),
                ],
                responses={
                    204: OpenApiResponse(
                        description="Kitten successfully deleted"
                    ),
                    403: OpenApiResponse(
                        description="Error: You are not authorized to delete this kitten",
                        examples={"error": "You are not authorized to delete this kitten"}
                    )
                }
            )
            def destroy(self, request, pk, *args, **kwargs):
                return super().destroy(request, pk, *args, **kwargs)

        return Fixed

class BreedViewSetExtension(OpenApiViewExtension):
    target_class = kittens_app.views.BreedViewSet

    def view_replacement(self):
        @extend_schema(tags=['Breeds'])
        class Fixed(self.target_class):

            @extend_schema(
                summary="List breeds",
                description="Retrieve a list of all cat breeds.",
                responses={
                    200: OpenApiResponse(
                        description="List of breeds",
                        examples=[
                            OpenApiExample(
                                "Example response",
                                value=[
                                    {
                                        "id": 1,
                                        "name": "Персидская"
                                    },
                                    {
                                        "id": 2,
                                        "name": "Британская"
                                    }
                                ]
                            )
                        ]
                    )
                }
            )
            def list(self, request, *args, **kwargs):
                return super().list(request, *args, **kwargs)

        return Fixed
