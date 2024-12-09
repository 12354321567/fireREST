from typing import Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_610, API_RELEASE_621
from fireREST.fmc import ChildResource
from .response import AccessRuleResponse


class AccessRule(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/accessrules/{uuid}'
    SUPPORTED_PARAMS = ['category', 'section', 'insert_before', 'insert_after']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_621
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        category=None,
        section=None,
        insert_after=None,
        insert_before=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)

    @utils.support_params
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None) -> list[AccessRuleResponse] | AccessRuleResponse:
        result = super().get(container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params)

        if type(result) == list:
            return [AccessRuleResponse(**access_rule) for access_rule in result]
        elif type(result) == dict:
            return AccessRuleResponse(**result)
