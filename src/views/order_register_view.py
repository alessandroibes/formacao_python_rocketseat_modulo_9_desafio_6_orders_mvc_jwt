from src.controllers.interfaces.order_register import OrderRegisterInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class OrderRegisterView(ViewInterface):
    def __init__(self, controller: OrderRegisterInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.body.get("user_id")
        description = http_request.body.get("description")

        self.__validate_inputs(user_id, description)

        response = self.__controller.registry(user_id, description)
        return HttpResponse(body=response, status_code=201)
    
    def __validate_inputs(self, user_id: any, description: any) -> None:
        if (
            not user_id
            or not description
            or not isinstance(user_id, int)
            or not isinstance(description, str)
        ): raise HttpBadRequestError("Invalid Input")
