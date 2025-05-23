from src.controllers.interfaces.fetch_orders_by_user import FetchOrdersByUserInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class FetchOrderByUserView(ViewInterface):
    def __init__(self, controller: FetchOrdersByUserInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.params["user_id"]
        header_user_id = http_request.headers.get("uid")

        self.__validate_inputs(user_id, header_user_id)

        response = self.__controller.get_orders_by_user(user_id)
        return HttpResponse(body=response, status_code=201)
    
    def __validate_inputs(self, user_id: any, header_user_id: any) -> None:
        if (
            not user_id
            or not user_id.isdigit()
            or int(header_user_id) != int(user_id)
        ): raise HttpBadRequestError("Invalid Input")
